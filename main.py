import pyttsx3

engine = pyttsx3.init()
text = "Привет, я сказочник, готовся мы сейчас будем портить тебе психику"
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", "<pyttsx3.voice.Voice object at 0x00000266925A16D0>")
engine.say(text)
engine.runAndWait()