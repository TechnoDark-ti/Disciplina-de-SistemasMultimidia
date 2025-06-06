import speech_recognition as sr
import pyttsx3


def speech():
    r = sr.Recognizer()

    engine = pyttsx3.init()

    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print("AAAÃÃÃNNHHÓÓOOOØOOONNN")
        engine.say("AAAÃÃÃNNHHÓÓOOOØOOONNN")
        engine.runAndWait()

        audio = r.listen(mic)

        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print(texto)
        except sr.UnknownValueError:
            print("AAAÃÃÃNNHHÓÓOOOØOOONNN")
        except sr.RequestError as e:
            print(f"AAAÃÃÃNNHHÓÓOOOØOOONNN: {e}")

