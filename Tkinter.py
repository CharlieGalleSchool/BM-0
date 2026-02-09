from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime
from tkinter import filedialog as fd


currentfile = None

# Create the main window
root = Tk()
root.title("FileEditor")

#Set size of window
root.geometry("900x900")

menubar = Menu(root)

root.config(menu=menubar)

def open_file_selection():
    global currentfile
    file = fd.askopenfile()
    currentfile = file.name
    return file
TextBox = Text(root, width=600, height=600)

def New_File():
	global currentfile
	with open("Note.txt", 'w') as file:
		print("created")

	currentfile = "Note.txt"


def Open_File():
	file = open_file_selection()
	TextBox.insert(END, file.read())

def Save_File():
	print(currentfile)
	if currentfile != None:
		with open(currentfile, 'w') as file:
			file.write(TextBox.get("1.0", END))


file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='FileEditor', menu = file)
file.add_command(label ='New File', command = New_File)
file.add_command(label ='Open...', command = Open_File)
file.add_command(label ='Save', command = Save_File)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

TextBox.pack()





root.mainloop()