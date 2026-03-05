from src.graph.state import State
from src.services.youtube_tool import get_youtube_data

def youtube_node(state: State): 
    query = state["query"]
    data = get_youtube_data(query)

    return {"yt_data": data}