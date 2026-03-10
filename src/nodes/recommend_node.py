from src.graph.state import State

def recommend_niche_node(state: State):
    # already sorted by opportunity score
    best_niche = state["niche_results"][0]
    print(best_niche)
    return {"recommendation": best_niche}

def recommend_topic_node(state: State):
    topic_recommended = state["analyzed_data"]
    print(topic_recommended)
    return {"recommendation": topic_recommended}