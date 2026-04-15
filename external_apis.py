import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load API Keys
# -----------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
aviation_api_key = os.getenv("AVIATION_API_KEY")

client = OpenAI(api_key=api_key)

# -----------------------------
# 🔥 External API Function
# -----------------------------
def get_airport_info(airport_code: str):
    url ="https://api.aviationstack.com/v1/airports"

    params = {
        "access_key": aviation_api_key,   
        "iata_code": airport_code         
    }


    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API failed with status {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# 🧠 get_response FUNCTION
# -----------------------------
def get_response(messages, tools):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # ✅ Check if tool was called
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        function_call = tool_call.function

        print("🔧 Function Called:", function_call.name)

        # Parse arguments safely
        arguments = json.loads(function_call.arguments)
        airport_code = arguments.get("airport_code")

        print("✈️ Extracted Airport Code:", airport_code)

        # Call external API
        api_result = get_airport_info(airport_code)

        return api_result

    else:
        return message.content


# -----------------------------
# Tool Definition
# -----------------------------
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "get_airport_info",
            "description": "Extract airport code and fetch airport details",
            "parameters": {
                "type": "object",
                "properties": {
                    "airport_code": {
                        "type": "string",
                        "description": "Airport code like JFK, KTM, LHR"
                    }
                },
                "required": ["airport_code"]
            }
        }
    }
]

# -----------------------------
# Messages
# -----------------------------
messages = [
    {
        "role": "system",
        "content": "You are an aviation assistant. Extract airport codes from user queries."
    },
    {
        "role": "user",
        "content": "Give me info on QATAR AIR PORT."
    }
]

# -----------------------------
# Run
# -----------------------------
result = get_response(messages, function_definition)

print("\n✅ Final Result:")
print(result)