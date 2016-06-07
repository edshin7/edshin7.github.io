# hw6.py
# Edward Shin
# edwardsh
# Section A

import math

from tkinter import *

####################################
# Othello
####################################

def othelloInit(data):
    data.boardN = 8
    data.squareSize = 60
    data.boardSize = data.boardN * data.squareSize
    data.startX = data.startY = 60
    data.endX = data.endY = data.startX + data.boardSize
    data.radius = 20
    data.player1Spots = [(3, 3), (4, 4)]   # starting spots for player 1
    data.player2Spots = [(4, 3), (3, 4)]   # starting spots for player 2
    data.playerTurn = "1"


def othelloMousePressed(event, data):
    # confirm square and return (row, column)
    if(getSquare(data, event.x, event.y) != (None, None)):
        (row, col) = getSquare(data, event.x, event.y)

        # checks if there are any possible moves
        if(len(squareMoves(data, row, col, data.playerTurn)) > 0):
            dirList = squareMoves(data, row, col, data.playerTurn)
            makeMove(data, row, col, data.playerTurn, dirList)



def othelloKeyPressed(event, data):
    # use event.char and event.keysym
    pass


def othelloTimerFired(data):
    pass


# draw the board
def drawBoard(canvas, data):
    for row in range(data.boardN):
        for col in range(data.boardN):
            leftX = data.startX + row * data.squareSize
            topY = data.startY + col * data.squareSize
            rightX = leftX + data.squareSize
            bottomY = topY + data.squareSize
            canvas.create_rectangle(leftX, topY, rightX, bottomY)

# checks if (x, y) is within othello grid
# reference to grid demo
# https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#gridDemo
def pointInGrid(data, x, y):
    margin = data.startX
    return((margin <= x <= data.width - margin) and 
        (margin <= y <= data.height - margin))


# finds the row and column based on x, y location
# reference to grid demo
# https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#gridDemo
def getSquare(data, x, y):
    if(not pointInGrid(data, x, y)):
        return (None, None)

    margin = data.startX
    gridWidth = data.width - 2 * margin
    gridHeight = data.height - 2 * margin
    cellWidth = cellHeight = data.squareSize
    row = (y - margin) // cellHeight
    col = (x - margin) // cellWidth

    return (row, col)


# from selected spot, find all the possible moves and return list of directions
# reference text version of Othello
# https://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html#othello
def squareMoves(data, row, col, playerTurn):
    numDir = 8
    dirList = []
    
    # prevents search on occupied spaces
    if(((row, col) in data.player1Spots) or ((row, col) in data.player2Spots)):
        return dirList
    
    for direct in range(numDir):
        if(squareHasMoveInDir(data, row, col, data.playerTurn, direct)):
            dirList += [direct]
    return dirList


# determines possible moves in all 8 directions
# reference text version of othello
# https://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html#othello
def squareHasMoveInDir(data, row, col, playerTurn, direct):
    dirs = [(-1, -1), (-1, 0), (-1, +1),
            (0,  -1),          ( 0, +1),
            (+1, -1), (+1, 0), (+1, +1)]

    (drow, dcol) = dirs[direct]
    rows = cols = data.boardN
    pieces = 1

    if(playerTurn == "1"):
        playerSpots = data.player1Spots
        opponentSpots = data.player2Spots
    else:
        playerSpots = data.player2Spots
        opponentSpots = data.player1Spots

    while(True):
        newRow = row + pieces * drow
        newCol = col + pieces * dcol
        # must be within boundary
        if((newRow < 0) or (newRow >= rows) or (newCol < 0) or 
            (newCol >= cols)):  return False
        
        # no possible move if there is no piece to check
        elif(((newRow, newCol) not in playerSpots) and 
            ((newRow, newCol) not in opponentSpots)):  return False
        
        #reached end of line
        elif((newRow, newCol) in playerSpots):  break
        
        # another spot captured
        else: pieces += 1

    return (pieces > 1)


# makes move from list of possible directions
# reference to text version of Othello
# https://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html#othello
def makeMove(data, row, col, playerTurn, dirList):
    if(data.playerTurn == "1"):
        playerSpots = data.player1Spots
    else:
        playerSpots = data.player2Spots

    for direct in dirList:
        if(squareHasMoveInDir(data, row, col, data.playerTurn, direct)):
            makeMoveInDir(data, data.playerTurn, row, col, direct)
    
    playerSpots += [(row, col)]
    
    #change player's turn once move is complete. bring it on
    if(data.playerTurn == "1"):
        data.playerTurn = "2"
    else:
        data.playerTurn = "1"


# move in any possible direction
# reference to text version of Othello
# https://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html#othello
def makeMoveInDir(data, playerTurn, row, col, direct):
    dirs = [(-1, -1), (-1, 0), (-1, +1),
            (0,  -1),          ( 0, +1),
            (+1, -1), (+1, 0), (+1, +1)]

    (drow, dcol) = dirs[direct]
    rows = cols = data.boardN
    pieces = 1

    if(playerTurn == "1"):
        playerSpots = data.player1Spots
        opponentSpots = data.player2Spots
    else:
        playerSpots = data.player2Spots
        opponentSpots = data.player1Spots

    while(True):
        newRow = row + pieces * drow
        newCol = col + pieces * dcol
        
        #reached end of line
        if((newRow, newCol) in playerSpots):
            break
        
        # another spot captured
        else:
            opponentSpots.remove((newRow, newCol))
            playerSpots += [(newRow, newCol)]
            pieces += 1


# update board to reflect the player's move (adding and stealing spaces)
def updateSpots(canvas, data, playerSpots):
    color = "white"
    if(playerSpots == data.player2Spots):
        color = "black"

    for spot in playerSpots:
        cx = data.startX + spot[1] * data.squareSize + data.squareSize / 2
        cy = data.startY + spot[0] * data.squareSize + data.squareSize / 2
        rad = data.radius
        canvas.create_oval(cx - rad, cy - rad, cx + rad, cy + rad, fill=color)


# score board and turn label for othello
def updateScore(canvas, data):
    sideOffset = 200
    heightOffset = 20
    canvas.create_text((data.width / 2) - sideOffset, heightOffset, 
        text="White Player 1: " + str(len(data.player1Spots)), 
        font="Heletiva 14")
    canvas.create_text((data.width / 2) + sideOffset, heightOffset,
        text="Black Player 2: " + str(len(data.player2Spots)), 
        font="Heletiva 14")
    canvas.create_text((data.width / 2), heightOffset * 2,
        text="Turn: Player " + data.playerTurn, font="Heletiva 14")


# checks if board is filled. if so, GAME OVER!
def isGameOver(canvas, data):
    if(len(data.player1Spots) + len(data.player2Spots) == data.boardN**2):
        canvas.create_text(data.width / 2, data.height / 2, text="Game Over", 
            fill="red", font="Heletiva 28 bold")


def othelloRedrawAll(canvas, data):
    drawBoard(canvas, data)
    updateSpots(canvas, data, data.player1Spots)
    updateSpots(canvas, data, data.player2Spots)
    updateScore(canvas, data)
    isGameOver(canvas, data)

####################################
# run function for Othello
####################################

def runOthello(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        othelloRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        othelloMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        othelloKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        othelloTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    othelloInit(data)
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

runOthello()
