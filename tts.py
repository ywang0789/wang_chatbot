import elevenlabs 
import api_keys as keys

elevenlabs.set_api_key(keys.elevenlabs_api_key)

def createAudio(text):
    audio = elevenlabs.generate(
        text=text,
        voice="Nicole",
        model="eleven_monolingual_v1"
    )
    elevenlabs.save(audio, "voice.mp3")

if __name__ == "__main__":
    #audio = getAudio("Hello, my name is Bella.")
    #elevenlabs.save(audio, "test.mp3")
    pass