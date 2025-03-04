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
   
5. **Test with API Client**
   
   python3 local_llm_api_client.py

   
