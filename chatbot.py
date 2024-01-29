import random

# Simple rule-based chatbot
def simple_chatbot(user_input):
    user_input = user_input.lower()

    # Define some basic rules
    greetings = ['hi', 'hello', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    weather_keywords = ['weather', 'temperature', 'forecast']
    joke_keywords = ['tell me a joke', 'make me laugh']
    compliments = ['you are awesome', 'great job', 'well done']
    questions_about_chatbot = ['who created you?', 'what are you?', 'how do you work?']
    user_name_keywords = ['your name', 'call you']
    favorite_color_keywords = ['your favorite color', 'what color do you like?']
    thanks_keywords = ['thank you', 'thanks', 'appreciate it']
    age_keywords = ['how old are you?', 'your age']

    # Check user input against rules
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in user_input for word in farewells):
        return "Goodbye! Have a great day."

    elif any(word in user_input for word in weather_keywords):
        return "I'm sorry, I don't have real-time weather information. You can check a weather website for that."

    elif any(word in user_input for word in joke_keywords):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
        ]
        return random.choice(jokes)

    elif any(word in user_input for word in compliments):
        return "Thank you! I'm here to assist you."

    elif any(word in user_input for word in questions_about_chatbot):
        return "I am a simple rule-based chatbot created using Python. I'm here to chat and assist with basic queries."

    elif any(word in user_input for word in user_name_keywords):
        return "I don't have a personal name, but you can call me ChatBot."

    elif any(word in user_input for word in favorite_color_keywords):
        return "I don't have a favorite color. I'm all about text and logic!"

    elif any(word in user_input for word in thanks_keywords):
        return "You're welcome! If you have more questions, feel free to ask."

    elif any(word in user_input for word in age_keywords):
        return "I don't have an age. I'm just a program running on a computer."

    else:
        return "I'm a simple chatbot and I don't understand that. Can you ask me something else?"

# Example usage
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Bot:", response)
