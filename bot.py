import openai

MODEL = "gpt-3.5-turbo"


class bot:
    def __init__(self, key):
        self.key = key
        openai.api_key = self.key
        self.history = []
        self.history.append(
            {"role": "system", "content": "in this scenario, your name is bob the builder"}
        )

    def chat(self, msg):
        self.history.append({"role": "user", "content": msg})
        response = openai.ChatCompletion.create(
            model=MODEL, messages=self.history
        )
        
        response = response["choices"][0]["message"]["content"]

        self.history.append({"role": "system", "content": response})
        return response
    

if __name__ == "__main__":
    b = bot("")
    print(b.chat("hello what is your name?"))
    print(b.chat("How are you?"))
    print(b.history)
