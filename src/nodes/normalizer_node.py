import statistics

def normalize_data(videos: list):
    engagement_rates_list = []
    views_per_day_list = []
    subscribers_list = []
    channel_set = set()

    total_results = 0 
    num_videos = 0 
    median_views_per_day = 0
    avg_views_per_day = 0
    median_engagement_rate = 0
    avg_engagement_rate = 0
    median_channel_subscribers = 0
    creator_saturation = 0

    for video in videos:
        views = int(video["view_count"])
        likes = int(video["like_count"])
        comments = int(video["comment_count"])
        days = video["days_since_upload"]
        channel = video["channel_title"]

        if channel not in channel_set:
            channel_set.add(channel)
            subscribers_list.append(int(video["channel_subscribers"]))

        if days > 0:
            views_per_day = (views/days)
        else:
            views_per_day = views

        if views > 0:
            engagement = ((likes+comments)/views)
        else: 
            engagement = 0
         

        engagement_rates_list.append(engagement)
        views_per_day_list.append(views_per_day)
    
    
    if videos:

        total_results = videos[0]["total_results"]
        num_videos = len(videos)
        median_views_per_day = statistics.median(views_per_day_list)
        avg_views_per_day = statistics.mean(views_per_day_list)
        median_engagement_rate = statistics.median(engagement_rates_list)
        avg_engagement_rate = statistics.mean(engagement_rates_list)
        median_channel_subscribers = statistics.median(subscribers_list)
        creator_saturation = statistics.median(subscribers_list)/statistics.mean(views_per_day_list)

    return {
        "total_results": total_results,
        "median_views_per_day": median_views_per_day,
        "avg_views_per_day": avg_views_per_day,
        "median_engagement_rate": median_engagement_rate,
        "avg_engagement_rate": avg_engagement_rate,
        "median_channel_subscribers": median_channel_subscribers,
        "creator_saturation": creator_saturation,
    }
