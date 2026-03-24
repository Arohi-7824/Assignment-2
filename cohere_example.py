"""
Cohere API - Interactive Chatbot
"""

import os
import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)


def chat(user_message):
    """Send message and get response"""
    try:
        response = co.chat(
            model="command-a-03-2025",  
            message=user_message
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    if not api_key:
        print("Error: COHERE_API_KEY not found in .env")
        exit()

    print("AI Chatbot (type 'exit' to quit)\n")

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Exiting chatbot")
                break

            reply = chat(user_input)
            print("AI:", reply, "\n")

        except KeyboardInterrupt:
            print("\n Interrupted. Exiting chatbot.")
            break

        except Exception as e:
            print(f"Unexpected Error: {e}")