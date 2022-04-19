from youtubeOOP import dn_search
import requests
api_url="https://api.spotify.com/v1/"
CLIENT_ID = '50fb0ee5e03d43498b3ab59144557a44'
CLIENT_SECRET = '93f75a80e0154f88800653abedc3ab37'
#this path is mystery sorry
AUTH_URL = 'https://accounts.spotify.com/api/token'
access_token='BQC8QMEjYDeqyUv-nrFA3y8vOY6CAh2-uEAITloYptCe75zcMZXVkzqTwjG3N9k8LVbPd0TAwl_UedaFl82ElPWwk53tS4cQ'
class spotAPI():
    #for all requests
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    #take url for whatever the user want
    def __init__(self,url):
        #to work with if all over the code
        self.id=spotAPI.get_id(url)
        # self.get_access()
    
    #variable to keep track how many times api tried to get data and failed
    times=0
    def request_track(self):
        #edit url for the request instead of editing headers dict
        request=requests.request("GET",api_url+ 'tracks/' + self.id,headers=spotAPI.headers)
        # print(request.status_code)
        if request.status_code!=200 and self.times<2:
            self.times+=1
            self.get_access()
            self.request_track()
        if self.times==2:
            return None
        self.times=0
        data=request.json()
        # print(data['name'], data['artists'][0]['name'])
        #return info about the track song anme and the artist name
        #as list to generlize data shape
        return [data['name']+" "+ data['artists'][0]['name']]

    #get the artist name , album name , all songs name
    def request_album(self):
        #edit url for the request instead of editing headers dict
        request=requests.request("GET",api_url+ 'albums/' + self.id,headers=spotAPI.headers)
        # print(request.status_code)
        if request.status_code!=200 and self.times<2:
            self.times+=1
            self.get_access()
            self.request_album()
        self.times=0
        data=request.json()
        #0 artist name , 1 album name, then songs name
        artist_name=data['artists'][0]['name'],data['name']
        temp=[]
        for item in data["tracks"]['items']:
            temp.append(f'{item["name"]} {artist_name}')
        return temp  
    
    #get playlist tracks name
    #notice the API can respond with maximum 100 song at time, but you can set the start variable to get next patch of tracks
    def request_playlist(self,start=0):
        #edit url for the request instead of editing headers dict
        request=requests.request("GET",api_url+ 'playlists/' + self.id 
        + f'/tracks?offset={start}',headers=spotAPI.headers)
        print(request.status_code)
        if request.status_code!=200 and self.times<2:
            self.times+=1
            self.get_access()
            self.request_playlist()
        self.times=0
        data=request.json()
        temp=[]
        for item in data['items']:
            temp.append(f"{item['track']['artists'][0]['name']} {item['track']['name']}")
        return temp

    #function to get the data returned by the api to youtube functions 
    #return list of search objects as general rule for track album playlist
    #key instead of make more than function ['t' ->track, 'a' -> album, 'p' -> playlist]
    def spot_to_youtube(self,key='t'):
        search_list=[]
        if key=='p':
            temp=self.request_playlist()
        elif key=='a':
            temp=self.request_album()
        else:
            temp=self.request_track()
        for track in temp: 
            obj=dn_search(track)
            search_list.append(obj)
        return search_list
    #NOT WORKING YET
    def request_saved(self):
        #edit url for the request instead of editing headers dict
        request=requests.request("GET",api_url+ '/users/epor0v8szttz3646ooin6738y',headers=spotAPI.headers)
        print(request.status_code)
        data=request.json()
        temp=[]
        for item in data['items']:
            temp.append(f"{item['track']['artists'][0]['name']} {item['track']['name']}")
        return temp
    @staticmethod
    #to get the key for spotify data base, will use it just once, NOOOO WRONG WE NEED TO USE IT EVERY TIME I SUPPOSE
    def get_access():
        # POST
        auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope':'user-library-read'
    })
        # convert the response to JSON
        auth_response_data = auth_response.json()
        # save the access token
        global access_token
        access_token = auth_response_data['access_token']
        # print(auth_response.status_code)
        # print(access_token)


    @staticmethod
    #to extract song or playlist id from the link
    def get_id(url):
        return url.split('/')[4].split("?")[0]

if __name__ == "__main__":
    print(access_token)
    # spotAPI.get_access()
    # print(access_token)
    obj=spotAPI("https://open.spotify.com/track/00NAQYOP4AmWR549nnYJZu?si=8ff074290d1f4c13")
    data=obj.request_track()
    print(data)
    # obj2=spotAPI("https://open.spotify.com/album/0gA0nZrZ55PLUp7ARfrICu?si=xIDc51q4SNSdDPLnyBO_Ag")
    # data2=obj2.request_album()
    # print(data)
    # print(data['items'][0]['track']['name'])
    # print(data['items'][0]['track']['artists'][0]['name'])
    # # for v, k in enumerate(data['items'][0]['track']['artists'],0):
    # #     print(f"{v} {k}")
    # # print(len(data)+"\n"+str(data))

    # # spotAPI.get_access()
    # print(len(data2))
    # for item in data:
    #     print(item)
    #     temp=dn_search(item)
    #     temp.downlaod_stream("160")