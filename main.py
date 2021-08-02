import pyttsx3 
import os



current_path = os.getcwd()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


name = input('What would you like to name your To-Do List: ')
name_with_txt  = name + ".txt"

with open(name_with_txt, "w") as create:
    create.write("")

while True:

    item_name = input('Enter To-Do List item name:')

    if "exit" not in item_name:

        with open(name_with_txt, 'a') as append:
            append.write(f"{item_name} \n")

    if "exit" in item_name:
        with open(name_with_txt, 'r') as f:
            a = f.read()
        speak(a)
        break
