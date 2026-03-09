from langgraph.graph import StateGraph, START, END
from src.graph.state import State
from src.nodes.youtube_node import youtube_node
from src.nodes.analyzer_node import analyzer_node
from src.nodes.niche_node import niche_node

workflow = StateGraph(State)

workflow.add_node("yt", youtube_node)
workflow.add_node("analyze", analyzer_node)
workflow.add_node("niche", niche_node)

workflow.add_edge(START, "yt")
workflow.add_edge("yt", "analyze")
workflow.add_edge("analyze", "niche")
workflow.add_edge("niche", END)

compiled_workflow = workflow.compile()
