from posixpath import expanduser
from PyQt5.QtWidgets import QMainWindow , QApplication, QComboBox, QLineEdit , QPushButton,QSpinBox, QCheckBox, QRadioButton, QProgressBar, QScrollArea, QFrame, QLabel,QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5 import uic
from youtubeOOP import dn_playlist, dn_search,dn_youtube
from spotify import spotAPI
from pytube import request
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QSize, QMutex
from PyQt5.QtGui import QMovie
from os import path
request.default_range_size = 1048576*2   # this is for chunck size, 2MB size
#empty list to carry all objects we create all objects of dn_youtube
objs_handler=[]
#empty list to carry all *QCheckBoxS* to give the user feature of choosing videos from playlist
tracks_check=[]
#obect to prevent parallel access to data
# mutex=QMutex()

#class that handels threads for search ing and downloading
class Worker(QObject):
    def __init__(self,url=None,index=None,res=None,location=''):
        super().__init__()
        self.url=url
        self.index=index
        self.res=res
        self.location=location
    finished=pyqtSignal()
    search_progress=pyqtSignal(str)#to emit search result one by one (Emit string ->track info)
    download_progress=pyqtSignal(int)#to emit downloaded chunks for the progress bar
    downloaded_one=pyqtSignal()#to emit siganl that one tracks download is finished not all the process [for playlists in general]

    # url and index to not make that thread interact with the event loop
    def run_search(self):
        '''here the code for search and download to not freaze program'''
        global objs_handler
        # mutex.lock()#save the data from prallel access
        if self.index==0:
            obj=dn_youtube(self.url)
            #save obj in objs_handler for download(the operation after that)
            objs_handler.append(obj)
            title_temp=obj.get_info()
            #emit title only
            self.search_progress.emit(title_temp)
            # mutex.unlock()
        elif self.index==1:
            obj=dn_playlist(self.url)
            for video in obj.get_links():#links
                temp_obj=dn_youtube(video)
                #save obj in objs_handler for download(the operation after that)
                objs_handler.append(temp_obj)
                title_temp=temp_obj.get_info()
                #emit title only
                self.search_progress.emit(title_temp)
                # self.search_progress.emit(dn_youtube(video).get_info())
        elif self.index==2:
            self.search_function(search_key=self.url)
        elif self.index==3:#spotify track
            obj=spotAPI(self.url)
            titles_temp=obj.request_track()#list of data
            if titles_temp:
                for title in titles_temp:
                    self.search_function(title)
        elif self.index==4:
            obj=spotAPI(self.url)
            titles_temp=obj.request_playlist()#list of data
            if titles_temp:
                for title in titles_temp:
                    self.search_function(title)
        self.finished.emit()

    #function to do search will be used with search youtube and spotify->spotify will return list of data only
    #emit video title
    def search_function(self,search_key):
        global objs_handler
        obj=dn_search(search_key)#here search key not url 
        objs_handler.append(obj)
        title_temp=obj.get_info()
        #emit title only
        self.search_progress.emit(title_temp)

    #function to send singals of downlaod 
    def run_download(self):
        #go through each youtube video and download it[at this point we edited objs_handler to have only user choices]
        for video in range(len(objs_handler)):
            if objs_handler[video]!=0:
                objs_handler[video].set_progress_callback(self.progress_callback)
                objs_handler[video].set_complete_callback(self.complete_callback)
                objs_handler[video].download_stream(self.res,self.location)
        self.finished.emit()

    #function will be called each time youtube download chunk
    def progress_callback(self,stream, chunk, bytes_remaining):
        size = stream.filesize
        progress_value = int(((size - bytes_remaining) / size) * 100)
        # print(progress)
        self.download_progress.emit(progress_value)
        # do call progress bar from GUI here

    #function will be called when the download is completed
    def complete_callback(self,stream, file_handle):
        self.downloaded_one.emit()

