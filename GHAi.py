
# -*- coding: utf-8 -*-
import os
from groq import Groq

def get_groq_response(question):
    try:
        client = Groq(
            api_key="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",  # Add your API key here
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("\033[92m" + r"""
 ██████╗ ██╗  ██╗     █████╗ ██╗
██╔════╝ ██║  ██║    ██╔══██╗██║
██║  ███╗███████║    ███████║██║
██║   ██║██╔══██║    ██╔══██║██║
╚██████╔╝██║  ██║    ██║  ██║██║
 ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
                                 """ + "\033[0m")
    while True:
        question = input("Enter your question (type 'q' to quit): ")
        if question.lower() == 'q':
            break
        answer = get_groq_response(question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
