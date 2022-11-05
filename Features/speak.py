
import pyttsx3
import playsound
from gtts import gTTS
import os
from Features.csv_writer import append_data

def speak(audio):
    engine = pyttsx3.init('sapi5') #google API
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',  140)  # rate by default is 200
    print(f"A.I : {audio}")
    engine.say(text = audio)
    engine.runAndWait()
    append_data("logs\speak_logs.csv", "A.I", audio)
    print(" ")
    
    
# from gtts import gTTS
# from playsound import playsound

# def speak(audio):
#     """
#     This function adds google assistant voice to our function incase of any hindi input it can also give hindi output un-comment the given line to listen hindi speech
#     """
#     engine = gTTS(audio)
#     engine.save('Assis.mp3')
#     playsound('Assis.mp3')


def speak_2(output):
    global num
  
    # num to rename every audio file 
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)
  
    toSpeak = gTTS(text = output, lang ='en-in', slow = True)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3 "
    toSpeak.save(file)
      
    # playsound package is used to play the same file.
    playsound.playsound(file, True) 
    os.remove(file)

    