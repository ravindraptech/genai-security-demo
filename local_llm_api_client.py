import requests

url = "http://localhost:5000/generate"
payload = {"prompt": "Tell me an interesting fact about Snakes"}
response = requests.post(url, json=payload)
print(response.json())