import openai 

KEY = ""

openai.api_key = KEY

MODEL = "gpt-3.5-turbo"

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Knock knock."}
    ]
)

print(response['choices'][0]['message']['content'])



