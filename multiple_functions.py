import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

message_listing = """
   I recently bought this smartphone and i really like it. The battery life is great and the camera is amazing. However, the phone feels a bit heavy.
"""

# Preloaded function definition
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract sentiment and key features",
            "parameters": {
                "type": "object",
                "properties": {
                    "sentiment": {
                        "type": "string",
                        "description": "overall sentiment of the review"
                    },
                    "features": {
                        "type": "array",
                        "items": {"types":"string"}
                    }
                },
                "required": ["sentiment", "features"]
            }
        }
    }
]

function_definition.append({'type': 'function', 'function':{'name': 'reply_to_review', 'description': 'Reply politely to the customer who wrote the review', 'parameters': {'type': 'object', 'properties': {'reply': {'type': 'string','description': 'Reply to post in response to the review'}}}, "required":["reply"]}})

client = OpenAI(api_key=api_key)

def get_reponse(message, function): 
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts structured data. and reply to the review"},
        {"role": "user", "content": message}
    ],
    tools=function,
    tool_choice="auto"
)

# Extract tool call 
    return response.choices[0].message.tool_calls

response = get_reponse(message_listing, function_definition)

print(response[0].function.arguments)
print(response[1].function.arguments)