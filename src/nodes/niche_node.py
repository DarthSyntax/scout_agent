from src.graph.state import State
from src.services.niche_service import NicheService
from src.services.youtube_tool import get_youtube_data
from src.nodes.normalizer_node import normalize_data

def niche_node(state: State):
    query = state["query"]

    niche_service = NicheService()
    niches = niche_service.find_niches(query)
    niche_results = niche_service.evaluate_niches(query=query, youtube_tool=get_youtube_data, normalizer=normalize_data)

    print(niche_results)
    return {
        "niches": niches,
        "niche_results": niche_results
    }