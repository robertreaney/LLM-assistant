import openai
import os

from typing import List

def api_call(model:str, messages:List[dict]):
    openai.api_key = os.getenv("OPEN_API_KEY")

    context = [
        "You are Python-AI, an AI designed to create Python code."
    ]

    system_message = [{"role": "system", "content": m} for m in context]


    completion = openai.ChatCompletion.create(model=model, messages=system_message + messages)

    return completion.choices[0].message.content


def message_formatter(command):
    messages = []
    for text in command:
        if isinstance(text, str):
            messages.append({'role': 'user', 'content': text})
    return messages

def main(command):
    return api_call(model='gpt-3.5-turbo', messages=message_formatter(command))


command= (
    "Give the python code that takes this size (100,1) numpy array named x and adds an element 1 to each row. The final matrix should be of size (100, 2) with the first column having all elements equal 1",
    )


response = main(command)
