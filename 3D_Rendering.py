from tkinter import *
from tkmacosx import Button
import numpy
import random
import json
root = Tk()

root.title("3D Rendering")
root.geometry("500x500")

with open("cube.json", 'r') as file:
	print(file)
	cube_points = json.load(file)

print(cube_points["vertices"])

c = Canvas(root, width=500, height=500, bg="yellow")

def triangle(points, color):
	c.create_polygon(points, fill=color)


def RenderFrame():
	c.delete("all")
	c.create_polygon([100,100,200,200,450,300], fill="#476042")
	triangle([100,100,200,200,300,300], "#476042")
	root.after(100, RenderFrame)



root.after(100, RenderFrame)

c.pack()
root.mainloop()

