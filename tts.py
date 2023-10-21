import elevenlabs 
import api_keys as keys

elevenlabs.set_api_key(keys.elevenlabs_api_key)

def getAudio(text):
    audio = elevenlabs.generate(
        text=text,
        voice="Bella",
        model="eleven_monolingual_v1"
    )
    return audio

if __name__ == "__main__":
    #audio = getAudio("Hello, my name is Bella.")
    #elevenlabs.save(audio, "test.mp3")
    pass