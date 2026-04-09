import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Create a detailed prompt
prompt = """
I need a product description for SonicPro headphones, wireless headphone with 40 hour of battery life. Active noise cancellation (ANC), foldable design
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    temperature=2
)

print(response.choices[0].message.content)