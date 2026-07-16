from openai import OpenAI
import json

# Replace with your OpenAI API key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

feedback = """
I ordered a laptop two weeks ago but still haven't received it.
Please help immediately.
"""

prompt = f"""
Analyze the customer feedback and return ONLY valid JSON in this format:

{{
  "sentiment": "",
  "urgency": "",
  "issue": ""
}}

Feedback:
{feedback}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a customer feedback analyzer. Return only JSON."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = response.choices[0].message.content

print("Analysis Result:")
print(result)
