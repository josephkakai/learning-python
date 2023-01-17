import speech_recognition as sr
from selenium import webdriver

class voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()        
        self.listenerOnMic()

    def listenerOnMic(self):        
        while True:            
            try:                
                with sr.Microphone() as source:                    
                    audio = self.recognizer.listen(source)                    
                    comand = self.recognizer.recognize_google(audio).lower()                    
                    
                    if "search" in comand:
                        driver = webdriver.Chrome()
                    driver.get(f"https://www.google.com/search?&aqs=chrome.0.0i131i433i512j0i512l9.23986j0j7&sourceid=chrome&ie=UTF-8={command.split('search ')[-1]}")
            except sr.UnkownValueError:                
                pass

listener = voice()

