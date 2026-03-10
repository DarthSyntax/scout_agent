from typing import TypedDict, List
class State(TypedDict):
    query: str
    yt_data: List[dict]
    analyzed_data: dict
    niches: List[str]
    niche_results: List[dict]
    recommendation: dict