import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

listener=sr.Recognizer()
model=pyttsx3.init()
voices=model.getProperty('voices')
model.setProperty('voice',voices[1].id)
def talk(text):
    model.say(text)
    model.runAndWait()
def get_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'elena' in command:
                command=command.replace('elena','')
                print(command)
    except:
        pass
    return command
while True:
    def run_elena():
        command =get_command()
        print(command)
        if 'hello' in command:
            greetings = "Hello! I am Elena"
            question = 'What can i do for you?'
            print(greetings)
            talk(greetings)
            print(question)
            talk(question)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("current time is")
            print(time)
            talk(time)
        elif 'date' in command:
            date = datetime.date.today()
            print(date)
            talk(date)
        elif 'tell me about' in command:
            about = command.replace('tell me about', '')
            info = wikipedia.summary(about, sentences=2)
            print(info)
            talk(info)
        elif 'who' in command:
            about = command.replace('who', '')
            info = wikipedia.summary(about, sentences=2)
            print(info)
            talk(info)
        elif 'stop' in command:
            bye = "Bye"
            greet="have a cute day"
            print(bye)
            talk(bye)
            print(greet)
            talk(greet)
            exit()
        else:
            print("Sorry can you please repeat the command")

    run_elena()
