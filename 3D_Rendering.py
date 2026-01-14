from tkinter import *
from tkmacosx import Button
import numpy
import random
root = Tk()

root.title("3D Rendering")
root.geometry("500x500")

c = Canvas(root, width=500, height=500)

c.pack()

c.delete("all")



def triangle(points, color):
	c.create_polygon(points, fill=color)


def RenderFrame():
	c.create_polygon([100,100,200,200,300,300], fill="#476042")
	triangle([100,100,200,200,300,300], "#476042")
	root.after(100, RenderFrame)

root.after(100, RenderFrame)
root.mainloop()