class UI(QMainWindow):   
    def __init__(self):
        super(UI,self).__init__()

        #laod ui file
        uic.loadUi("secEdition.ui",self)

        #define widgets
        self.which_download=self.findChild(QComboBox,"which_download")
        self.url_input=self.findChild(QLineEdit,"url_input")
        self.search_button=self.findChild(QPushButton,"search_button")
        self.from_spotify=self.findChild(QSpinBox,"from_spotify")
        self.loading_gif=self.findChild(QLabel,"loading_gif")
        self.end_process_button=self.findChild(QPushButton,"end_process_button")
        # Loading the GIF
        self.movie = QMovie("images\\Spinner-1s-200px.gif")
        self.loading_gif.setMovie(self.movie)
        self.check_all=self.findChild(QCheckBox,"check_all")
        # self.pick_song=self.findChild(QCheckBox,"pick_song")
        self.res360_download=self.findChild(QRadioButton,"res360_download")
        self.res720_download=self.findChild(QRadioButton,"res720_download")
        self.audio_download=self.findChild(QRadioButton,"audio_download")
        self.download_button=self.findChild(QPushButton,"download_button")
        self.download_progress=self.findChild(QProgressBar,"download_progress")
        self.download_frame=self.findChild(QFrame,"download_frame")
        self.output_area=self.findChild(QScrollArea,"output_area")

        #initlizing some attributes
        self.initialize()
        self.which_download.currentIndexChanged.connect(self.combobox_change)#what happen when changing combobox index
        self.check_all.stateChanged.connect(lambda:self.check_all_fun())#to excuate function when state of checkbutton change\
        self.search_button.clicked.connect(self.search_fun)
        self.download_button.clicked.connect(self.download_fun)
        self.end_process_button.clicked.connect(self.restet_after_download)
        #show app
        self.show()

    #function to set initliazing the ui 
    def initialize(self):
        self.loading_gif.hide()
        self.from_spotify.hide()
        self.check_all.hide()
        # self.pick_song.hide()
        self.download_frame.hide()
        self.end_process_button.hide()
        # self.download_progress.hide()

    #function to show or hide from_Spotify when combobox change
    def combobox_change(self):
        if self.which_download.currentIndex()==4:
            self.from_spotify.show()
            self.from_spotify.setEnabled(True)
        else:
            self.from_spotify.hide()

    #set check all function to select or diselect all tracks at once
    def check_all_fun(self):
        if self.check_all.checkState()==0:
            for item in tracks_check:
                item.setChecked(False)
        if self.check_all.checkState()==2:
            for item in tracks_check:
                item.setChecked(True)  
    
    #function to show loading gif and disable the window
    def run_loading(self):
        self.loading_gif.show()
        self.movie.start()
        self.setEnabled(False)#to disable main window

    #function to stop loading after search is done and enable window again
    def reset_after_search(self):
        self.movie.stop()
        self.loading_gif.hide()
        self.setEnabled(True)
        #edit widgets
        self.search_button.setEnabled(False)
        self.url_input.setEnabled(False)
        self.which_download.setEnabled(False)
        #edit widgets
        self.check_all.show()
        self.check_all.setEnabled(True)
        self.verticalLayout.addWidget(self.download_frame)
        self.download_frame.show()
        self.end_process_button.show()

    #function search go to worker thread and return objs data as finished signal
    def search_fun(self):
        url=self.get_url()
        index=self.which_download.currentIndex()
        self.search_thread(url,index)
    
    def search_thread(self,url,index):
        #define thread
        self.thread=QThread()
        self.worker=Worker(url,index)
        self.worker.moveToThread(self.thread)
        #set signals
        self.thread.started.connect(self.run_loading)
        self.thread.started.connect(self.worker.run_search)
        self.worker.search_progress.connect(self.create_check_gui)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #start thread
        self.thread.start()
        #settings after start the thread
        
        self.thread.finished.connect(self.reset_after_search)
    #not anymore->to create gui for the results [each track as check box as general rule to give the user apility to choose songs from playlists]
    #now->get only the title and create gui and append QCheckBox in tracks_check
    def create_check_gui(self,track_title):
        global tracks_check
        # mutex.lock()
        self.pick_song = QCheckBox(self.scrollAreaWidgetContents)
        self.pick_song.setMinimumSize(QSize(0, 25))
        self.pick_song.setChecked(True)
        self.pick_song.setAutoRepeat(False)
        self.pick_song.setTristate(False)
        self.pick_song.setObjectName("pick_song")
        self.pick_song.setText(f"{track_title}") #titles
        #global list
        tracks_check.append(self.pick_song)#to know user choices
        self.verticalLayout.addWidget(self.pick_song)

    #function to control global list objs_handler with the user choices , through tracks_check[global list]
    def get_choices(self):
        for track in range(len(tracks_check)):
            #if the track uncheked remove it from objs_handler[global list] 
            if tracks_check[track].checkState()==0:
                # objs_handler.pop(track)
                objs_handler[track]=0

    #function to set download button function disable checkboxes and get choices then go to worker thread and download
    def download_fun(self):
        self.download_frame.setEnabled(False)
        self.get_choices()
        
        self.download_thread()
    def download_thread(self):
        #init
        self.thread=QThread()
        self.worker=Worker(res=self.get_res(),location=self.get_location())
        self.worker.moveToThread(self.thread)
        #signals
        self.thread.started.connect(self.worker.run_download)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.download_progress.connect(self.update_progressbar)
        self.worker.downloaded_one.connect(self.reset_progressbar)
        #start thread
        self.thread.start()
        
        self.download_progress.show()
        self.thread.finished.connect(self.restet_after_download)
    #function to ubdate progress bar value each time there's value
    def update_progressbar(self,value):
        self.download_progress.setProperty("value",value)
    
    #to reset progress bar to zero after the download for the next video
    def reset_progressbar(self):
        self.download_progress.setProperty("value",0)

    #function to reset all program after download is finished
    #will be used with end_process_button [because it's the same function]
    def restet_after_download(self):
        self.remove_from_area()
        self.initialize()
        self.which_download.setEnabled(True)
        self.url_input.setEnabled(True)
        self.url_input.setText('')
        self.search_button.setEnabled(True)
        self.download_frame.setEnabled(True)

    #function to remove all tracks widgets from the scrollable area [from global tracks_check]
    #and also remove their objects from objs_handler[global list]
    def remove_from_area(self):
        global tracks_check
        global objs_handler
        for track in range(len(tracks_check)):
            tracks_check[track].deleteLater()
        tracks_check.clear()
        objs_handler.clear()

        # print(len(tracks_check))

    #now to return only url(entry)
    def get_url(self):
            return  self.url_input.text().strip()

    #function to know the user quality choice 
    def get_res(self):
        if self.res360_download.isChecked():
            return "360p"
        if self.res720_download.isChecked():
            return "720p"
        if self.audio_download.isChecked():
            return "160"
    
    #fucntion to know where the user want to save the files
    def get_location(self):
        fname=QFileDialog.getExistingDirectory(self,"choose folder","")
        if fname:
            return fname
        else:
            return f'{path.expanduser("~")}\Downloads\Video'
if __name__ == "__main__":
    
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())
    