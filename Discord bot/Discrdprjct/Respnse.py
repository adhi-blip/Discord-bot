import ollama


def chat_with_ollama(prompt):
    """Sends user input to the Ollama chatbot and returns the response."""
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']


def main():
    print("Ollama Chatbot - Type 'exit' to quit")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Ollama: Goodbye!")
            break

        response = chat_with_ollama(user_input)
        print("Ollama:", response)


if __name__ == "__main__":
    main()

