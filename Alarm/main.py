from tkinter import *
import time as t
import datetime as dt
import pyttsx3




#alarm_time = input("Enter alarm time (HH:MM:SS AM/PM): ").strip()




win = Tk()
win.title("Alarm clock")
win.geometry("600x600+100+100")
win.resizable(False, False)


def start():
    alarms = times.get()
    check_alarm(alarms)

times = Entry(  font=( "arial", 32, "bold"))
Label(text="Enter alarm time (HH:MM:SS AM/PM)", font=("arial", 16, "bold")).pack()
times.pack()
Start = Button(text="Start", width=9, height=2,  background="light green", command=start)
Start.pack()

def alarmsound():
    
    engine = pyttsx3.init()
    times.insert(0,"Close out this program to end the alarm...")
    while True:
        engine.say("Wake up you little fuck")
        engine.runAndWait()


def check_alarm(alarm):
    print("Alarm set")
    while True:
        current_time = dt.datetime.now().strftime("%I:%M:%S %p")  # Update the time
        if current_time == alarm:
            print("Wake up!")
            alarmsound()
            break
        t.sleep(1)


win.mainloop()

