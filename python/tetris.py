# hw7c.py
# Edward Shin
# edwardsh
# Section A

# Collaborated with
# Seph Xiao
# wenxinx

import random
import copy
from tkinter import *

####################################
# Tetris
####################################

def init(data):
    data.emptyColor = "blue"
    data.board = [([data.emptyColor] * data.cols) for row in range(data.rows)]
    data.iPiece = [[True, True, True, True]]
    data.jPiece = [[True, False, False], [True,  True, True ]]
    data.lPiece = [[False, False, True], [True,  True,  True]]
    data.oPiece = [[True, True], [True, True]]
    data.sPiece = [[False, True,  True], [True,  True, False]]
    data.tPiece = [[False, True, False], [True,  True,  True]]
    data.zPiece = [[True,  True, False], [False, True, True]]
    data.tetrisPieces = [data.iPiece, data.jPiece, data.lPiece, data.oPiece, 
        data.sPiece, data.tPiece, data.zPiece]
    data.tetrisColors = ["red", "yellow", "magenta", "pink", "cyan", "green", 
        "orange"]
    data.isGameOver = False
    data.isPaused = False
    data.score = 0
    newFallingPiece(data)


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    if(not data.isPaused):
        if(event.keysym == "Down"):
            moveFallingPiece(data, +1, 0)
        elif(event.keysym == "Left"):
            moveFallingPiece(data, 0, -1)
        elif(event.keysym == "Right"):
            moveFallingPiece(data, 0, +1)
        elif(event.keysym == "Up"):
            rotateFallingPiece(data)
    #to reset game
    if(event.char == "r" or event.char == "R"):
        init(data)

    #to pause game
    if((event.char == "p" or event.char == "P") and not data.isGameOver):
        if(data.isPaused):
            data.isPaused = False
        else:
            data.isPaused = True


def timerFired(data):
    if(not data.isGameOver and not data.isPaused):
        if(moveFallingPiece(data, +1, 0) == False):
            placeFallingPiece(data)
            removeFullRows(data)
            newFallingPiece(data)
            if(not fallingPieceIsLegal(data)):
                data.isGameOver = True


# reference to grid-demo.py
# https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#gridDemo
def getCellBounds(data, row, col):
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    x1 = data.margin + gridWidth * col / data.cols
    y1 = data.margin + gridHeight * row / data.rows
    x2 = data.margin + gridWidth * (col+1) / data.cols
    y2 = data.margin + gridHeight * (row+1) / data.rows
    return (x1, y1, x2, y2)


# draw the board an pieces for the game
# some reference to tutorial
# https://www.cs.cmu.edu/~112/notes/notes-tetris/tetris-after-step-2.py
def drawGame(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)


# draw the Tetris Board
# some reference to tutorial
# https://www.cs.cmu.edu/~112/notes/notes-tetris/tetris-after-step-2.py
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(canvas, data, row, col, color)


# draw the Tetris Board cell
# some reference to tutorial
# https://www.cs.cmu.edu/~112/notes/notes-tetris/tetris-after-step-2.py
def drawCell(canvas, data, row, col, color):
    (x1, y1, x2, y2) = getCellBounds(data, row, col)
    m = 1      #margin for colored boxes
    canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    canvas.create_rectangle(x1 + m, y1 + m, x2 - m, y2 - m, 
        fill=color)


# set variables for new falling piece
def newFallingPiece(data):
    data.numPieces = len(data.tetrisPieces)
    data.newPieceIndex = random.randint(0, data.numPieces - 1)
    data.newPiece = data.tetrisPieces[data.newPieceIndex]
    data.newPieceRows = len(data.newPiece)
    data.newPieceCols = len(data.newPiece[0])
    data.newPieceColor = data.tetrisColors[data.newPieceIndex]
    data.newPieceRow = 0
    data.newPieceCol = data.cols // 2 - data.newPieceCols // 2


#draw current falling piece
def drawFallingPiece(canvas, data):
    startRow = data.newPieceRow
    startCol = data.newPieceCol 
    color = data.newPieceColor

    for row in range(data.newPieceRows):
        for col in range(data.newPieceCols):
            if(data.newPiece[row][col] == True):
                r = startRow + row
                c = startCol + col
                drawCell(canvas, data, r, c, color)


