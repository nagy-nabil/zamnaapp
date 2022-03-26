from pytube import YouTube, Playlist, Search
class dn_youtube():
    def __init__(self,url):
        #to create youtube object so i can mange it
        self.yt_object=YouTube(url);
    #function to return basic information about the video as LIST[]
    def get_info(self):
        # 0 title ,1 length, 2 description 
        #return list of lists to generlize dataset
        return [[self.yt_object.title, self.yt_object.length,self.yt_object.description]]
    def set_streams(self):
        return {"video":self.yt_object.streams.filter(progressive=True).asc(),
        "audio":self.yt_object.streams.filter(only_audio=True,adaptive=True).asc()}
    def get_streams(self):
        return self.streams
    #choose stream and download it
    def download_stream(self,key,check):
        if check[0]=='1':
            #download 720p video
            if key=="720p":
                self.yt_object.streams.filter(progressive=True,resolution="720p")[0].download()
            #download 480p video
            elif key=="360p":
                self.yt_object.streams.filter(progressive=True,resolution="360p")[0].download()
            # download audio with 160kbps
            else:
                self.yt_object.streams.filter(adaptive=True,only_audio=True,abr="160kbps")[0].download()


#you can get the list by playlist link or video link
#yt_obj is a list of dn_youtube links
class dn_playlist():
    def __init__(self, url):
        self.pl_object=Playlist(url);
    #return list of lists [playlist title, [video title , length , description]]
    def get_info(self):
        # temp=[self.pl_object.title]
        temp=[]
        for v in self.pl_object.videos: 
            temp.append([v.title, v.length, v.description])
        return temp
    #key and index to chose how to download the whole playlist
    def download_list(self,key):
        # .videos to create youtube objects
        # but we deal with links here and go to yt_download
        for video in self.pl_object:
            dn_youtube(video).download_stream(key)
    #key and index to chose how to download the whole playlist
    #overload function to take list to know which tracks user did choose
    def download_stream(self,key,check):
        # .videos to create youtube objects
        # but we deal with links here and go to yt_download
        for video in range(len(self.pl_object)):
            if check[video]=="1":
                dn_youtube(self.pl_object[video]).download_stream(key)
        print("done")
#search with keyword and transfer it to yt_object
class dn_search(dn_youtube):
    def __init__(self,search_key):
        #to get the first result as youtube object
        self.yt_object=Search(search_key).results[0]
    #get_info and download_stream from dn_youtube
