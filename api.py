from googleapiclient.discovery import build
import os
import json
from requests import post, get
from dotenv import load_dotenv
load_dotenv()


  
# set up and .enc file and save your youtube API key in it and access it using dotenv method
# You will need to create an YT api key in order to make API calls.
api_Key = os.getenv("YT_API_KEY")
# build method of the youtube API
youtube = build('youtube', 'v3',developerKey=api_Key)


request = youtube.search().list(
    q = 'Jigle bells', # add your song name or the content you need to search result for
    part = 'snippet',
    type = 'video',
    maxResults = 5,
    videoDefinition = 'standard'


)

video_list = []
response = request.execute()

for dict_obj in response['items']:
    video_id = dict_obj['id']['videoId']
    video_duration = "short"
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_title = dict_obj['snippet']['title']


    video_list.append((video_title,video_url))

for item in video_list:
    print(item[0])
    print(item[1],'\n')

#-----------------------------------------------------------------------------------------

    
youtube.close()
