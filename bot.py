import openai 

MODEL = "gpt-3.5-turbo"

class bot():
    def __init__(self, key):
        self.key = key
        openai.api_key = self.key

    def chat(self, message):
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']
    



