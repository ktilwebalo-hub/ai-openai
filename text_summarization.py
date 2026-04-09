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

# prompt="""Replace car with plane and adjust phrase:
# A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

finance_text = """
Finance is the study of managing money, focusing on how individuals, companies, and governments acquire, spend, and invest funds. Key areas include corporate finance, investment management, and personal finance, focusing on assets, liabilities, and risk. Core concepts include net present value (NPV), cash flow analysis, and capital structure. 
Here is a breakdown of key finance concepts and terminology:
Financial Statements: Essential reports including the income statement, balance sheet, and cash flow statement, which track a company's financial health.
Assets and Liabilities: Assets are resources with economic value (e.g., cash, property), while liabilities are obligations, such as loans and debts.
Investment Basics: The allocation of money with expectations of profit, involving stocks, bonds, or real assets.
Core Principles: Successful financial management relies on budgeting, saving, understanding credit, and managing risk.
Key Financial Metrics:
Return on Investment (ROI): A measure used to evaluate the efficiency of an investment.
Net Present Value (NPV): A method to determine the value of an investment by calculating the present value of future cash flows.
Equity: The value of shares issued by a company or the value of an asset after deducting liabilities. 
For foundational knowledge, texts like Benjamin Graham's "The Intelligent Investor" emphasize value-oriented investing, while Morgan Housel's "The Psychology of Money" focuses on the emotional aspects of wealth management. 
"""

prompt =  f"""Summarize the following text into three concise bullet points:
{finance_text}"""

# chat.completion end point
max_completion_tokens = 100
response = client.chat.completions.create(model='gpt-4o-mini', max_completion_tokens=max_completion_tokens, messages=[{"role":"user", "content":prompt}])

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# print(response)

# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")
