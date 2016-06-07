# hw7s.py
# Edward Shin
# edwardsh
# Section A

from tkinter import *

####################################
# Dots and Boxes
####################################

def init(data):
    data.totalBoxes = (data.rows - 1) * (data.cols - 1)
    data.margin = 100
    data.gridWidth = data.width - (data.margin)
    data.gridHeight = data.height - (data.margin)
    data.space = data.gridWidth / data.cols     # distance between dots
    data.radius = 8
    data.dots = []
    data.lineWidth = 5
    data.lines = []

    # the player's boxes are stored by their top left (row, col)
    data.redBoxes = []  
    data.blueBoxes = []

    # previously clicked (row, col); currently set to "nothing"
    data.selection = (-1, -1) 
    data.playerTurn = "red"
    data.playerTurnBoxes = data.redBoxes
    data.timerCount = 1
    data.isGameOver = False


# connect the dots with mousePressed
def mousePressed(event, data):
    (row, col) = getDot(data, event.x, event.y)

    if(data.selection == (row, col)):
        data.selection = (-1, -1)
    else:
        if(data.selection == (-1, -1)):
            data.selection = (row, col)

        elif(data.selection != (-1, -1) and (row, col) != (-1, -1)):
            # if a new line is added and a new box is NOT added,
            # change the player's turn and reset timer
            if(addLine(data, row, col, data.playerTurn) and not 
                addBox(data, data.playerTurnBoxes)):

                changePlayerTurn(data)
                data.timerCount = 0

            data.selection = (-1, -1)


def keyPressed(event, data):
    if(event.char == "r" or event.char == "R"):
        init(data)


# when time is up, the player's turn is changed and the timer resets
def timerFired(data):
    if(not data.isGameOver):
        data.timerCount += 1
        if(data.timerCount == data.timeLimit + 1):
            changePlayerTurn(data)
            data.timerCount = 0
            data.selection = (-1, -1)


#change player's turn and box by their color
def changePlayerTurn(data):
    if(data.playerTurn == "red"):
        data.playerTurn = "blue"
        data.playerTurnBoxes = data.blueBoxes

    elif(data.playerTurn == "blue"):
        data.playerTurn = "red"
        data.playerTurnBoxes = data.redBoxes


# get the (row, col) of dot if selected
def getDot(data, x, y):
    for dot in data.dots:
        r = data.radius
        row = dot[0]
        col = dot[1]
        cx = data.margin + col * data.space
        cy = data.margin + row * data.space
        if((cx - r <= x <= cx + r)  and (cy - r <= y <= cy + r)):
            return (row, col)
    return (-1, -1)


# set (row, col)'s for the dots
def setDots(data):
    for row in range(data.rows):
        for col in range(data.cols):
            data.dots += [(row, col)]


# draw dots from dots list made by setDots
def drawDots(canvas, data):
    for dot in data.dots:
        r = data.radius
        cx = data.margin + dot[1] * data.space
        cy = data.margin + dot[0] * data.space
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="black")



# checks if line is legal (not diagonal line)
def isLegalLine(data, row, col):
    dirs = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]  #only digaonal directions

    for d in dirs:
        dRow = d[0]
        dCol = d[1]
        sRow = data.selection[0]
        sCol = data.selection[1]
        if((row, col) == (sRow + dRow, sCol + dCol)):
            return False

    return True

# adds line when mouse is clicked, line is legal(not diagonal or not used)
def addLine(data, row, col, playerTurn):
    lineSets = []

    # making a list of sets of (row, col)'s of lines so there is no worry of 
    # order or color. the reason it's not initially in sets for the main list 
    # is beacuse indexes cannot be used inside sets
    for line in data.lines:
        lineSets += [set([line[0], line[1]])]

    possibleLine = [(data.selection), (row, col), playerTurn]

    if(data.selection != (-1, -1) and (row, col) != (-1, -1) and 
        isLegalLine(data, row, col) and 
        (set([possibleLine[0], possibleLine[1]]) not in lineSets)):

        data.lines += [possibleLine]
        return True  # True if line is added

    return False  # False if line is not added


