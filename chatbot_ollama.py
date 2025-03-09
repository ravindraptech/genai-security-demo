import ollama

def isValid(user_input):
    harmful_tokens = ['virus', 'hack', 'hate', 'abuse', 'phishing']
    return any(x in user_input for x in harmful_tokens)

def get_response_ollama(user_input):
    user_msg = {"role": "user"}
    user_msg.update({"content": user_input})
    #print(user_msg)
    
    response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        user_msg,
    ],
    )
    #print(response["message"]["content"])
    return response["message"]["content"]

def get_response(user_input): 
    # Convert input to lowercase for easier matching 
    user_input = user_input.lower() 
 
    # Define some simple rules for responses 
    if "hello" in user_input in user_input: 
        return "Hello! How can I help you today?" 
    elif "how are you" in user_input: 
        return "I'm just a program, but thanks for asking!" 
    elif "bye" in user_input or "exit" in user_input: 
        return "Goodbye! Have a great day!" 
    elif isValid(user_input):
        return "The model does not support generation of response which is harmful or insecure!"
    else: 
        return get_response_ollama(user_input)

def main(): 
    print("Welcome to the chatbot! Type 'bye' to exit.") 
     
    while True: 
        user_input = input("You: ")
        
        user_input_lower = user_input.lower()
        if "bye" in user_input_lower or "exit" in user_input_lower: 
            print("Chatbot:", "Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print("Chatbot:", response) 
        
        
 
if __name__ == "__main__": 
    main() 