#Creating a Virtual Assistant using Python
import speech_recognition as sr #sr is a variable
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer() #used to recognize the voice
engine=pyttsx3.init() #create a engine that will speak to you and initialize this engine
voices=engine.getProperty('voices') # We declare a variable called voices to get all the different voices ,the python text to speech can provide
engine.setProperty('voice',voices[1].id)

def talk(text): # We define a function that will always say whatever we pass in the parameter
    engine.say(text)
    engine.runAndWait() #It makes the speech audible in the system

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source) #We use microphone as a source and then calling the speech recognizer to listen to this source
            command=listener.recognize_google(voice) #We use google api.We pass the voice to the google.Google gives us the text
            command=command.lower()#coverted the command to lower case
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command() #We are getting the command using take_command function
    print(command)
    if 'play' in command:#4
        song=command.replace('play','') #Replace the word play with empty string
        talk('playing'+ song)
        pywhatkit.playonyt(song) #playonyt means play on youtube

    elif 'time' in command:#1
        time=datetime.datetime.now().strftime('%I:%M %p') #to get current date and time in am pm format,otherwise for 24 hr format we use '%H:%M' ,strf converts the date and time into string format
        print(time)
        talk('Current time is '+time)

    elif 'who is' in command:#2
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)#We want only 1 line from wikipedia
        print(info)
        talk(info)

    elif 'joke' in command:#3
        talk(pyjokes.get_joke()) #Used for listening to a joke


    elif 'are you single' in command:
        talk('I am in a relationship with Google Assistant')

    else:
        talk('Please say the command again')

while True:
    run_alexa()
