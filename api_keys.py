import json 

with open("api_keys/keys.json", "r") as file:
    keys = json.load(file)

gpt_api_key = keys["gpt_api_key"]
elevenlabs_api_key = keys["elevenlabs_api_key"]