# draw and color lines from line list
def drawLines(canvas, data):
    for line in data.lines:
        x1 = data.margin + line[0][1] * data.space
        y1 = data.margin + line[0][0] * data.space
        x2 = data.margin + line[1][1] * data.space
        y2 = data.margin + line[1][0] * data.space
        color = line[2]
        canvas.create_line(x1, y1, x2, y2, fill=color, width=data.lineWidth)


# checks for legal boxes by finding four side satrting from top left corners
def isLegalBox(data, row, col):
    vertices = [(row, col), (row, col+1), (row+1, col+1), (row+1, col)]
    lineSets = []

    # making a list of sets of (row, col)'s of lines so there is no worry of 
    # order or color. the reason it's not initially in sets for the main list 
    #is beacuse I cannot use indexes with sets
    for line in data.lines:
        lineSets += [set([line[0], line[1]])]

    for index in range(len(vertices)):
        nextIndex = (index + 1) % len(vertices)
        curVertex = vertices[index]
        nextVertex = vertices[nextIndex]
        if(set([curVertex, nextVertex]) not in lineSets):
            return False

    return True


# add box to either player's list when there are isLegalBox is confirmed
def addBox(data, playerBoxes):
    # since we check for boxes by top left corner, rows and cols are reduced by
    # one since you cannot make box by top left corner at right and bottom edges

    for row in range(data.rows - 1):
        for col in range(data.cols - 1):
            if(isLegalBox(data, row, col) and ((row, col, "blue") 
                not in data.blueBoxes) and ((row, col, "red") 
                not in data.redBoxes)):

                playerBoxes += [(row, col, data.playerTurn)]
                return True   # True if box is added

    return False   # False if Box is not added  


#draw boxes that individual players won
def drawBoxes(canvas, data, playerBoxes):
    for box in playerBoxes:
        m = 10     # margin to make box smaller
        x1 = data.margin + box[1] * data.space
        y1 = data.margin + box[0] * data.space
        x2 = x1 + data.space
        y2 = y1 + data.space
        color = box[2]
        canvas.create_rectangle(x1 + m, y1 + m, x2 - m, y2 - m, fill=color)


# scoreboard displaying scores, timer, and turn
def drawScoreBoard(canvas, data):
    offset1 = 30   # offsets from edges for texts
    offset2 = 50

    canvas.create_text(data.margin, offset1, 
        text="Red Player: " + str(len(data.redBoxes)), font="Heletiva 14 bold")
    canvas.create_text(data.width - data.margin, offset1, 
        text="BluePlayer: " + str(len(data.blueBoxes)), font="Heletiva 14 bold")
    canvas.create_text(data.width/2, offset1, text=data.timerCount)
    canvas.create_text(data.width/2, offset2, 
        text="Turn: " + str(data.playerTurn))

# flash whenever the timelimit occurs; simply draw a white rectangle
def flash(canvas, data):
    m = 10      # margin to completely fill the window
    if(data.timerCount == data.timeLimit):
        canvas.create_rectangle(0, 0, data.width+m, data.height+m, fill="white")


# if all squares are filled, the game is over
def sayGameOver(canvas, data):
    if(len(data.redBoxes) + len(data.blueBoxes) == data.totalBoxes):
        data.isGameOver = True
        canvas.create_text(data.width/2, data.height/2, text="GAME OVER", 
            fill="purple", font="Heletiva 32 bold")


def redrawAll(canvas, data):
    setDots(data)
    drawScoreBoard(canvas, data)
    drawLines(canvas, data)
    drawDots(canvas, data)
    drawBoxes(canvas, data, data.redBoxes)
    drawBoxes(canvas, data, data.blueBoxes)
    flash(canvas, data)
    sayGameOver(canvas, data)


####################################
# use the run function as-is
####################################

def run(width, height, rows, cols, maxSecondsPerTurn):
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
    data.rows = rows
    data.cols = cols
    data.timeLimit = maxSecondsPerTurn
    data.timerDelay = 1000 # milliseconds
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

#run()

def playDotsAndBoxes(rows, cols, maxSecondsPerTurn):
    width = 600
    height = 600
    run(width, height, rows, cols, maxSecondsPerTurn)

playDotsAndBoxes(5, 5, 15)
