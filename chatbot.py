print("Chatbot: Hello! I am your Chatbot." \
 " How can I help you?" \
 " Type 'bye' to exit.")
    
while True:
    user = input("You:").lower()

 # Exit condition
    if user == "bye":
        print("Chatbot: Goodbye! " \
        " Have a Great Day.")
        break

    #Respones
    elif user in ["hi", "hello", "hey"]:
        print("Chatbot: Hi bro! How can I assist you today?")
    
    elif "your name" in user:
        print("Chatbot: I am a rule-based chatbot. "
        " Created to help you." \
        " You can call me bro!")

    elif "how are you" in user:
        print("Chatbot: I am program based bot!" \
        " but I'm doing Great." \
        " How about You? ")

    elif "who created you" in user:
        print("Chatbot: I was created by Baibhaw.")

    elif "help" in user:
        print("Chatbot: Sure! You can ask me about my name, greetings, Who created me, or exit.")

    else:
        print("Chatbot: Sorry, I don't understand that yet." \
        "Can you try asking Something else!")
