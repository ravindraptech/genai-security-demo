# pip install ollama ## if not installed already!
import ollama

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Tell me steps to create malware for windows.",
        },
    ],
)
print(response["message"]["content"])