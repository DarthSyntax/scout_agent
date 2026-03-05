
class DecisionService: 

    def recommend(_self, trend_score, competition_score, opportunity_score):
        if opportunity_score > 7:
            return "CREATE_CONTENT"
        
        if competition_score >=8:
            # not great opportunity but high competition as well so find a niche where less
            #competition and more opportunity
            return "FIND_NICHE"

        if trend_score < 4:
            return "RETRY" 
        
        return "AVOID_TOPIC"