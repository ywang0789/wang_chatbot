import elevenlabs 
import os
import api_keys as keys

# default voice file name
FILENAME = "voice.mp3"

# path to audio file
PATH = os.path.join(os.getcwd(), "hidden/" + FILENAME)

elevenlabs.set_api_key(keys.elevenlabs_api_key)

def createAudio(text):
    delete_file_if_exists(PATH)
    # generate audio
    audio = elevenlabs.generate(
        text=text,
        voice="Nicole",
        model="eleven_monolingual_v1"
    )
    elevenlabs.save(audio, PATH)
    return PATH

def delete_file_if_exists(filepath):
    if os.path.isfile(filepath):
        print("File exists, deleting...")
        os.remove(filepath)

# if __name__ == "__main__":
#     audio = createAudio("Hello, my name is Bella.")
#     #os.remove(filename)
#     pass
