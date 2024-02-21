#for getting input from mic and transcribing it
import speech_recognition as sr

#for using the transcribed input as prompt
import openai

#for converting text to speech
import pyttsx3

import sys
sys.stdout.reconfigure(encoding='utf-8')

sr_object = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Speak please: ")
        sr_object.adjust_for_ambient_noise(source)
        audio = sr_object.listen(source)
        try:
            print("Processing...")
            text = sr_object.recognize_whisper(audio_data=audio)
            print("You spoke: ",text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))        

    return text

def get_response(prompt):
    openai.api_key="apikey"
    message=prompt
    messages=f"act as a speech assistant and create a conversation reply for {message}"
    chat = openai.completions.create(
            model="gpt-3.5-turbo-instruct",prompt=messages,temperature=0,max_tokens=100,top_p=1,frequency_penalty=0.0,presence_penalty=0.0
        )
    reply = chat.choices[0].text
    print(reply)
    return reply

def convert_audio(reply):
    engine = pyttsx3.init()

    engine.setProperty('rate',150)
    engine.setProperty('volume',0.9)
    engine.say(reply)

    engine.runAndWait()

prompt = listen()
reply = get_response(prompt)
convert_audio(reply)