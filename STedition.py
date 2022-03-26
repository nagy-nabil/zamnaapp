# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firedition.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from youtubeOOP import dn_playlist, dn_search,dn_youtube
from PyQt5 import QtCore, QtGui, QtWidgets
from spotify import spotAPI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(548, 767)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(548, 767))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 120, 451, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(15, 15, 15, 15)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.url_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.url_input.sizePolicy().hasHeightForWidth())
        self.url_input.setSizePolicy(sizePolicy)
        self.url_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.url_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.url_input.setInputMask("")
        self.url_input.setText("")
        self.url_input.setMaxLength(22669)
        self.url_input.setFrame(True)
        self.url_input.setCursorPosition(0)
        self.url_input.setObjectName("url_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.url_input)
        self.search_button = QtWidgets.QPushButton(self.formLayoutWidget,clicked=lambda:self.search_fun())
        self.search_button.setObjectName("search_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.search_button)
        self.output_area = QtWidgets.QScrollArea(self.centralwidget)
        self.output_area.setGeometry(QtCore.QRect(30, 260, 471, 441))
        self.output_area.setMinimumSize(QtCore.QSize(0, 50))
        self.output_area.setFrameShape(QtWidgets.QFrame.VLine)
        self.output_area.setWidgetResizable(True)
        self.output_area.setObjectName("output_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 467, 437))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_all = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.check_all.setEnabled(False)
        self.check_all.setMinimumSize(QtCore.QSize(0, 25))
        self.check_all.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.check_all.setChecked(True)
        self.check_all.setTristate(False)
        self.check_all.setObjectName("check_all")
        self.verticalLayout.addWidget(self.check_all)
        #to excuate function when state of checkbutton change
        self.check_all.stateChanged.connect(lambda:self.check_all_fun())
        self.check_all.hide()
        # self.pick_song = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        
        # self.verticalLayout.addWidget(self.pick_song)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.audio_download = QtWidgets.QRadioButton(self.frame)
        self.audio_download.setMinimumSize(QtCore.QSize(0, 20))
        self.audio_download.setChecked(True)
        self.audio_download.setObjectName("audio_download")
        self.gridLayout.addWidget(self.audio_download, 1, 2, 1, 1)
        self.res720_download = QtWidgets.QRadioButton(self.frame)
        self.res720_download.setMinimumSize(QtCore.QSize(0, 20))
        self.res720_download.setChecked(False)
        self.res720_download.setObjectName("res720_download")
        self.gridLayout.addWidget(self.res720_download, 1, 1, 1, 1)
        self.res48_downlaod = QtWidgets.QRadioButton(self.frame)
        self.res48_downlaod.setMinimumSize(QtCore.QSize(0, 20))
        self.res48_downlaod.setObjectName("res48_downlaod")
        self.gridLayout.addWidget(self.res48_downlaod, 1, 0, 1, 1)
        self.download_button = QtWidgets.QPushButton(self.frame,clicked=lambda:self.deownload_fun())
        self.download_button.setMinimumSize(QtCore.QSize(80, 40))
        self.download_button.setSizeIncrement(QtCore.QSize(57, 0))
        self.download_button.setBaseSize(QtCore.QSize(91, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.download_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.download_button.setFont(font)
        self.download_button.setIconSize(QtCore.QSize(50, 30))
        self.download_button.setShortcut("")
        self.download_button.setCheckable(True)
        self.download_button.setAutoDefault(True)
        self.download_button.setDefault(False)
        self.download_button.setFlat(False)
        self.download_button.setObjectName("download_button")
        self.gridLayout.addWidget(self.download_button, 2, 1, 1, 1)
        
        self.frame.hide()
        self.output_area.setWidget(self.scrollAreaWidgetContents)
        self.which_download = QtWidgets.QComboBox(self.centralwidget)
        self.which_download.setGeometry(QtCore.QRect(40, 40, 451, 31))
        self.which_download.setFrame(True)
        self.which_download.setObjectName("which_download")
        self.which_download.addItem("")
        self.which_download.addItem("")
        self.which_download.addItem("")
        self.which_download.addItem("")
        self.which_download.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.which_download.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.which_download, self.url_input)
        MainWindow.setTabOrder(self.url_input, self.search_button)
        MainWindow.setTabOrder(self.search_button, self.output_area)
        MainWindow.setTabOrder(self.output_area, self.check_all)
        # MainWindow.setTabOrder(self.check_all, self.pick_song)
        # MainWindow.setTabOrder(self.pick_song, self.res48_downlaod)
        MainWindow.setTabOrder(self.res48_downlaod, self.res720_download)
        MainWindow.setTabOrder(self.res720_download, self.audio_download)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "zamnapp"))
        self.url_input.setPlaceholderText(_translate("MainWindow", "please enter url"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.check_all.setText(_translate("MainWindow", "Check All"))
        # self.pick_song.setText(_translate("MainWindow", "SONG NAME"))
        self.audio_download.setText(_translate("MainWindow", "160kpbs"))
        self.res720_download.setText(_translate("MainWindow", "720p"))
        self.res48_downlaod.setText(_translate("MainWindow", "480p"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.which_download.setCurrentText(_translate("MainWindow", "YouTube Track"))
        self.which_download.setItemText(0, _translate("MainWindow", "YouTube Track", "0"))
        self.which_download.setItemText(1, _translate("MainWindow", "YouTube Playlist", "1"))
        self.which_download.setItemText(2, _translate("MainWindow", "YouTube search", "2"))
        self.which_download.setItemText(3, _translate("MainWindow", "Spotify Track", "3"))
        self.which_download.setItemText(4, _translate("MainWindow", "Spotify Playlist", "4"))
    #know what user want to do and get the input
    #now to return only url(entry)
    def get_url(self):
            return  self.url_input.text().strip()
    #get user choicses       
    tracks_check=[]
    #to create gui for the results [each track as check box as general rule to give the user apility to choose songs from playlists]
    def download_gui_check(self):
        tracks_info=obj.get_info()
        # del tracks[0] #for now for gui purposes
        for item in tracks_info:
            self.pick_song = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.pick_song.setMinimumSize(QtCore.QSize(0, 25))
            self.pick_song.setChecked(True)
            self.pick_song.setAutoRepeat(False)
            self.pick_song.setTristate(False)
            self.pick_song.setObjectName("pick_song")
            self.pick_song.setText(f"{item[0]}") #titles
            self.tracks_check.append(self.pick_song)#to know user choices
            self.verticalLayout.addWidget(self.pick_song)
        #edit widgets
        self.check_all.setEnabled(True)
        self.verticalLayout.addWidget(self.frame)
        # self.frame.setEnabled(True)
        self.frame.show()

    #fun to set basic oberation of search function which object to create and so on
    def search_fun(self):
        self.search_button.setEnabled(False)
        self.url_input.setEnabled(False)
        self.which_download.setEnabled(False)
        #to get url and use it for the object
        url=self.get_url()
        global obj
        global objs_list
        if self.which_download.currentIndex()==0:
            obj=dn_youtube(url)
        elif self.which_download.currentIndex()==1:
            obj=dn_playlist(url)
        elif self.which_download.currentIndex()==2:
            obj=dn_search(url)
        elif self.which_download.currentIndex()==3:
            objs_list=spotAPI(url)
            objs_list=obj.spot_to_youtube()#list of objs
        self.download_gui_check()
        self.check_all.show()

    #set check all function to select or diselect all tracks at once
    def check_all_fun(self):
        if self.check_all.checkState()==0:
            for item in self.tracks_check:
                item.setChecked(False)
        if self.check_all.checkState()==2:
            for item in self.tracks_check:
                item.setChecked(True)  



    #to change check_all state if we change any other check box
    #not used yot///////////////////////////////***************************************************************************************
    def change_check_all_state(self):
        self.check_all.setChecked(False)



    #download function
    def deownload_fun(self):
        self.frame.hide()#remove the ability from the user to click download again
        #edit self.tracks_check as "0" and "1" (take user input) to send it to download function and download what and through what
        chektemp=[]
        for track in range(len(self.tracks_check)):
            # print(self.tracks_check[track].checkState())
            if self.tracks_check[track].checkState()==2:
                chektemp.append('1')
            else:
                chektemp.append('0')
        print(chektemp)
        #DONT FORGET GET THE KEY
        obj.download_stream('160',chektemp)
        del chektemp
        #edit widegts
        self.remove_from_area()
        self.enable_widgets()


    #function to remove all tracks widgets from the scrollable area
    def remove_from_area(self):
        for track in range(len(self.tracks_check)):
            self.tracks_check[track].deleteLater()
        self.tracks_check.clear()
        print(len(self.tracks_check))
    
    #return all widgets to work again[default before search]
    def enable_widgets(self):
        self.which_download.setEnabled(True)
        self.url_input.setEnabled(True)
        self.url_input.setText('')
        self.search_button.setEnabled(True)
        self.check_all.setChecked(True)
        self.check_all.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())