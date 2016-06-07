# hw6.py
# Edward Shin
# edwardsh
# Section A

import math

from tkinter import *

####################################
# FancyWheels
####################################

def fancyWheelsInit(data):
    data.n = 5
    data.startVertexNum = 4
    data.radius = (data.width / data.n) / 2
    data.steps = 0
    data.stepSize = 10    # degrees for rotation
    data.startCX = data.radius
    data.startCY = data.radius
    data.startRed = 0
    data.startGreen = 255

def fancyWheelsMousePressed(event, data):
    pass

def fancyWheelsKeyPressed(event, data):
    if(event.keysym == "Up" or event.keysym == "Right"):
        data.n += 1
        data.radius = (data.width / data.n) / 2
        data.startCX = data.radius
        data.startCY = data.radius
    elif((event.keysym == "Down" or event.keysym == "Left") and data.n > 1):
        data.n -= 1
        data.radius = (data.width / data.n) / 2
        data.startCX = data.radius
        data.startCY = data.radius


def fancyWheelsTimerFired(data):
    data.steps += data.stepSize


# set the coordinates for drawing polygons
def setPolygons(canvas, data):
    vertexNum = data.startVertexNum
    rValue = data.startRed
    gValue = data.startGreen
    changeValue = 255 / data.n
    direct = 1   # direction of rotation

    for row in range(data.n):
        for col in range(data.n):
            tempVertexNum = vertexNum + col
            cx = data.startCX + row * (data.radius * 2)
            cy = data.startCY + col * (data.radius * 2)

            #set color based on position
            color = "#%02x%02x%02x" % (rValue, gValue, 0)

            #set direction of rotation
            if((row + col) % 2 == 0):
                direct = 1
            elif((row + col) % 2 == 1):
                direct = -1
            drawPolygon(canvas, data, tempVertexNum, cx, cy, color, direct)
            rValue += changeValue

        vertexNum += 1
        gValue -= changeValue
        rValue = data.startRed


# draw polygons based on information from data and setPolygons
def drawPolygon(canvas, data, vertexNum, cx, cy, color, direct):
    vertices = []
    
    # determining vertices
    for point in range(vertexNum):
        angle = 360 / vertexNum     #360 is the total degrees within a circle
        x = cx + (data.radius * math.cos(math.radians(angle) * point + 
            direct * math.radians(data.steps)))
        y = cy + (data.radius * math.sin(math.radians(angle) * point + 
            direct * math.radians(data.steps)))
        vertices += [(x, y)]
    
    #creating the shape
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            x1 = vertices[i][0]
            y1 = vertices[i][1]
            x2 = vertices[j][0]
            y2 = vertices[j][1]
            canvas.create_line(x1, y1, x2, y2, fill=color)


def fancyWheelsRedrawAll(canvas, data):
    setPolygons(canvas, data)

####################################
# run function for FancyWheels
####################################

def runFancyWheels(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        fancyWheelsRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        fancyWheelsMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        fancyWheelsKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        fancyWheelsTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    fancyWheelsInit(data)
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

runFancyWheels()
