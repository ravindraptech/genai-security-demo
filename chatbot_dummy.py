# chatbot_dummy.py 
 
def get_response(user_input): 
    # Convert input to lowercase for easier matching 
    user_input = user_input.lower() 
 
    # Define some simple rules for responses 
    if "hello" in user_input or "hi" in user_input: 
        return "Hello! How can I help you today?" 
    elif "how are you" in user_input: 
        return "I'm just a program, but thanks for asking!" 
    elif "bye" in user_input or "exit" in user_input: 
        return "Goodbye! Have a great day!" 
    else: 
        return "I'm sorry, I don't understand that." 
 
def main(): 
    print("Welcome to the chatbot! Type 'bye' to exit.") 
     
    while True: 
        user_input = input("You: ") 
        response = get_response(user_input) 
        print("Chatbot:", response) 
 
        if "bye" in user_input or "exit" in user_input: 
            break 
 
if __name__ == "__main__": 
    main() 