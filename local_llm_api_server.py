from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the DistilGPT-2 model
generator = pipeline("text-generation", model="distilgpt2") # distilgpt2

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate text
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return jsonify({"response": result[0]["generated_text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)