# move falling piece based on given drow and dcol
def moveFallingPiece(data, drow, dcol):
    data.newPieceRow += drow
    data.newPieceCol += dcol
    if(not fallingPieceIsLegal(data)):
        data.newPieceRow -= drow
        data.newPieceCol -= dcol
        return False

    return True


# rotate falling piece
def rotateFallingPiece(data):
    oldRows = len(data.newPiece); oldCols = len(data.newPiece[0])
    newRows = oldCols; newCols = oldRows
    oldRow = data.newPieceRow; oldCol = data.newPieceCol
    centerRow = oldRow + data.newPieceRows // 2
    centerCol = oldCol + data.newPieceCols // 2
    newRow = centerRow - newRows // 2
    newCol = centerCol - newCols // 2
    oldPiece = data.newPiece
    newPiece = [[None] * newCols for row in range(newRows)]
    for row in range(newRows):
        for col in range(newCols):
            newPiece[row][col] = oldPiece[col][oldCols - row - 1]
    data.newPieceRow = newRow
    data.newPieceCol = newCol
    data.newPieceRows = newRows
    data.newPieceCols = newCols
    data.newPiece = newPiece
    if(not fallingPieceIsLegal(data)):
        data.newPieceRow = oldRow
        data.newPieceCol = oldCol
        data.newPieceRows = oldRows
        data.newPieceCols = oldCols
        data.newPiece = oldPiece


#check if the falling piece can move
def fallingPieceIsLegal(data):
    for row in range(data.newPieceRows):
        for col in range(data.newPieceCols):
            r = data.newPieceRow + row
            c = data.newPieceCol + col

            # is the piece in the board
            if(r < 0 or r >= data.rows or c < 0 or c >= data.cols):
                return False
            
            # is any part of the piece in an empty spot
            if(data.board[r][c] != data.emptyColor and 
                data.newPiece[row][col] == True):
                return False

    return True


# set the piece colors onto the board when it could no longer move
def placeFallingPiece(data):
    for row in range(data.newPieceRows):
        for col in range(data.newPieceCols):
            if(data.newPiece[row][col] == True):
                r = data.newPieceRow + row
                c = data.newPieceCol + col
                data.board[r][c] = data.newPieceColor


# remove Rows when there it is full
def removeFullRows(data):
    newBoard = []
    newRow = 0
    fullRows = 0

    for oldRow in reversed(range(data.rows)):
        colorCount = 0  #number of times a colored Box occurs per row

        for col in range(data.cols):
            if(data.board[oldRow][col] == data.emptyColor):
                newBoard.insert(newRow, copy.deepcopy(data.board[oldRow]))
                break
            colorCount += 1
        
        if(colorCount == data.cols):
            fullRows += 1

    for row in range(fullRows):
        newBoard.insert(0, [data.emptyColor] * data.cols)

    data.board = newBoard
    data.score += fullRows**2


# record socre
def drawScoreBoard(canvas, data):
    offset1 = 0.15 * data.width
    offset2 = 0.05 * data.height 
    canvas.create_text(offset1, offset2, 
        text="Score: " + str(data.score), font="Heletiva 14 bold")
        

# say game over when no more pieces can fall
def sayGameOver(canvas, data):
    if(data.isGameOver):
        canvas.create_text(data.width/2, data.height/2, fill="white",
            text="GAME OVER", font="Heletiva 28 bold")

# say paused when game is...well...paused
def sayPaused(canvas, data):
    if(data.isPaused):
        canvas.create_text(data.width/2, data.height/2, fill="white",
            text="Paused", font="Heletiva 20 bold")


def redrawAll(canvas, data):
    drawGame(canvas, data)
    drawScoreBoard(canvas, data)
    sayPaused(canvas, data)
    sayGameOver(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=30, height=300, rows=15, cols=15, margin=30):
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
    data.margin = margin
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

def playTetris():
    rows = 15
    cols = 10
    margin = 40
    cellSize = 30
    width = 2 * margin + cols * cellSize
    height = 2 * margin + rows * cellSize
    run(width, height, rows, cols, margin)

playTetris()
