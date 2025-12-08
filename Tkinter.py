from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("StopLight")

#Set size of window
root.geometry("300x150")

ColorChange = Button(root, text="Color will change", background="White")

ColorChange.grid(row=4, column=0, columnspan=2)


def changecolor(color):
	ColorChange.config(bg=color)

label = Label(root, text="Click Buttons to change the color!").grid(row=3, column=2)


Button(root, text="red", background="red",command=lambda: changecolor("red")).grid(row=0, column=1)
Button(root, text="yellow", background="yellow",command=lambda: changecolor("yellow")).grid(row=0, column=2)
Button(root, text="green", background="green",command=lambda: changecolor("green")).grid(row=0, column=3)
Text(root, height=5, width=20).grid(row=4, column=2)








root.mainloop()