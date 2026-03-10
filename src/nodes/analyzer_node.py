from src.graph.state import State
from src.nodes.normalizer_node import normalize_data
from src.services.scoring_service import ScoringService

def analyzer_node(state: State):
    print("Analyzing Query")
    yt_data = state["yt_data"]
    scoring_service = ScoringService()
    normalized_data = normalize_data(yt_data)

    trend_score = scoring_service.calc_trend_score(normalized_data)
    competition_score = scoring_service.calc_competition_score(normalized_data)
    opportunity_score = scoring_service.calc_opportunity_score(trend_score, competition_score)

    scored_data = {
        "trend_score": trend_score,
        "competition_score": competition_score,
        "opportunity_score": opportunity_score,
    }

    analyzed_data = {"query": state["query"]} | normalized_data | scored_data
    return {
        "analyzed_data": analyzed_data
    }
