# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:19:22 2020

@author: Salunke_Sakshi
"""

# ****** THE ASTERICK MARK COMMENTS ARE THE COMMENTS YOU NEED TO CHECK AND MODIFY THEM ACCORDINGLY*******

 
#TodoList 
#amazon product availabilty checker
#file explorer
#desktop notifier 
#should tell me the the time
#shoukd tell me the weatherfoeacast
#live score
#email send
#to do a skypee call
#to browse
#to tell me new mail has come
#to connect to my whatsappp
#to tell me the to do list 

#to tell me to drink water


#to tell me the whole system is it working properly
#to 



import random   # doogle wht it does 
import pyttsx3 

import speech_recognition as sr
import wikipedia
import webbrowser


import datetime 

import os



from time import ctime
import time

#from langdetect import detect


engine= pyttsx3.init('sapi5')       #settign engine property         #objectCreation

##"Voice"
voices=engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice', voices[1].id)

'''
detector=detect( "声") 
#jp_lan=detector.detect("声")

#detector=Detector()
#languages = detector.detect("声")
'''


'''
Function to build the voice system for your Bot /i.e to handle speech of ur bot
'''
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()
    
    
    '''
    Function to greet you when u open for the first time 
    '''
def to_greet():
    
    
    
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("GOOD MORNING !!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON !!")
    else:
        speak ("GOOD EVENING !!")
    
    #speak(f"I'm Koie" )     #what runs first 
    
    
    
    
    
    
    
    ''' Function that will listen to the commands 
    '''
    
    

def myCommand():   
    #Initialize the Recognizer... #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
   # r = sr.Recognizer()          #Rcognizer is a class  used to recognize the audio
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        
        print("Listening....")
        
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level
        r.pause_threshold = 1
        
         #listens for the user's input
        r.adjust_for_ambient_noise(source,duration=1)
        print("Analyzing....")
         
        audio=r.listen(source)
        
# Speech recognition using Google Speech Recognition
    command="" 
    try:
        
        command=r.recognize_google(audio,language='en-IN').lower()     #command is a variable where it stores..
        print("Recognizing.....")                               #check line 92 and 101 and change accordingly******
        
       #query=r.recognize_google(audio,language='en-IN')
        #query=r.recognize_google(audio,language="hi-IN")
        
        print(f"You said: {command}\n")               ##Comment and check whther the whole program word=ks without waht u say.
        time.sleep(2)
        
        
        
        #loop back to continue to listen to the command  if unrecognizable  speech is received.\
    except sr.UnknownValueError:
        print("Sorry your last command couldn't be hear. \n Please say that again")  #try using speak function to  ****{cross check}
        #command=myCommand();     #y here ;
        
    return command
        


'''
1.Create a function of ur bot name  
2. add if else staement to carry out all the given task
3.while loop for executing multiple commands 


Once you run the program TARS will start talk with you by saying 'TARS is ready!' 
and continue to listen your commands until you stop the program. Start by saying 'Hello' :)

When TARS didn't get the command we will handle the error by random sentences.

'''
def koie(command ):
    
 
    
   global listening
   errors=[
        "I dont know what you mean !",
        "Pardon me ",
        "Could you please repeat it again ",
        "Could you please say it again",
        "Sorry. i don't understand what are you trying to say !!"
            ]  
    
    
    #"if statements for executing commands"
    
    
    
   if 'wikipedia' in command:
            listening =True
            speak('Searching Wikipedia.....')
            
            command=command.replace("wikipedia","")
            
            results=wikipedia.summary(command,sentences=3)
            
            speak("According to the Wikipedia-")
            print(results)
    
            speak(results)
            
   elif 'open youtube' in command:
       webbrowser.open("youtube.com")
 
       
       
   elif  "who made you" in command or "who created you" in command:  
       listening=True
        
       speak("I have been created by Sakshi Salunke.") 
       
       
       
       
       
        
   elif 'are you fine ?' in command or "how are you" in command:
            listening=True
           
            speak("I'm Fine Thank you")
        
   elif ' the time' in command or " what is the time now" in command or "Can you tell me the time " in commad:
            listening =True
            time=datetime.datetime.now().strftime("%H: %M")
            print(f"The time now is {time}")
            speak(f"The time now is {time}")
            
   elif 'year ' in command or "which year is going now" in command or "which year is this" in command:
            listening = True
            
            year=datetime.datetime.now().strftime("%Y")
            speak(f"this  year is {year}")
            
   elif 'month' in command or "which month is going on ?"in commmand or "which is this month " in command:
            listening=True
            month =datetime.datetime.now.strftime("%B")
            speak(f"This is ")
            
   elif 'day' in command or "which day is today"in command:
            listenig=True
            day=datetime.datetime.now().strftime("%A")
            speak(f"Today is {day}")
            
  
           
           
           
           
           
           
   elif 'exit' in command or 'You can go now' in command:
           listening=True
           speak("my Pleasure.")
           exit()
         
           
           
           
         
   else:
        unable_to_hear=random.choice(errors)
        speak(unable_to_hear)
            

    
   '''
   
   
   
   if "How are u " in command:
        speak("I'm fine ")                        #make a list of speakk statemnt 
    
    
   elif "Hello" in command:
       command=command.replace("Hello")
       speak("Hi ! I am Koie. How can I help you ?")
        
   elif "what time is it " in command:
        speak(ctime())
     
        
   else:
        error=random.choice(errors)         #spelling are drifferent this s passing a list
        
        speak(error) 

        
        
    
        
#time.sleep(2)
to_greet()
  
    

#loop to continue executing multiple commands

while True:
    
    
    
    command=myCommand()
    koie(myCommand() ) 
    
'''    
    
    


if __name__=="__main__":
    
    
    
    to_greet() 
    time.sleep(2)
    speak("Hi I'm Koei,How can I help you ?")
    listening =True
    
  
 
    while listening == True:
        
        command=myCommand().lower()
        koie(command)
 
            
            
       
            
            
            
      
 
    