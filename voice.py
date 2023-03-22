import openai
import speech_recognition as sr
import pyttsx3

# Configurer une clé d'API valide
openai.api_key = "yourAPIKey-xxxxxXXXX1111222abc"


# Initialiser le recognizer
r = sr.Recognizer()

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

while True:
    # Ecouter pour la commande vocale
    with sr.Microphone() as source:
        print("Listen...")
        audio = r.listen(source)

    # Transcrire la commande vocale
    try:
        prompt = r.recognize_google(audio, language="en-EN")
        print("You said: " + prompt)
        if prompt == "exit":
            break
    except sr.UnknownValueError:
        print("I didnt understand")
        continue
    except sr.RequestError as e:
        print("Service error; {0}".format(e))
        continue

    # Envoyer une requête à l'API de GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Afficher la réponse
    print(response["choices"][0]["text"])
    engine.say(response["choices"][0]["text"])
    engine.runAndWait()
