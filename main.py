# to avoide writing speech_recognition.something (basically sr is short name)
import speech_recognition as sr  # sr is speach to command converter
# A built in function so we can access any browser
import webbrowser
# A command to speach converter which is not built we need to install
import pyttsx3
# when word == jarvis the program is not able to respond yes because how rapidly the program moves so we are using time.sleep....which will pause everything for a given second
import time

import winsound
import music_lib
import pygame 
import os
import openai

# import sys
# print(sys.executable)


from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)

def play_beep(a: int):
    if a == 1:
        pygame.mixer.init()
        pygame.mixer.music.load("beep_sound_error.mp3")
        pygame.mixer.music.play()

    # Optional: wait until sound finishes
        while pygame.mixer.music.get_busy():   # pygame.mixer.music.get_busy() this shit returns true if music is still playing and false if it's not, if true them loop continues 
            continue
    elif a == 2:
        pygame.mixer.init()
        pygame.mixer.music.load("beep_sound_alertt.mp3")
        pygame.mixer.music.play()

    # Optional: wait until sound finishes
        while pygame.mixer.music.get_busy():   # pygame.mixer.music.get_busy() this shit returns true if music is still playing and false if it's not, if true them loop continues 
            continue
    
    elif a == 3:
        pygame.mixer.init()
        pygame.mixer.Sound("beep_sound_activate.wav").play()
        

    # Optional: wait until sound finishes
        while pygame.mixer.music.get_busy():   # pygame.mixer.music.get_busy() this shit returns true if music is still playing and false if it's not, if true them loop continues 
            continue
    
def speak(command):
    engine = pyttsx3.init()
    engine.say(command) # here engine is what we have assigned to pyttsx.init()
    engine.runAndWait()

# speak("hello bro waddup")    

def processcommand(c: str):
    query = c.lower()

    match query:
        case _ if "open" in query:
            if "google" in query:
                webbrowser.open("https://google.com")
            elif "youtube" in query:
                webbrowser.open("https://youtube.com")
            elif "discord" in query:
                webbrowser.open("https://discord.com")
            elif "github" in query:
                webbrowser.open("https://github.com")
            else:
                site = query.split(" ")[1]
                webbrowser.open(f"https://{site}.com")
                speak(f"I couldn't find a specific match, so I'm opening {site}.com")

        case _ if "play" in query:
            if "succession" in query:
                webbrowser.open(music_lib.music.get("succession"))
            elif "back to chicago" in query:
                webbrowser.open(music_lib.music.get("back to chicago"))
            elif "dark paradise" in query:
                webbrowser.open(music_lib.music.get("dark paradise"))
            elif "skyfall" in query:
                webbrowser.open(music_lib.music.get("skyfall"))
            elif "sad girl" in query:
                webbrowser.open(music_lib.music.get("sad girl"))
            else:
                search_term = query.replace("play", "").strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
                speak(f"I couldn't find that in your music library. Searching YouTube for {search_term}")

        case _: # this is like else, now if we don't understand anythig lets open AI handle it
            speak("sorry, i coudn't understand your command//")

if __name__ == "__main__":
    speak("initializing assistant.....")
    speak("say the code word to activate assistant.....")
    while True:
    # now first step is to make a recogniser object 
        r = sr.Recognizer()
    # listen for the wake word "jarvis"
    # obtain an audio from the microphone
    # source record your audi and keep it with itself so that we can access source and store the audio in command using sr or do other operations                                         
    # processing function
        # Recognize speech using google web searh pi
        try:
            with sr.Microphone() as source:
                print("Listening...")    
                audio = r.listen(source, timeout=5)   # listen take two parameter (anoter one is time out)
            word = r.recognize_google(audio)
            
            if "jarvis" not in word.lower():
                
                speak("wrong code word detected, I am going to hack you.....")
                play_beep(2)
            elif "jarvis" in word.lower():
                speak ("code word detected, activating jarvis")
                play_beep(3)
            
                speak("hello boss, how may i help you")
    
                
                # listen command
                with sr.Microphone() as source:
                    print("how may i help you...")    
                    audio = r.listen(source, timeout=5)   # listen take two parameter (anoter one is time out)
                    command = r.recognize_google(audio)
                    processcommand(command)
                    
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")    
        
        
                    
                
        

