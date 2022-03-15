from pytube import YouTube, Playlist, Search
class dn_youtube():
    def __init__(self,url):
        #to create youtube object so i can mange it
        self.yt_object=YouTube(url);
    #function to return basic information about the video as LIST[]
    def get_info(self):
        # 0 title ,1 length, 2 description 
        return [self.yt_object.title, self.yt_object.length,self.yt_object.description]
    def set_streams(self):
        return {"video":self.yt_object.streams.filter(progressive=True).asc(),
        "audio":self.yt_object.streams.filter(only_audio=True,adaptive=True).asc()}
    def get_streams(self):
        return self.streams
    def downlaod_stream(self,key):
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
    def get_info(self):
        temp=[self.pl_object.title]
        for v in self.pl_object.videos:
            temp.append([v.title, v.length, v.description])
        return temp
    #key and index to chose how to download the whole playlist
    def download_list(self,key):
        # .videos to create youtube objects
        for video in self.pl_object:
            dn_youtube(video).downlaod_stream(key)

class dn_search(dn_youtube):
    def __init__(self,search_key):
        #to get the first result as youtube object
        self.yt_object=Search(search_key).results[0]
    #get_indo and download_Stream from dn_youtube

obj=dn_search("your man joji")
print(obj.get_info()[0])
obj.downlaod_stream("160")
