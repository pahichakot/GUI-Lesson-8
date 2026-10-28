#Speed Calculator
from tkinter import *

#Setup
root = Tk()
root.title("Speed Calculator")
root.geometry("700x300")

#Enter distance - Label
distance_label = Label(root, text = "Enter the distance in kilograms", fg = "blue", font = ("Helvetica", 16, "bold"))
distance_label.grid(row = 0, column = 0)

#Enter distance - Entry
distance_entry = Entry(root, width = 10)
distance_entry.grid(row = 1, column = 0)

#Enter time - Label
time_label = Label(root, text = "Enter the time in hours", fg = "purple", font = ("Helvetica", 16, "bold"))
time_label.grid(row = 0, column = 2)

#Enter time - Entry
time_entry = Entry(root, width = 10)
time_entry.grid(row = 1, column = 2)

#Calculate Speed - Function
def calc_speed():
    distance = distance_entry.get()
    time = time_entry.get()

    speed = int(distance) / int(time)
    speed_label.config(text = "Speed: " + str(speed))

#Calculate - Button
calc_button = Button(root, text = "Calculate Speed", command = calc_speed)
calc_button.grid(row = 2, column = 1)

#Speed - Label
speed_label = Label(root, fg = "green", font = ("Times New Roman", 20, "bold"))
speed_label.grid(row = 4, column = 1)

root.mainloop()