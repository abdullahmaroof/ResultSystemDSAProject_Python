import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class call_voice:
    @staticmethod
    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=5 and hour<10:
            speak('Good Morning!')
        elif hour>=10 and hour<16:
            speak('Good Afternoon!')
        elif hour>=16 and hour<18:
            speak('Good Evening!')
        else:
            speak('Good Night!')
        speak('Welcome to Superior Exam Portal by Coder TECH')

class voice_aboutus(call_voice):
    @staticmethod
    def wishme():
        speak("you can see about the team of coder tech!!!")

class voice_aboutabdullah(call_voice):
    @staticmethod
    def wishme():
        speak("He is a leader of coder tech!!!")
        speak("Name: Abdullah Maroof")
        speak("Rollnumber: B A I M - F 19- 007")
        speak("section: 3 A")
        speak("Program: B S Artificial Intelligence")
        speak("Department: Software Engineering")
        speak("Student of Superior University, gold campus")

class voice_aboutabdulkabeer(call_voice):
    @staticmethod
    def wishme():
        speak("He is a member of coder tech!!!")
        speak("Name: Abdul Kabeer Abid")
        speak("Rollnumber: B D S M - S 20- 005")
        speak("section: 3 A")
        speak("Program: B S Data Science")
        speak("Department: Software Engineering")
        speak("Student of Superior University, gold campus")

class voice_aboutZUBAIR(call_voice):
    @staticmethod
    def wishme():
        speak("He is a member of coder tech!!!")
        speak("Name: Zubair Ali")
        speak("Rollnumber: B A I M - S 20- 009")
        speak("section: 3 A")
        speak("Program: B S Artificial Intelligence")
        speak("Department: Software Engineering")
        speak("Student of Superior University, gold campus")

class voice_backmain(call_voice):
    @staticmethod
    def wishme():
        speak("Back   to   main   page!!!")


class call_stdlogin(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to student login. Please enter your username and password")


class call_adminlogin(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to admin login. Please enter your username and password")

class call_admin(call_voice):
    @staticmethod
    def wishme():
        speak("You are login to admin portal")

class call_std(call_voice):
    @staticmethod
    def wishme():
        speak("You are login to student portal")