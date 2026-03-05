from pytrends.request import TrendReq

async def get_google_trends(topic="asmr"):
    request = TrendReq(hl='en-US', tz=300)
    request.build_payload(
        [topic],
        timeframe='today 7-d'
    )
    results = await request.interest_over_time()

    print(results.head())
    return results