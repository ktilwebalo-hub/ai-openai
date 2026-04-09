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


response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user",
  		     "content": "The product quality exceeded my expectations"},
              {"role": "assistant",
  		     "content": "1"},
              {"role": "user",
  		     "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant",
  		     "content": "-1"}, 
              # Provide the text for the model to classify
              {"role": "user",
  		     "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)