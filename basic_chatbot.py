def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hi! How can I help you?"

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! What about you?"

    elif user_input in ["i am fine", "i am good", "fine", "good"]:
        return "That's great to hear 😊"

    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple rule-based chatbot."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that."


def run_chatbot():
    print("🤖 Chatbot Started")
    print("Type 'bye' or 'exit' to stop the chat\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


# Start chatbot
run_chatbot()
