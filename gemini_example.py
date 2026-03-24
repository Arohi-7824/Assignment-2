"""
Gemini API - Interactive Chatbot
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def chat(user_message):
    """Send message and get response"""
    try:
        response = model.generate_content(user_message)
        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        exit()

    print("Gemini AI Chatbot (type 'exit' to quit)\n")

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