from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import json
from dotenv import load_dotenv
import os

load_dotenv()

now_utc = datetime.now(timezone.utc)
one_week_ago = now_utc - timedelta(weeks=1)
formatted_date = one_week_ago.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'


API_KEY = os.getenv("YT_API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_youtube_data(topic="asmr"):
    video_response = youtube.search().list(
        part='snippet',
        type="video",
        regionCode='US',
        maxResults=25,
        q=topic,
        order='viewCount',
        publishedAfter=formatted_date
    ).execute()
    

    with open(r'C:\Users\stael\Projects\scout_agent\data\example_output.json', 'w') as file:
            json.dump(video_response, file, indent=1)

    video_ids = [item["id"]["videoId"] for item in video_response["items"]]


    list_response = youtube.videos().list(
         part="snippet,statistics",
         id=','.join(video_ids)
    ).execute()

    with open(r'C:\Users\stael\Projects\scout_agent\data\id_output.json', 'w') as file:
            json.dump(list_response, file, indent=1)
    

    videos = []
    for video in list_response["items"]:
          date_published = datetime.fromisoformat(video["snippet"]["publishedAt"])
          days_since_upload = (now_utc - date_published).days
          videos.append({
                "id": video["id"],
                "channel_title": video["snippet"]["channelTitle"],
                "title": video["snippet"]["title"],
                "published_at": video["snippet"]["publishedAt"],
                "view_count": video["statistics"].get("viewCount", "0"),
                "days_since_upload": days_since_upload,
                "like_count": video["statistics"].get("likeCount", "0"),
                "comment_count": video["statistics"].get("commentCount", "0"),
                "total_results": video_response["pageInfo"]["totalResults"]         

          })

    return videos        
        
            

