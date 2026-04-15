import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_job_info",
            "description": "Extract job information from text",
            "parameters": {
                "type": "object",
                "properties": {
                    "job": {
                        "type": "string",
                        "description": "The job title mentioned in the text"
                    },
                    "location": {
                        "type": "string",
                        "description": "The office location mentioned in the text"
                    }
                },
                "required": ["job", "location"]
            }
        }
    }
]

# Input text
text = """
Our company is hiring a Machine Learning Engineer in London.
The role requires experience with Python and TensorFlow.
"""
client = OpenAI(api_key=api_key)

def get_reponse(text): 
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts structured data."},
        {"role": "user", "content": text}
    ],
    tools=tools,
    tool_choice="auto"
)

# Extract tool call result
    return response.choices[0].message.tool_calls[0].function.arguments


print(get_reponse(text))