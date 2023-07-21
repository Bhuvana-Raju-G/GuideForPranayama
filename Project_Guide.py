import tkinter as tk
import pyttsx3

# Top level window
frame = tk.Tk()
frame.title("Guide ")
frame.geometry('400x200')

#function to speak out
def speak(s):
    engine=pyttsx3.init()
    engine.say(s)
    engine.runAndWait()
    
#Main Function , on click of function  
def startExercise():
    print("Guide Started")
    lbl.config(text="Guide Started")
    inp=int(inputtxt.get(1.0, "end-1c"))
    if inp==0:
        lbl.config(text="Please provide number of reptations you in text field")
        speak("please Provide Number of Repetations other than zero")
        
    else:
        lbl.config(text="Guide Started, Choosed repetations for  "+str(inp)+"  times")
        GuideStarted(inp)
    exit()
       
#Repetations        
def GuideStarted(n):
    for i in range(int(n)):
        Exercise_1()

#Counts the Process    
def counter():
    for i in range(3):
        speak(i)
        
 #Exercise fucnction 1       
def Exercise_1():
    speak("Inhale")
    print("Inhale")
    counter()   
    speak("Exhale")
    print("Exhale")
    counter()        
        
# TextBox Creation
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Start",
						command = startExercise)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "Guide Started")
lbl.pack()

frame.mainloop()
