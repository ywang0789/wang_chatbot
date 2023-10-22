import elevenlabs 
import os
import api_keys as keys

# default voice file name
FILENAME = "voice"

# path to audio file
PATH = os.path.join(os.getcwd(), "hidden/" + FILENAME)

elevenlabs.set_api_key(keys.elevenlabs_api_key)

def createAudio(text):
    # generate audio
    audio = elevenlabs.generate(
        text=text,
        voice="Nicole",
        model="eleven_monolingual_v1"
    )
    # save audio
    elevenlabs.save(audio, PATH)
    print(PATH)
    return PATH



# if __name__ == "__main__":
#     audio = createAudio("Hello, my name is Bella.")
#     #os.remove(filename)
#     pass
