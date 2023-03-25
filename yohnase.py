import openai

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a kind, helpfull and fun assistant."}
]

while True:``
    messages.append(
        {"role": "user", "content": input("You: ")},
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        )
    messages.append(response["choices"][0]["message"])

    print("chatGPT:", messages[-1]["content"])