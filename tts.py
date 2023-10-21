import elevenlabs 

elevenlabs.set_api_key("")

audio = elevenlabs.generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Bella",
  model="eleven_multilingual_v2"
)
elevenlabs.save(audio, "test.mp3")