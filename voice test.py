import time
import pyttsx3

engine = pyttsx3
timestamp = time.strftime("%H : %M : %S")
my_time = time.strftime("%H")
hour = int(my_time)


if 3 <= hour < 12:
    print("Good Morning Sir")
    greeting = "Good Morning, Sir!"


elif hour == 12:
    print("Good Noon Sir")
    greeting = "Good Noon, Sir!"


elif 12 < hour < 17 :
    print("Good Afternoon Sir")
    greeting = "Good Afternoon, Sir!"


else:
    print("Good Night Sir")
    greeting = "Good Night, Sir!"


engine.speak(greeting)
engine.speak("The current time is  " + timestamp)
a = "the current time is"
print(a.title(), timestamp)
