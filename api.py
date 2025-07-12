from googleapiclient.discovery import build
import os
# from flask import Flask, session, redirect, url_for,request, jsonify
import json
from requests import post, get
from dotenv import load_dotenv
load_dotenv()
import base64
import urllib
import datetime


  

api_Key = os.getenv("YT_API_KEY")

youtube = build('youtube', 'v3',developerKey=api_Key)


request = youtube.search().list(
    q = 'nahi milta',
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



# spotify_client_id =os.getenv("CLIENT_ID")
# spotify_client_secret = os.getenv("CLIENT_SECRET")


    
youtube.close()
