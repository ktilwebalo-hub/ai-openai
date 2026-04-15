import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

def get_response(prompt):
	
	response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}],
    temperature = 0
    
    )
	return response.choices[0].message.content



# Create a prompt detailing steps to plan the trip
prompt = """
I need to plan for my 2 week beach vacation.
step 1: Four potential locations.
step 2: Each location must have accommodation options, some activities.
steo 3: Evaluate pros and cons for each locations.
"""

response = get_response(prompt)
print(response)