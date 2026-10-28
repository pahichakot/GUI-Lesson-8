#Calculator
from tkinter import *

#Setup
root = Tk()
root.geometry("500x500")
root.title("Calculator")
root.config(bg= "pink")

#Num1 - Label
num1_label = Label(root, text = "Enter the first number", fg = "black")
num1_label.grid(row = 1, column = 1)

#Num1 - Entry
num1_entry = Entry(root, width = 15)
num1_entry.grid(row = 1, column = 2)

#Num2 - Label
num2_label = Label(root, text = "enter the second number", fg = "black")
num2_label.grid(row = 2, column = 1)

#Num2 - Entry
num2_entry = Entry(root, width = 15)
num1_entry.grid(row = 2, column = 2)

#Add - Button
add = Button(root, text = "Add", bg = "red")
add.grid(row = 3, column = 0)

#Subtract - Button
subtract = Button(root, text = "Subtract", bg = "light blue")
subtract.grid(row = 3, column = 1)

#Multiply - Button
multiply = Button(root, text = "Multiply", bg = "purple")
multiply.grid(row = 3, column = 2)

#Divide - Button
divide = Button(root, text = "Divide", bg = "purple")
divide.grid(row = 3, column = 3)

#Answer - Label
answer_label = Label(root, fg = "orange")
answer_label.grid(row = 4, column = 1)

root.mainloop()