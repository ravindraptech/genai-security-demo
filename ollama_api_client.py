# pip install ollama ## if not installed already!
import ollama

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Write a poem about a sunny day in 50 words.",
        },
    ],
)
print(response["message"]["content"])