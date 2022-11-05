
import datetime

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        return ("Hello Friend")
    elif hour>=12 and hour<18:
        return ("Good Afternoon, I'm ready. You can call me anytime")
    else:
        return ("Good Evening sir, I'm ready. You can call me anytime")
    

