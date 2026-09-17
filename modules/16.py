import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

engine.say("Hello Kapil")
engine.say("Welcome to Python programming")

engine.runAndWait()