# genai-security-demo
Generative AI Security Demo

1. **Set Up a Virtual Environment**
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/macOS
     venv\Scripts\activate     # Windows
     ```

2. **Install Dependencies**
   - Install required Python packages:
     ```bash
     pip install torch transformers flask requests
     ```
   - Note: `torch` (PyTorch) is needed for the model. If GPU is available, install the GPU version (`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`).

3. **Start API Server**
   
   python3 local_llm_api_server.py
   
4. **Test with Client**

   - Option 1: API Client
      python3 local_llm_api_client.py

   - Option 2: Interact with the API
      Test with cURL
      - Open a new terminal (keep the server running) and send a request:
        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"prompt":"Hello, how are you?"}' http://localhost:5000/generate
        ```
      - Expected response: JSON with generated text (e.g., `{"response": "Hello, how are you? I'm doing great, thanks for asking!"}`).

