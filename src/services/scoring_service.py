import math

class ScoringService:

    def calc_trend_score(_self, normalized_data):
        view_score = _self._score_view_count(normalized_data["avg_views_per_day"])
        engagement_score = _self._score_engagement_rate(normalized_data["avg_engagement_rate"])
        
        return round( math.log10(view_score + 1) * 0.7 +
            (engagement_score * 10) * 0.3, 2)

    def calc_competition_score(_self, normalized_data):
        # total results is not a good metric for youtube because searches for niches have nearly the same result
        # maybe make it median subscribers?
        results_score = _self._score_median_subscribers(normalized_data["median_channel_subscribers"])

        return round(results_score, 2)
    
    def calc_opportunity_score(_self, trend_score, competition_score):

        return round(trend_score / competition_score, 2)
    
    def _score_view_count(self, avg_views_per_day):
        if avg_views_per_day >= 5000000:
            return 10
        elif avg_views_per_day >= 1000000:
            return 8
        elif avg_views_per_day >= 500000:
            return 6
        elif avg_views_per_day >= 100000:
            return 4
        elif avg_views_per_day >= 50000:
            return 2
        else:
            return 1
        
            
    

    def _score_engagement_rate(self, avg_engagement_rate):
        if avg_engagement_rate > 0.08:
            return 10
        elif avg_engagement_rate > 0.06:
            return 8
        elif avg_engagement_rate > 0.04:
            return 6
        elif avg_engagement_rate > 0.03:
            return 4
        elif avg_engagement_rate > 0.02:
            return 2
        else:
            return 1
        
    def _score_total_results(self, total_results):
        if total_results > 500000:
            return 10
        elif total_results > 200000:
            return 8
        elif total_results > 50000:
            return 6
        elif total_results > 10000:
            return 4
        else:
            return 1
        
    def _score_median_subscribers(self, median_subscribers):
        if median_subscribers > 1000000:
            return 10
        elif median_subscribers > 500000:
            return 8
        elif median_subscribers > 100000:
            return 6
        elif median_subscribers > 50000:
            return 4
        elif median_subscribers > 10000:
            return 2
        else:
            return 1

