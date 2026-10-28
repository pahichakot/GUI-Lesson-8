#Digital Clock
from tkinter import *
from time import strftime

#Setup
root = Tk()
root.title("Digital Clock")

#Label
time_display = Label(root, fg = "white", bg = "orange", font = ("Helvetica", 20, "bold"))
time_display.pack()

#Timer - Function
def timer():
    #%H - Hours
    #%M - Minutes
    #%S - Seconds
    #%p - am/pm
    string = strftime("%H:%m:%S:%p")
    time_display.config(text = string)

    #In milliseconds
    time_display.after(1000, timer)

timer()

root.mainloop()