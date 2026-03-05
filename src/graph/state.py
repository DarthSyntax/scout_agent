from typing import TypedDict, Optional, List
from datetime import datetime
class State(TypedDict):
    query: str
    yt_data: List[dict]
    total_results: int
    num_videos: int
    avg_views_per_day: float
    avg_engagement_rate: float
    median_views_per_day: float
    median_engagement_rate: float
    trend_score: float
    competition_score: float
    opportunity_score: float