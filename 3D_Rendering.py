from tkinter import *
from tkmacosx import Button
import numpy

root = Tk()

root.title("3D Rendering")
root.geometry("500x500")

c = Canvas(root, width=500, height=500)

c.pack()

c.delete("all")



def triangle(points, color):
	c.create_polygon(points, fill=color)





triangle([100,100,200,300,300,400], "#476042")

root.mainloop()

