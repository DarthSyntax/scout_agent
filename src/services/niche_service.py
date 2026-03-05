from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class NicheService:

    def find_niches(self, query: str):
        client = OpenAI(api_key=api_key)

        sys_message = '''You are a helpful chatbot who is to give suggestions for niche subtopics about a 
            given word or phrase. The point is to help aspiring content creators on Youtube pick video ideas
            in order to grow their channels. You are getting this job because the chosen topic by the user was too competitive 
            and we want to give them a niche within that topic. Give just the suggestions with only a comma in between each one. '''
        
        assist_one_shot = """AI Agents in business,AI Agents for small businesses,AI Agents without coding,AI Agents for creators,AI Agents in marketing"""
        

        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": sys_message},
                {"role": "user", "content": "Give me 5 niche topic suggestions for AI Agents"},
                {"role": "assistant", "content": assist_one_shot},
                {"role": "user", "content": f"Give me 3 niche topic suggestions for {query}"},
                {"role": "assistant", "content": ''}
            ]
        )
        list_results = (response.choices[0].message.content).split(',')
        # print(list_results)
        return list_results
        

    def evaluate_niches(self, query, youtube_tool, normalizer):
        # gets the niches stats from youtube and normalizes them to later compare the opportunity score
        niches = self.find_niches(query)

        results = []

        for niche in niches:
            videos = youtube_tool.get_youtube_data(query)
            normalized = normalizer.normalize_data(query)
