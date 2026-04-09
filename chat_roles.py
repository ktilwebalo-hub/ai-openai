import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Create OpenAI client
client = OpenAI(api_key=api_key)



sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to python."}
  ]
)

print(response.choices[0].message.content)