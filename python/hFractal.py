# hw9.py
# Edward Shin
# edwardsh
# Section A

import math
import os
from tkinter import *

####################################
# H-Fractals Viewer Program
####################################

def init(data):
    data.vLine = data.height//2    # vertical line
    data.hLine = data.width//2     # horizontal line
    data.cx = data.width//2        # center x
    data.cy = data.height//2       # center y
    data.level = 0
    data.lineWidth = 3


# draw H-fractal according to the level
def createHFractal(data, canvas, cx, cy, vLine, hLine, level):
    x0 = cx - hLine//2
    y0 = cy - vLine//2
    x1 = cx + hLine//2
    y1 = cy + vLine//2

    drawH(data, canvas, cy, x0, y0, x1, y1)
    
    # stop rescursion once level is 0
    if(level == 0): return
    
    # otherwise, make another smaller H for each of the four endppoints of H
    else:
        createHFractal(data, canvas, x0, y0, vLine//2, hLine//2, level-1)
        createHFractal(data, canvas, x0, y1, vLine//2, hLine//2, level-1)
        createHFractal(data, canvas, x1, y0, vLine//2, hLine//2, level-1)
        createHFractal(data, canvas, x1, y1, vLine//2, hLine//2, level-1)


# draw a single H
def drawH(data, canvas, cy, x0, y0, x1, y1):
    canvas.create_line(x0, y0, x0, y1, width=data.lineWidth)  # vertical line 1
    canvas.create_line(x1, y0, x1, y1, width=data.lineWidth)  # vertical line 2
    canvas.create_line(x0, cy, x1, cy, width=data.lineWidth)  # horizontal line


def mousePressed(event, data):
    pass


# use up/down arrow keys to adjust level
def keyPressed(event, data):
    if(event.keysym == "Up"):
        data.level += 1

    elif(event.keysym == "Down" and data.level > 0):
        data.level -= 1


def timerFired(data):
    pass


# update h-fractal based on level
def redrawAll(canvas, data):
    createHFractal(data, canvas, data.cx, data.cy, data.vLine, data.hLine, 
        data.level)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def hFractal():
    run(600, 600)

hFractal()

