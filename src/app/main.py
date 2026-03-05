from src.services.youtube_tool import get_youtube_data
from src.nodes.normalizer_node import normalize_data
from src.services.scoring_service import ScoringService

if __name__ == "__main__":
    data = get_youtube_data()
    normalized_data = normalize_data(data)
    print(normalized_data)

    scoring = ScoringService()

    comp_score = scoring.calc_competition_score(normalized_data)
    trend_score = scoring.calc_trend_score(normalized_data)
    opp_score = scoring.calc_opportunity_score(trend_score=trend_score, competition_score=comp_score)
    print(f"""
        Trend Score: {trend_score}
        Competition Score: {comp_score}
        Opportunity Score: {opp_score}
""")
    
    

