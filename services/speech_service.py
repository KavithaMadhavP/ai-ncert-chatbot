import speech_recognition as sr

def audio_to_text(audio_bytes):
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio_data)
    except:
        return None
