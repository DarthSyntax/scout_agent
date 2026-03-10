from src.graph.state import State
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_response(state: State):
    client = OpenAI(api_key=api_key)
    context = state["recommendation"]
    prompt = f'''You are a helpful chatbot who is to help aspiring content creators on Youtube pick video ideas
            in order to grow their channels. If the user message starts with niche, then the chosen topic by the user was too competitive 
            and a niche was chosen within that topic. If user message starts with query, then that is the topic that was originally searched for.

            Using the data provided, write a short analysis explaining:
            1. Why this topic is attractive or unattractive
            2. What the metrics suggest about demand
            3. What the metrics suggest about competition
            4. Whether a creator should target this niche
            Only use the data provided in the context. Do not invent additional reasons.

            Meanings behind some of the data:
            Engagement rate is a ratio of average views per day divided by the number of likes + comments.
            Creator saturation is based on median_subscribers divided by average views per day.
            total_results is the number of videos returned when the topic is searched through the Youtube API.
            num_videos_analyzed is the number of videos with the highest views returned by the API that were posted in the last 7 days,
            the data is based on these most viewed videos
            
            Context: {json.dumps(context)}'''
    result = list(context.keys())[0]
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"{result}: {context[result]}"}
        ]
    )

    print(response.choices[0].message.content)