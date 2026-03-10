from langgraph.graph import StateGraph, START, END
from src.graph.state import State
from src.nodes.youtube_node import youtube_node
from src.nodes.analyzer_node import analyzer_node
from src.nodes.niche_node import niche_node
from src.nodes.recommend_node import recommend_niche_node, recommend_topic_node
from src.nodes.router_node import router_node
from src.nodes.generate_node import generate_response

workflow = StateGraph(State)

workflow.add_node("yt", youtube_node)
workflow.add_node("analyze", analyzer_node)
workflow.add_node("niche", niche_node)
workflow.add_node("recommend_topic", recommend_topic_node)
workflow.add_node("recommend_niche", recommend_niche_node)
workflow.add_node("generate", generate_response)

workflow.add_edge(START, "yt")
workflow.add_edge("yt", "analyze")
workflow.add_conditional_edges("analyze", router_node, {
    "CREATE_CONTENT": "recommend_topic",
    "FIND_NICHES": "niche"
})
workflow.add_edge("niche", "recommend_niche")
workflow.add_edge("recommend_topic", "generate")
workflow.add_edge("recommend_niche", "generate")
workflow.add_edge("generate", END)
workflow.add_edge("generate", END)

compiled_workflow = workflow.compile()
