"""
Ollama API - Interactive Chatbot
"""

import requests


def chat(user_message):
    """Send message and get response"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": user_message,
                "stream": False
            }
        )

        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"

        data = response.json()

        return data.get("response", "No response generated.")

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
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