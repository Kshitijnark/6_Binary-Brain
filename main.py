
import requests
import os
from Features.wishme import wishMe
from Features.csv_writer import append_data
from Features.speak import speak
from Features.listen import listen_std
from Features.time_checker import inactive
from Features.read_logs import read_logs
import time



sender = "Kshitij"
bot_name = "Harry"
bot_message = ""
user = ""
append_data("logs/chat_logs.csv","entered", "entered")
speak("Hello Friend ,I am Harry!!!")
speak("Activated")
#speak("Would you like to talk to me?")
#choice = input("Would you like to talk to me?")
#choice = listen_std()
choice =True
if choice ==True:
    speak(wishMe())
    while True:
        print("---------------------------------------------------------------------------\nInactivated")
        print(f"call my name ({bot_name}) to resume")
        query = listen_std()
        if f"{bot_name.lower()}" in query:
            status = True

            append_data('data.csv',"Entered", "Entered")

            while status == True:
                print("Activated")
                print("Tell me your problem? How can i help you?\n---------------------------------------------------------------------------")
                user_message = listen_std()
                if len(user_message) != 0:
                    print("Sending message now....")
                    r = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": sender, "message": user_message})
                    print("Bot: ", end = ' ')
                    user = read_logs("logs/initial_face_logs.csv", "user")
                   
                    for i in r.json():
                        try:
                            bot_message = i["text"]
                            bot_message = bot_message.replace("sir",user).replace("Sir",user)
                            speak(bot_message)
                            append_data("logs/chat_logs.csv", user_message,bot_message )
                        except Exception as e:
                            # print("Exception: ", e)
                            print("Exception occured")
                            for content in i.keys():
                                speak(i[content])
                                append_data("logs/chat_logs.csv", user_message, i[content])
                status = inactive('logs/chat_logs.csv', 30)
    
