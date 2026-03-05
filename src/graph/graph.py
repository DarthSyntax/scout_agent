from langgraph import StateGraph, START, END
from src.graph.state import State
from src.nodes.youtube_node import youtube_node
from src.nodes.normalizer_node import normalize_data


workflow = StateGraph(State)

workflow.add_node("yt", youtube_node)
workflow.add_node("norm", normalize_data)


workflow.add_edge(START, 'yt')
workflow.add_edge('yt', "norm")
workflow.add_edge("norm")

workflow.compile()
