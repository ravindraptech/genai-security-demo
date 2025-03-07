import requests
import argparse
import json

url = "http://localhost:5000/generate"
#payload = {"user_prompt": "Tell me an interesting fact about Pizza"}


# Create CLI.
parser = argparse.ArgumentParser()
parser.add_argument("user_prompt", type=str, help="The user prompt.")
args = parser.parse_args()
user_prompt = args.user_prompt
user_prompt = f"\"user_prompt\":\"{user_prompt}\""
user_prompt_txt = '{' + user_prompt + '}'
payload = json.loads(user_prompt_txt)

response = requests.post(url, json=payload)
print(response.json())
