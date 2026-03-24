"""
Groq API - Interactive Chatbot
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(user_message):
    """Send message and get response"""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI Assistant"
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ],
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("AI Chatbot (type 'exit' to quit)\n")

    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not found in .env")
        exit()

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Exiting chatbot")
                break

            response = chat(user_input)
            print("AI:", response, "\n")

        except KeyboardInterrupt:
            print("\n Interrupted. Exiting chatbot.")
            break

        except Exception as e:
            print(f"Unexpected Error: {e}")