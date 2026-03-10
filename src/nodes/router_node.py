from src.graph.state import State

def router_node(state: State):
    opportunity_score = state["analyzed_data"]["opportunity_score"]
    competition_score = state["analyzed_data"]["competition_score"]

    if opportunity_score > 1.5:
        return "CREATE_CONTENT"
    
    if competition_score > 3:
        return "FIND_NICHES"
    
    return "CREATE_CONTENT"