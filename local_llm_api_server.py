from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the DistilGPT-2 model
generator = pipeline("text-generation", model="distilgpt2") # distilgpt2

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    print(f"Received request: {data}")
    user_prompt = data.get("user_prompt", "")
    if not user_prompt:
        return jsonify({"error": "No user_prompt provided"}), 400

    # validate input
    harmful_tokens = ['virus', 'hack', 'hate']
    if any(x in user_prompt for x in harmful_tokens):
        return jsonify({"error": "The model does not support generation of response which is harmful or insecure!"}), 403

    # Generate text with context (RAG)
    context = 'The name of the father of king Foobar was Daddybar. '
    user_prompt = context +  user_prompt

    # Generate text
    result = generator(user_prompt, num_return_sequences=1)
    print(f"result: {result[0]["generated_text"]}")
    return jsonify({"response": result[0]["generated_text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)