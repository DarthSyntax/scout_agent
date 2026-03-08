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

def get_youtube_data(topic="asmr", max_results = 25):
    video_response = youtube.search().list(
        part='snippet',
        type="video",
        regionCode='US',
        maxResults=25,
        q=topic,
        order='viewCount',
        publishedAfter=formatted_date
    ).execute()
    
    video_ids = [item["id"]["videoId"] for item in video_response["items"]]
    channel_ids = [item["snippet"]["channelId"] for item in video_response["items"]]

    channel_response = youtube.channels().list(
         part="snippet,contentDetails,statistics",
         id=','.join(channel_ids)

    ).execute()
    
    channels_dict = {}
    for item in channel_response.get("items", []):
         c_id = item["id"]
         channels_dict.update({
              c_id : {
                  "channel_id": item["id"],
                  "channel_title": item["snippet"]["title"],
                  "channel_subscribers": item["statistics"].get("subscriberCount", "0"),
                  "channel_total_views": item["statistics"].get("viewCount", "0"),
                  "channel_total_videos": item["statistics"].get("videoCount", "0"),
                  }
            })
    


    list_response = youtube.videos().list(
         part="snippet,statistics",
         id=','.join(video_ids)
    ).execute()
    
    videos = []
    for video in list_response["items"]:
          date_published = datetime.fromisoformat(video["snippet"]["publishedAt"])
          days_since_upload = (now_utc - date_published).days
          channel_id = video["snippet"]["channelId"]
          current_channel = channels_dict[channel_id]
          
          videos.append({
                "id": video["id"],
                "channel_id": channel_id,
                "channel_title": video["snippet"]["channelTitle"],
                "title": video["snippet"]["title"],
                "published_at": video["snippet"]["publishedAt"],
                "view_count": video["statistics"].get("viewCount", "0"),
                "days_since_upload": days_since_upload,
                "like_count": video["statistics"].get("likeCount", "0"),
                "comment_count": video["statistics"].get("commentCount", "0"),
                "channel_subscribers": current_channel["channel_subscribers"],
                "channel_total_views": current_channel["channel_total_views"],
                "channel_total_videos": current_channel["channel_total_videos"],
                "total_results": video_response["pageInfo"]["totalResults"]         
            })
          # print({video["snippet"]["channelTitle"] : current_channel["channel_subscribers"]})
    
            
    return videos     
        
            

