from tkinter import *
from tkmacosx import Button

root = Tk()

root.title("Creating File")
root.geometry("500x500")

textbox = Text(root, height=20, width=52)


def save():
	with open("test.txt", 'w') as file:
		file.write(textbox.get("1.0", END))

button = Button(root, text="text", command=save)

textbox.pack()

button.pack()

root.mainloop
