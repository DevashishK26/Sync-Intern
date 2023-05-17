


import random
import time

# Define a function to greet the user
def greet():
    greetings = ["ChatBot: Hello! I'm your travel assistant.", "ChatBot: Hi, I'm here to help you plan your trip."]
    greeting = random.choice(greetings)
    print(greeting)
    time.sleep(2)

# Define a function to ask for the user's name
def ask_name():
    print("ChatBot: What's your name?")
    name = input("User: ")
    time.sleep(1)
    print("ChatBot: Nice to meet you, " + name + "!")
    time.sleep(2)

# Define a function to ask for the user's travel destination
def ask_destination():
    print("ChatBot: Where would you like to travel to?")
    destination = input("User: ")
    time.sleep(1)
    print("ChatBot: Great choice! " + destination + " is a beautiful place.")
    time.sleep(2)

# Define a function to ask for the user's travel dates
def ask_dates():
    print("ChatBot: When do you plan to travel?")
    dates = input("User: ")
    time.sleep(1)
    print("ChatBot: Okay, your travel dates are " + dates + ".")
    time.sleep(2)

# Define a function to ask if the user needs help with anything else
def ask_help():
    print("ChatBot: Is there anything else I can help you with?")
    help_needed = input("User: ").lower()
    if help_needed == "yes":
        return True
    else:
        return False

# Main function to run the chatbot
def main():
    greet()
    ask_name()
    ask_destination()
    ask_dates()
    while ask_help():
        ask_destination()
        ask_dates()
    print("ChatBot: Okay, have a great trip!")

# Run the main function
if __name__ == "__main__":
    main()
