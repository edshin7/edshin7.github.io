# 15-112 Term Project 2016

# Edward Shin
# edwardsh
# Section A
# April 28, 2016

# Edge (2008) | Final Phase


from tkinter import *
import math
import os


# almostEqual provided by this link
# https://www.cs.cmu.edu/~112/notes/notes-data-and-exprs.html
def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)


# Classes for game components

# mainly gives the dimensions and corners for the square
class Square(object):
    def __init__(self, x, y):
        self.size = 40
        self.x1 = x          # top left x,y
        self.y1 = y
        self.x2 = self.x1 + self.size   # top right x,y
        self.y2 = self.y1
        self.x3 = self.x1          # bottom left x,y
        self.y3 = self.y1 + self.size
        self.x4 = self.x1 + self.size   # bottom right x,y
        self.y4 = self.y1 + self.size


# player class that inherits Square properties
class PlayerSquare(Square):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.startX = x  # start x,y of a level
        self.startY = y

        self.lineW = 3
        self.outlineColor = "Black"
        self.baseAngle = 0
        self.gravity = 10
        self.lives = 2
        self.score = 0


    # rotating the square from its bottom right corner
    def turnRight(self, angle): 
        angle = math.radians(angle)
        self.baseAngle += angle

        self.x1 = self.x4 - (self.size * (2**0.5) * math.cos(math.radians(45) 
            + self.baseAngle))
        self.y1 = self.y4 - (self.size * (2**0.5) * math.sin(math.radians(45) 
            + self.baseAngle))
        self.x2 = self.x4 - (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y2 = self.y4 - (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x3 = self.x4 - (self.size * math.cos(self.baseAngle))
        self.y3 = self.y4 - (self.size * math.sin(self.baseAngle))

    
    # rotating the SQuare from its bottom left corner
    def turnLeft(self, angle):
        angle = math.radians(angle)
        self.baseAngle -= angle

        self.x4 = self.x3 + (self.size * math.cos(self.baseAngle))
        self.y4 = self.y3 + (self.size * math.sin(self.baseAngle))
        self.x1 = self.x3 + (self.size * math.cos(math.radians(-90) 
            + self.baseAngle))
        self.y1 = self.y3 + (self.size * math.sin(math.radians(-90) 
            + self.baseAngle))
        self.x2 = self.x3 + (self.size * (2**0.5) * math.cos(math.radians(-45) 
            + self.baseAngle))
        self.y2 = self.y3 + (self.size * (2**0.5) * math.sin(math.radians(-45) 
            + self.baseAngle))


    # rotating the square from its top right corner
    def turnUpRight(self, angle):
        angle = math.radians(angle)
        self.baseAngle += angle

        self.x1 = self.x2 - (self.size * math.cos(self.baseAngle))
        self.y1 = self.y2 - (self.size * math.sin(self.baseAngle))
        self.x4 = self.x2 + (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y4 = self.y2 + (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x3 = self.x2 + (self.size * (2**0.5) * math.cos(math.radians(135) 
            + self.baseAngle))
        self.y3 = self.y2 + (self.size * (2**0.5) * math.sin(math.radians(135) 
            + self.baseAngle))


    # rotating the square from its top left corner
    def turnUpLeft(self, angle):
        angle = math.radians(angle)
        self.baseAngle -= angle

        self.x2 = self.x1 + (self.size * math.cos(self.baseAngle))
        self.y2 = self.y1 + (self.size * math.sin(self.baseAngle))
        self.x3 = self.x1 + (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y3 = self.y1 + (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x4 = self.x1 + (self.size * (2**0.5) * math.cos(math.radians(45) 
            + self.baseAngle))
        self.y4 = self.y1 + (self.size * (2**0.5) * math.sin(math.radians(45) 
            + self.baseAngle))


    def resetBaseAngle(self):
        self.baseAngle = 0


    # reset corners to original setting
    def resetCorners(self, direction):
        tempX1 = self.x1
        tempY1 = self.y1
        tempX2 = self.x2
        tempY2 = self.y2
        tempX3 = self.x3
        tempY3 = self.y3
        tempX4 = self.x4
        tempY4 = self.y4
        temps = [(tempX1, tempY1), (tempX2, tempY2), (tempX3, tempY3), 
                 (tempX4, tempY4)]
        if(direction == "Right"):
            self.resetAtRight(temps)
        elif(direction == "Left"):
            self.resetAtLeft(temps)
        elif(direction == "Up Right"):
            self.resetAtUpRight(temps)
        elif(direction == "Up Left"):
            self.resetAtUpLeft(temps)
        elif(direction == "Up Right Wall"):
            self.resetAtUpRightWall(temps)
        elif(direction == "Up Left Wall"):
            self.resetAtUpLeftWall(temps)


    # reset orignal x,y positions based on direction of rotation upon completion
    def resetAtRight(self, temps):
        (self.x1, self.y1) = temps[2]
        (self.x2, self.y2) = temps[0]
        (self.x3, self.y3) = temps[3]
        (self.x4, self.y4) = temps[1]


    def resetAtLeft(self, temps):
        (self.x1, self.y1) = temps[1]
        (self.x2, self.y2) = temps[3]
        (self.x3, self.y3) = temps[0]
        (self.x4, self.y4) = temps[2]


    def resetAtUpRight(self, temps):
        (self.x1, self.y1) = temps[3]
        (self.x2, self.y2) = temps[2]
        (self.x3, self.y3) = temps[1]
        (self.x4, self.y4) = temps[0]

    
    # reset if square moving up right into a wall
    def resetAtUpRightWall(self, temps):
        (self.x1, self.y1) = temps[2]
        (self.x2, self.y2) = temps[0]
        (self.x3, self.y3) = temps[3]
        (self.x4, self.y4) = temps[1]


    def resetAtUpLeft(self, temps):
        (self.x1, self.y1) = temps[3]
        (self.x2, self.y2) = temps[2]
        (self.x3, self.y3) = temps[1]
        (self.x4, self.y4) = temps[0]

    
    # reset if square moving up left into a wall
    def resetAtUpLeftWall(self, temps):
        (self.x1, self.y1) = temps[1]
        (self.x2, self.y2) = temps[3]
        (self.x3, self.y3) = temps[0]
        (self.x4, self.y4) = temps[2]

    
    # fall as if acted upon by gravity
    def fall(self):
        self.y1 += self.gravity
        self.y2 += self.gravity
        self.y3 += self.gravity
        self.y4 += self.gravity

    # snap the corners of the player when standing still
    def snapGrid(self, direction, point):
        if(direction == "Right"):
            (self.x2, self.y2) = point
            (self.x1, self.y1) = (self.x2 - self.size, self.y2)
            (self.x3, self.y3) = (self.x2 - self.size, self.y2 + self.size)
            (self.x4, self.y4) = (self.x2, self.y2 + self.size)

        elif(direction == "Left"):
            (self.x1, self.y1) = point
            (self.x2, self.y2) = (self.x1 + self.size, self.y1)
            (self.x3, self.y3) = (self.x1, self.y1 + self.size)
            (self.x4, self.y4) = (self.x1 + self.size, self.y1 + self.size)

        elif(direction == "Down"):
            (self.x3, self.y3) = point[0]
            (self.x4, self.y4) = point[1]
            (self.x1, self.y1) = (self.x3, self.y3 - self.size)
            (self.x2, self.y2) = (self.x4, self.y4 - self.size)

    
    # snaps the point to a specific point when rotating the square
    def snapPoint(self, direction, point):
        if(direction == "Right"):
            self.snapAtRight(point)

        elif(direction == "Left"):
            self.snapAtLeft(point)

        elif(direction == "Down Right"):
            self.snapAtDownRight(point)

        elif(direction == "Down Left"):
            self.snapAtDownLeft(point)


    def snapAtRight(self, point):
        (self.x2, self.y2) = point
        self.x1 = self.x2 - (self.size * math.cos(self.baseAngle))
        self.y1 = self.y2 - (self.size * math.sin(self.baseAngle))
        self.x4 = self.x2 + (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y4 = self.y2 + (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x3 = self.x2 + (self.size * (2**0.5) * 
            math.cos(math.radians(135) + self.baseAngle))
        self.y3 = self.y2 + (self.size * (2**0.5) * 
            math.sin(math.radians(135) + self.baseAngle))


    def snapAtLeft(self, point):
        (self.x1, self.y1) = point
        self.x2 = self.x1 + (self.size * math.cos(self.baseAngle))
        self.y2 = self.y1 + (self.size * math.sin(self.baseAngle))
        self.x3 = self.x1 + (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y3 = self.y1 + (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x4 = self.x1 + (self.size * (2**0.5) * 
            math.cos(math.radians(45) + self.baseAngle))
        self.y4 = self.y1 + (self.size * (2**0.5) * 
            math.sin(math.radians(45) + self.baseAngle))


    def snapAtDownRight(self, point):
        (self.x4, self.y4) = point
        self.x1 = self.x4 - (self.size * (2**0.5) * 
            math.cos(math.radians(45) + self.baseAngle))
        self.y1 = self.y4 - (self.size * (2**0.5) * 
            math.sin(math.radians(45) + self.baseAngle))
        self.x2 = self.x4 - (self.size * math.cos(math.radians(90) 
            + self.baseAngle))
        self.y2 = self.y4 - (self.size * math.sin(math.radians(90) 
            + self.baseAngle))
        self.x3 = self.x4 - (self.size * math.cos(self.baseAngle))
        self.y3 = self.y4 - (self.size * math.sin(self.baseAngle))


    def snapAtDownLeft(self, point):
        (self.x3, self.y3) = point
        self.x4 = self.x3 + (self.size * math.cos(self.baseAngle))
        self.y4 = self.y3 + (self.size * math.sin(self.baseAngle))
        self.x1 = self.x3 + (self.size * math.cos(math.radians(-90) 
            + self.baseAngle))
        self.y1 = self.y3 + (self.size * math.sin(math.radians(-90) 
            + self.baseAngle))
        self.x2 = self.x3 + (self.size * (2**0.5) * 
            math.cos(math.radians(-45) + self.baseAngle))
        self.y2 = self.y3 + (self.size * (2**0.5) * 
            math.sin(math.radians(-45) + self.baseAngle))


    # reset player to starting position
    def resetPlayer(self):
        (self.x1, self.y1) = (self.startX, self.startY)
        (self.x2, self.y2) = (self.x1 + self.size, self.y1)
        (self.x3, self.y3) = (self.x1, self.y1 + self.size)
        (self.x4, self.y4) = (self.x1 + self.size, self.y1 + self.size)


    # draw player's square
    def drawSquare(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, 
            fill=self.outlineColor, width=self.lineW)
        canvas.create_line(self.x2, self.y2, self.x4, self.y4, 
            fill=self.outlineColor, width=self.lineW)
        canvas.create_line(self.x1, self.y1, self.x3, self.y3, 
            fill=self.outlineColor, width=self.lineW)
        canvas.create_line(self.x3, self.y3, self.x4, self.y4, 
            fill=self.outlineColor, width=self.lineW)

        canvas.create_line(self.x1, self.y1, self.x4, self.y4, 
            fill=self.outlineColor)
        canvas.create_line(self.x2, self.y2, self.x3, self.y3, 
            fill=self.outlineColor)


# Square that could be an obstacle or ground for the player
class Block(Square): 
    def __init__(self, x, y, instructions):
        super().__init__(x, y)
        self.color = "DarkSlateGray"
        self.outlineColor = "White"

        self.direction = instructions[0]
        self.maxSteps = instructions[1]
        self.direct = instructions[2]
        self.step = 4 * self.direct
        self.numSteps = 0
        self.timer = 0
        self.maxTime = 20
        self.isMoving = False

    def drawBlock(self, canvas):
        if(self.maxSteps != None):
            self.color = "Steel Blue"

        canvas.create_rectangle(self.x1, self.y1, self.x4, self.y4, 
            fill=self.color, outline=self.outlineColor)


    # move the Block if any instructions were given
    def moveBlock(self):
        if(self.direction == "X"):
            self.moveXDir()

        elif(self.direction == "Y"):
            self.moveYDir()

    # move in X direction
    def moveXDir(self):
        if(self.numSteps == self.maxSteps):
            if(self.timer == self.maxTime):
                self.timer = 0
                self.numSteps = 0
                self.step *= -1
                self.isMoving = True

            else:
                self.isMoving = False
                self.timer+=1

        else:
            self.x1 += self.step
            self.x2 += self.step
            self.x3 += self.step
            self.x4 += self.step
            self.numSteps += 1

    
    # move in Y direction
    def moveYDir(self):
        if(self.numSteps == self.maxSteps):
            if(self.timer == self.maxTime):
                self.timer = 0
                self.numSteps = 0
                self.step *= -1

            else:
                self.timer+=1

        else:
            self.y1 -= self.step
            self.y2 -= self.step
            self.y3 -= self.step
            self.y4 -= self.step
            self.numSteps += 1


# finish box
class Finish(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.outlineColor = "Lime Green"
        self.lineWidth = 5
        self.points = 100

    def drawFinish(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x4, self.y4, fill=None, 
            outline=self.outlineColor, width=self.lineWidth)


# prizes to collect to increase score
class Prize(object):
    def __init__(self, x, y):
        self.size = 20
        self.x = x
        self.y = y
        self.x1 = self.x + self.size/2
        self.y1 = self.y + self.size/2
        self.x2 = self.x1 + self.size
        self.y2 = self.y1 + self.size
        self.color = "Hot Pink"
        self.outlineColor = "Medium Violet Red"
        self.outlineWidth = 3
        self.points = 10

    def drawPrize(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
            fill=self.color, outline=self.outlineColor, width=self.outlineWidth)


# trigger for activating various events
class Trigger(object):
    def __init__(self, x, y):
        self.size = 20
        self.x = x
        self.y = y
        self.x1 = self.x + self.size/2
        self.y1 = self.y + self.size/2
        self.x2 = self.x1 + self.size
        self.y2 = self.y1 + self.size
        self.color = "Red"
        self.outlineWidth = 3
        self.isOn = False

    def drawTrigger(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
            fill=self.color, width=self.outlineWidth)


# Splash Screen for introducing the game
class SplashScreen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = "Light Cyan"
        self.titleOffsetX = self.width//2
        self.titleOffsetY = 70
        self.title = "EDGE 2D"
        self.startOffsetX = self.width - 150
        self.startOffsetY = height - 350
        self.startMessage = "Press [W] to Play\nPress [A] for Help"
        
        #for background
        self.sqSize = 160
        self.sqColor = "DarkSlateGray"
        self.sqOutColor = "White"
        self.sqWidth = 10


    # drawing entire splash screen based on details
    def drawSplashScreen(self, canvas):
        self.drawDetails(canvas)


    # drawing details of the splash screen
    def drawDetails(self, canvas):
        canvas.create_rectangle(-2, -2, self.width+3, self.height+3, 
            fill=self.color)

        for i in range(self.height//self.sqSize + 1):
            canvas.create_rectangle(0, i*self.sqSize, self.sqSize, 
                (i + 1)*self.sqSize, fill=self.sqColor, outline=self.sqOutColor,
                width=2)

        for i in range(self.width//self.sqSize):
            canvas.create_rectangle(i*self.sqSize, 2*self.sqSize, 
                (i+1)*self.sqSize, 3*self.sqSize, fill=self.sqColor, 
                outline=self.sqOutColor, width=2)

        canvas.create_rectangle(self.sqSize, self.sqSize, 2*self.sqSize, 
            2*self.sqSize, fill=None, outline="Black", width=self.sqWidth)

        canvas.create_line(self.sqSize, self.sqSize, 2*self.sqSize, 
            2*self.sqSize, fill="Black", width=self.sqWidth)

        canvas.create_line(2*self.sqSize, self.sqSize, self.sqSize, 
            2*self.sqSize, fill="Black", width=self.sqWidth)

        canvas.create_text(self.titleOffsetX, self.titleOffsetY, 
            text=self.title, font="Helevetica 100 bold")

        canvas.create_text(self.startOffsetX, self.startOffsetY, 
            text=self.startMessage, font="Helevetica 20 bold")


# Level Panel for displaying what levels are unlocked
class LevelPanel(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = "Light Cyan"
        self.outlineColor = "Gray"
        self.titleOffsetX = width//2
        self.titleOffsetY = 60
        self.title = "LEVELS"
        self.messageOffsetX = width//2
        self.messageOffsetY = 140
        self.levelMessage = ("Press the Corresponding Number Key to Play\n" + 
                    "     [W] to Pause                            [A] for Help")

        self.startGridX = 250
        self.startGridY = 200
        self.spacing = 100
        self.rows = self.cols = 3
        self.lineWidth = 3


    # drawing entire level panel based on details
    def drawLevelPanel(self, canvas):
        self.drawDetails(canvas)

    # drawing details of level panel
    def drawDetails(self, canvas):
        canvas.create_rectangle(-2, -2, self.width+3, self.height+3, 
        fill=self.color)

        canvas.create_text(self.titleOffsetX, self.titleOffsetY, 
            text=self.title, font="Helevetica 40 bold")

        canvas.create_text(self.messageOffsetX, self.messageOffsetY, 
            text=self.levelMessage, font="Helevetica 20 bold")

        for row in range(self.rows):
            for col in range(self.cols):
                x1 = self.startGridX + self.spacing * col
                y1 = self.startGridY + self.spacing * row
                x2 = x1 + self.spacing
                y2 = y1 + self.spacing
                centerX = x1 + self.spacing//2
                centerY = y1 + self.spacing//2

                canvas.create_rectangle(x1, y1, x2, y2, fill=None, 
                    width=self.lineWidth, outline=self.outlineColor)

                canvas.create_text(centerX, centerY, text="?", 
                    fill=self.outlineColor, font="Helevetica 40 bold")


# squares in the level panel that show what levels are unlocked
class LevelSquare(object):
    def __init__(self, x, y, level):
        self.size = 100
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + self.size
        self.y2 = self.y1 + self.size
        self.centerX = self.x1 + self.size//2
        self.centerY = self.y1 + self.size//2
        self.level = level
        self.color = "Light Sky Blue"
        self.lineWidth = 4

    def drawLevelSquare(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
            fill=self.color, width=self.lineWidth)

        canvas.create_text(self.centerX, self.centerY, text=self.level, 
            font="Helevetica 30 bold")


# a menu shown when the game is paused
class Menu(object):
    def __init__(self, width, height):
        self.width = 3 * width // 4
        self.height = 3 * height // 4
        self.x1 = width//2 - self.width//2
        self.y1 = height//2 - self.height//2
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.color = "Light Blue"

        self.title = "PAUSED"
        self.titleX = width//2
        self.titleY = self.y1 + 30

        self.instructions = ("[W] to Exit\n\n[S] for Levels\n\n" + 
            "[A] for Help\n\n[D] to Resume")

        self.instX = width//2
        self.instY = self.titleY + 210

    def drawMenu(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
            fill=self.color, outline=self.color)

        canvas.create_text(self.titleX, self.titleY, text=self.title, 
            font="Helevetica 40 bold")

        canvas.create_text(self.instX, self.instY, text=self.instructions,
            font="Helevetica 35 bold")


# help screen that gives instructions and descriptions of game
class HelpScreen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = "Light Cyan"
        self.titleOffsetX = width//2
        self.titleOffsetY = 60
        self.title = "HELP"
        self.goalOffsetX = 20
        self.goalOffsetY = 120
        self.goalMessage = ("Goal:\nGuide the Square in Black outlines" + 
            " to the Green Goal")

        self.controlOffsetX = self.goalOffsetX
        self.controlOffsetY = self.goalOffsetY + 60
        self.controlMessage = "Collect Pink Squares to earn points."
        
        self.controlOffsetX2 = self.controlOffsetX
        self.controlOffsetY2 = self.controlOffsetY + 60
        self.controlMessage2 = ("Controls:\n[Left] and [Right]" + 
            " to move, climb, and balance\n\nPress [Left] or [Right]" + 
            "to keep the player's square moving or climbing\n\n" + 
            "Press and Release repeatedly to balance the square on a side edge."
            + "\nIt will be especially helpful for latching onto moving Blocks")

        self.exitOffsetX = width//2
        self.exitOffsetY = height - 50
        self.exitMessage = "[W] to Exit"

    # drawing entire level panel based on 
    def drawHelpScreen(self, canvas):
        self.drawDetails(canvas)

    # drawing details of level panel
    def drawDetails(self, canvas):
        canvas.create_rectangle(-2, -2, self.width+3, self.height+3, 
            fill=self.color)

        canvas.create_text(self.titleOffsetX, self.titleOffsetY, 
            text=self.title, font="Helevetica 80 bold")

        canvas.create_text(self.goalOffsetX, self.goalOffsetY, 
            text=self.goalMessage, font="Helevetica 20 bold", anchor=NW)

        canvas.create_text(self.controlOffsetX, self.controlOffsetY, 
            text=self.controlMessage, font="Helevetica 20 bold", anchor=NW)

        canvas.create_text(self.controlOffsetX2, self.controlOffsetY2, 
            text=self.controlMessage2, font="Helevetica 20 bold", anchor=NW)

        canvas.create_text(self.exitOffsetX, self.exitOffsetY, 
            text=self.exitMessage, font="Helevetica 20 bold")


#-----------------------------------------#

# tkinter animation code

def init(data):
    data.player = None
    data.addAng = 10   # angle for cube to rotate when moving
    
    # Gives the ok for moving in a certain direction
    data.rightMode = data.leftMode = False   
    data.upRightMode = data.upLeftMode = False

    # tells if player is in the middle of moving
    data.isRightMotion = data.isLeftMotion = False   
    data.isUpRightMotion = data.isUpLeftMotion = False

    data.playerFalling = False   # tells if player is falling
    data.playerPushed = False    # tells if player is pushed by another Block

    data.blocks = data.levelSquares = []
    data.prizes = data.triggers = []
    data.finish = None

    data.totalLevels = 9
    data.levels = set(["1"])
    data.currentLevel = 1
    
    data.deaths = 0
    data.pinkies = 0    # number of prizes collected
    data.score = 0
    
    data.splashIsOn = True
    data.levelPanelIsOn = data.menuIsOn = data.helpIsOn = False
    data.gameIsOn = False 

    data.screen = SplashScreen(data.width, data.height)
    data.levelPanel = LevelPanel(data.width, data.height)
    data.menu = Menu(data.width, data.height)
    data.helpScreen = HelpScreen(data.width, data.height)


# moving the player
def movePlayer(data):
    # checks if player is not stuck between two Blocks and not under a block
    if(not(checkPlayerLeft(data) != None and checkPlayerRight(data) != None) 
        and checkPlayerUp(data) == None):

        if(data.upRightMode == True):
            movePlayerUpRight(data)

        elif(data.upLeftMode == True):
            movePlayerUpLeft(data)

        if(data.rightMode == True):
            movePlayerRight(data)

        elif(data.leftMode == True):
            movePlayerLeft(data)
    


# move the player up right when there's a Block in front
def movePlayerUpRight(data):
    data.player.turnUpRight(data.addAng)
    
    # Check if there is another Block obstructing the path
    if(almostEqual(data.player.baseAngle, math.radians(90)) and
        checkPlayerUpRight(data) != None):

        data.player.resetCorners("Up Right Wall")
        data.player.resetBaseAngle()
        data.isUpRightMotion = False
        data.upRightMode = False

    elif(almostEqual(data.player.baseAngle, math.radians(180))):
        data.player.resetCorners("Up Right")
        data.player.resetBaseAngle()
        data.isUpRightMotion = False
        data.upRightMode = False


# move the player up left when there's a Block in front
def movePlayerUpLeft(data):
    data.player.turnUpLeft(data.addAng)
    
    # Check if there is another Block obstructing the path
    if(almostEqual(data.player.baseAngle, math.radians(-90)) and
        checkPlayerUpLeft(data) != None):

        data.player.resetCorners("Up Left Wall")
        data.player.resetBaseAngle()
        data.isUpLeftMotion = False
        data.upLeftMode = False


    elif(almostEqual(data.player.baseAngle, math.radians(-180))):
        data.player.resetCorners("Up Left")
        data.player.resetBaseAngle()
        data.isUpLeftMotion = False
        data.upLeftMode = False


# move the player to the right when there are no obstructing blocks
def movePlayerRight(data):
    data.player.turnRight(data.addAng)

    if (almostEqual(data.player.baseAngle, math.radians(90))):
        data.player.resetCorners("Right")
        data.player.resetBaseAngle()
        data.isRightMotion = False
        data.rightMode = False


# move the player to the left when there are no obstructing blocks
def movePlayerLeft(data):
    data.player.turnLeft(data.addAng)

    if (almostEqual(data.player.baseAngle, math.radians(-90)) ):
        data.player.resetCorners("Left")
        data.player.resetBaseAngle()
        data.isLeftMotion = False
        data.leftMode = False


# control player using the arrow keys
def controlPlayer(data, event):
    if(data.player != None):
        if(event.keysym == "Right" and not data.isLeftMotion and 
            not data.isUpLeftMotion):

            if(checkPlayerRight(data) != None and not data.upRightMode and 
                not data.playerFalling):
                
                data.upRightMode = True
                data.isUpRightMotion = True

            elif(not data.rightMode and not data.playerFalling):
                data.rightMode = True
                data.isRightMotion = True

        elif(event.keysym == "Left" and not data.isRightMotion and 
            not data.isUpRightMotion):

            if(checkPlayerLeft(data) != None and not data.upLeftMode and
                not data.playerFalling):

                data.upLeftMode = True
                data.isUpLeftMotion = True

            elif(not data.leftMode and not data.playerFalling):
                data.leftMode = True
                data.isLeftMotion = True


# player falls based on block conditions
def fallPlayer(data):
        if(checkPlayerDown(data) == None and closePlayerDown(data) == None and
            not data.isUpRightMotion and not data.isRightMotion and
            not data.isUpLeftMotion and not data.isLeftMotion):

            data.playerFalling = True
            data.player.fall()

        else:
            data.playerFalling = False


# reset player to normal position when soppinr rotation midway
def resetPlayer(data):
    if(data.isUpRightMotion and not data.upRightMode):
        resetWhenUpRight(data)

    elif(data.isUpLeftMotion and not data.upLeftMode):
        resetWhenUpLeft(data)

    elif(data.isRightMotion and not data.rightMode):
        resetWhenRight(data)

    elif(data.isLeftMotion and not data.leftMode):
        resetWhenLeft(data)

    
# reset player position when in the middle of moving right
def resetWhenRight(data):
    if(data.player.baseAngle < math.radians(45) and not 
        almostEqual(data.player.baseAngle, 0)):

        data.player.turnRight(-data.addAng)

        if(almostEqual(data.player.baseAngle, 0)):
            data.player.resetBaseAngle()
            data.isRightMotion = False
            data.isUpRightMotion = False

    elif(data.player.baseAngle >= math.radians(45) and not 
        almostEqual(data.player.baseAngle, math.radians(90))):

        data.player.turnRight(data.addAng)

        if (almostEqual(data.player.baseAngle, math.radians(90))):
            data.player.resetCorners("Right")
            data.player.resetBaseAngle()
            data.isRightMotion = False
            data.isUpRightMotion = False


# reset player position when in the middle of moving left
def resetWhenLeft(data):
    if(data.player.baseAngle > math.radians(-45) and not 
        almostEqual(data.player.baseAngle, 0)):

        data.player.turnLeft(-data.addAng)

        if(almostEqual(data.player.baseAngle, 0)):
            data.player.resetBaseAngle()
            data.isLeftMotion = False
            data.isUpLeftMotion = False

    elif(data.player.baseAngle <= math.radians(-45) and not 
        almostEqual(data.player.baseAngle, math.radians(-90))):

        data.player.turnLeft(data.addAng)

        if (almostEqual(data.player.baseAngle, math.radians(-90))):
            data.player.resetCorners("Left")
            data.player.resetBaseAngle()
            data.isLeftMotion = False
            data.isUpLeftMotion = False


# reset player position when in the middle of moving up right 
def resetWhenUpRight(data):
    if(data.player.baseAngle < math.radians(135) and not 
        almostEqual(data.player.baseAngle, 0)):

        data.player.turnUpRight(-data.addAng)

        if(almostEqual(data.player.baseAngle, 0)):
            data.player.resetBaseAngle()
            data.isRightMotion = False
            data.isUpRightMotion = False

    elif(data.player.baseAngle >= math.radians(135) and not 
        almostEqual(data.player.baseAngle, math.radians(180))):

        data.player.turnUpRight(data.addAng)

        if (almostEqual(data.player.baseAngle, math.radians(180))):
            data.player.resetCorners("Up Right")
            data.player.resetBaseAngle()
            data.isRightMotion = False
            data.isUpRightMotion = False


# reset player when in the middle of moving up left
def resetWhenUpLeft(data):
    if(data.player.baseAngle > math.radians(-135) and not 
        almostEqual(data.player.baseAngle, 0)):

        data.player.turnUpLeft(-data.addAng)

        if(almostEqual(data.player.baseAngle, 0)):
            data.player.resetBaseAngle()
            data.isLeftMotion = False
            data.isUpLeftMotion = False

    elif(data.player.baseAngle <= math.radians(-135) and not 
        almostEqual(data.player.baseAngle, math.radians(-180))):

        data.player.turnUpLeft(data.addAng)

        if (almostEqual(data.player.baseAngle, math.radians(-180))):
            data.player.resetCorners("Up Left")
            data.player.resetBaseAngle()
            data.isLeftMotion = False
            data.isUpLeftMotion = False



# check if there are any blocks under player
def checkPlayerDown(data):
    for block in data.blocks:
        yCondition1 = ((almostEqual(data.player.y3, block.y1) or 
            data.player.y3 > block.y1) and 
            data.player.y3 < block.y1 + block.size//2)

        yCondition2 = ((almostEqual(data.player.y4, block.y2) or 
            data.player.y4 > block.y2) and 
            data.player.y4 < block.y2 + block.size//2)

        offset = 9

        if(yCondition1 or yCondition2):

            if((almostEqual(data.player.x3, block.x1) or 
                data.player.x3 > block.x1) and 
                data.player.x3 < block.x2 - offset):


                return ((block.x1, block.y1), (block.x2, block.y2), block)

            elif((almostEqual(data.player.x4, block.x2) or 
                data.player.x4 < block.x2) and 
                data.player.x4 > block.x1 + offset):

                return ((block.x1, block.y1), (block.x2, block.y2), block)

    return None


# check if there are any blocks above player
def checkPlayerUp(data):
    for block in data.blocks:
        yCondition1 = ((almostEqual(data.player.y1, block.y3) or 
            data.player.y1 > block.y3) and 
            data.player.y1 < block.y3 + block.size//2)

        yCondition2 = ((almostEqual(data.player.y2, block.y4) or 
            data.player.y2 > block.y4) and 
            data.player.y2 < block.y4 + block.size//2)

        offset = 9

        if(yCondition1 or yCondition2):

            if((almostEqual(data.player.x1, block.x3) or 
                data.player.x1 > block.x3) and 
                data.player.x1 < block.x4 - offset):


                return ((block.x3, block.y3), (block.x4, block.y4), block)

            elif((almostEqual(data.player.x2, block.x4) or 
                data.player.x2 < block.x4) and 
                data.player.x2 > block.x3 + offset):

                return ((block.x3, block.y3), (block.x4, block.y4), block)

    return None


# check if there are any blocks on player's right
def checkPlayerRight(data):
    for block in data.blocks:
        if((data.player.x2 > block.x1 or almostEqual(data.player.x2, block.x1))
            and data.player.x2 < block.x2 and 
            almostEqual(data.player.y2, block.y1)):

            return (block.x1, block.y1, block)

        elif((data.player.x2 > block.x3 or almostEqual(data.player.x2, block.x3))
            and data.player.x2 < block.x4 and 
            almostEqual(data.player.y2, block.y3)):

            return (block.x3, block.y3, block)

    return None


#  check if there are any blocks on player's left
def checkPlayerLeft(data):
    for block in data.blocks:
        if((data.player.x1 < block.x2 or almostEqual(data.player.x1, block.x2))
            and data.player.x1 > block.x1 and 
            almostEqual(data.player.y1, block.y2)):

            return (block.x2, block.y2, block)

        elif((data.player.x1 < block.x4 or almostEqual(data.player.x1, block.x4)) 
            and data.player.x1 > block.x3 and
            almostEqual(data.player.y1, block.y4)):

            return (block.x4, block.y4, block)

    return None


# check if there are any blocks on player's upper right
def checkPlayerUpRight(data):
    for block in data.blocks:
        if(almostEqual(data.player.x1, block.x1) and
            almostEqual(data.player.y1, block.y1)):

            return (block.x1, block.y1)

    return None


# check if there are any blocks on player's upper left
def checkPlayerUpLeft(data):
    for block in data.blocks:
        if(almostEqual(data.player.x2, block.x2) and
            almostEqual(data.player.y2, block.y2)):

            return (block.x2, block.y2)

    return None


# check if there are any blocks close to the player's down;
# used when the block is moving away
def closePlayerDown(data):
    for block in data.blocks:
        yCondition1 = (data.player.y3 > block.y1 - abs(block.step) - 1 and 
            data.player.y3 < block.y1 + 1)
        yCondition2 = (data.player.y4 > block.y2 - abs(block.step) - 1 and 
            data.player.y4 < block.y2 + 1)

        if(yCondition1 or yCondition2):
            if((almostEqual(data.player.x3, block.x1) or 
                data.player.x3 > block.x1) and 
                data.player.x3 < block.x2 - 3*abs(block.step)):

                return ((block.x1, block.y1), (block.x2, block.y2), block)

            elif((almostEqual(data.player.x4, block.x2) or 
                data.player.x4 < block.x2) and 
                data.player.x4 > block.x1 + 3*abs(block.step)):

                return ((block.x1, block.y1), (block.x2, block.y2), block)

    return None


# check if there are any blocks close to the player's right;
# used when the block is moving away
def closePlayerRight(data):
    for block in data.blocks:
        if((data.player.x2 > block.x1 - abs(block.step) - 1 and 
            data.player.x2 < block.x1 + 1) and 
            data.player.y2 > block.y1 - abs(block.step) - 1 and
            data.player.y2 < block.y1 + abs(block.step) + 1):

            return (block.x1, block.y1, block)

        elif((data.player.x2 > block.x3 - abs(block.step) - 1 and 
            data.player.x2 < block.x3 + 1) and 
            data.player.y2 > block.y3 - abs(block.step) - 1 and
            data.player.y2 < block.y3 + abs(block.step) + 1):

            return (block.x3, block.y3, block)

    return None


# check if there are any blocks close to the player's left;
# used when the block is moving away
def closePlayerLeft(data):
    for block in data.blocks:
        if((data.player.x1 < block.x2 + abs(block.step) + 1 and 
            data.player.x1 > block.x2 - 1) and 
            data.player.y1 > block.y2 - abs(block.step) - 1 and
            data.player.y1 < block.y2 + abs(block.step) + 1):

            return (block.x2, block.y2, block)

        elif((data.player.x1 < block.x4 + abs(block.step) + 1 and
            data.player.x1 > block.x4 - 1) and
            data.player.y1 > block.y4 - abs(block.step) - 1 and
            data.player.y1 < block.y4 + abs(block.step) + 1):

            return (block.x4, block.y4, block)

    return None


# check if player collides into a moving block from the right
def collisionPlayerRight(data):
    for block in data.blocks:
        if((data.player.x2 > block.x1 or almostEqual(data.player.x2, block.x1))
            and data.player.x2 < block.x2 and data.player.y2 > block.y1
            and data.player.y2 < block.y3 and block.step == -abs(block.step)):

            return (block.x1, block.y1, block)

    return None


#check if player collides into a moving bloc from the left
def collisionPlayerLeft(data):
    for block in data.blocks:
        if((data.player.x1 < block.x2 or almostEqual(data.player.x1, block.x2))
            and data.player.x1 > block.x1 and data.player.y1 > block.y2
            and data.player.y1 < block.y4 and block.step == abs(block.step)):

            return (block.x2, block.y2, block)


# update player when interacting with moving block or others
def checkForBlocks(data):
    checkMoveFromDown(data)

    data.playerPushed = False

    checkMoveFromRight(data)
    checkMoveFromLeft(data)
    

# check for blocks from down the player
def checkMoveFromDown(data):
    downBlock = checkPlayerDown(data)
    downCloseBlock = closePlayerDown(data)

    if(downBlock != None and downBlock[2].maxSteps != 0 and 
        not data.playerPushed):

        points = (downBlock[0], downBlock[1])
        point1 = points[0]
        point2 = points[1]

        if(data.isLeftMotion): data.player.snapPoint("Down Left", point1)

        elif(data.isRightMotion): data.player.snapPoint("Down Right", point2)

        else: data.player.snapGrid("Down", points)

    if(downCloseBlock != None and not data.playerPushed):

        points = (downCloseBlock[0], downCloseBlock[1])
        point1 = points[0]
        point2 = points[1]

        if(data.isLeftMotion): data.player.snapPoint("Down Left", point1)

        elif(data.isRightMotion): data.player.snapPoint("Down Right", point2)

        else: data.player.snapGrid("Down", points)


# check for blocks to player's right
def checkMoveFromRight(data):
    rightBlock = checkPlayerRight(data)
    rightCloseBlock = closePlayerRight(data)
    rightCollisionBlock = collisionPlayerRight(data)

    if(rightBlock != None):
        point = (rightBlock[0], rightBlock[1])

        if(rightBlock[2].isMoving): data.playerPushed = True

        if(data.isUpRightMotion): data.player.snapPoint("Right", point)

        elif(point != (rightBlock[2].x3, rightBlock[2].y3)):
            data.player.snapGrid("Right", point)

    elif(rightCloseBlock != None and data.isUpRightMotion):
        if(rightCloseBlock[2].isMoving): data.playerPushed = True

        point = (rightCloseBlock[0], rightCloseBlock[1])
        data.player.snapPoint("Right", point)

    elif(rightCollisionBlock != None and data.isRightMotion):
        if(rightCollisionBlock[2].isMoving): data.playerPushed = True

        point = (rightCollisionBlock[0], rightCollisionBlock[1])
        data.rightMode = False
        data.isRightMotion = False
        data.leftMode = False
        data.isLeftMotion = False
        data.player.snapGrid("Right", point)


# check for blocks from player's left
def checkMoveFromLeft(data):
    leftBlock = checkPlayerLeft(data)
    leftCloseBlock = closePlayerLeft(data)
    leftCollisionBlock = collisionPlayerLeft(data)

    if(leftBlock != None):
        point = (leftBlock[0], leftBlock[1])

        if(leftBlock[2].isMoving): data.playerPushed = True

        if(data.isUpLeftMotion): data.player.snapPoint("Left", point)

        elif(point != (leftBlock[2].x4, leftBlock[2].y4)):
            data.player.snapGrid("Left", point)

    elif(leftCloseBlock != None and data.isUpLeftMotion):
        if(leftCloseBlock[2].isMoving): data.playerPushed = True

        point = (leftCloseBlock[0], leftCloseBlock[1])
        data.player.snapPoint("Left", point)

    elif(leftCollisionBlock != None and data.isLeftMotion):
        if(leftCollisionBlock[2].isMoving): data.playerPushed = True

        point = (leftCollisionBlock[0], leftCollisionBlock[1])
        data.leftMode = False
        data.isLeftMotion = False
        data.rightMode = False
        data.isRightMotion = False
        data.player.snapGrid("Left", point)


# move the moving type blocks
def moveBlocks(data):
    for block in data.blocks:
        if(block.maxSteps != None):
            block.moveBlock()


# collecting the prizes and updating score
def collectPrize(data):
    for prize in data.prizes:
        if(almostEqual(data.player.x1, prize.x) and 
            almostEqual(data.player.y1, prize.y)):
            
            data.score += prize.points
            data.pinkies += 1
            data.prizes.remove(prize)


# activate Trigger when player comes in contact
def activateTrigger(data):
    for trigger in data.triggers:
        if(almostEqual(trigger.x, data.player.x1) and 
            almostEqual(trigger.y, data.player.y1) and trigger.color == "Red"):

            trigger.color = "Green"


# update lives when player falls out of bounds
def updateDeaths(data):
    if(data.player.y1 > data.height + data.player.size):
        data.deaths += 1
        data.score = data.score // 2
        startX = data.player.startX
        startY = data.player.startY
        data.player.resetPlayer()


# set the level's blocks, player, finish, etc.
def setLevel(data, level):
    data.blocks = []
    data.prizes = []
    data.triggers = []
    data.isRightMotion = False
    data.isLeftMotion = False
    data.isUpRightMotion = False
    data.isUpLeftMotion = False

    if(level == 1):
        setLevel1(data)

    elif(level == 2):
        setLevel2(data)

    elif(level == 3):
        setLevel3(data)

    elif(level == 4):
        setLevel4(data)

    elif(level == 5):
        setLevel5(data)

    elif(level == 6):
        setLevel6(data)

    elif(level == 7):
        setLevel7(data)

    elif(level == 8):
        setLevel8(data)

    elif(level == 9):
        setLevel9(data)


def setLevel1(data):
    (startX, startY) = (100, 100); data.player = PlayerSquare(startX, startY)

    blockX = startX + 3*data.player.size
    prizeX = startX + 7*data.player.size
    finishX = startX + 9*data.player.size

    prizeY = finishY = blockY = 300
    blockY2 = blockY + data.player.size

    for i in range(10):
        data.blocks += [Block(startX + data.player.size*i, 
            blockY2, (None, None, 1))]

    data.blocks += [Block(blockX, blockY, (None, None, 1))]
   
    data.prizes += [Prize(prizeX, prizeY)]
    
    data.finish = Finish(finishX, finishY)


def setLevel2(data):
    (startX, startY) = (100, 100); data.player = PlayerSquare(startX, startY)
    
    blockX =  startX
    blockX2 = prizeX = 300
    blockX3 = prizeX2 = 500
    mBlockX = blockX3 - 3*data.player.size
    prizeX3 = finishX = startX + 14*data.player.size

    blockY = prizeY3 = 200
    prizeY = mBlockY = blockY + data.player.size
    prizeY2 = finishY = blockY + 2*data.player.size

    numSteps = 70

    for i in range(5):
        data.blocks += [Block(blockX + data.player.size*i, 
            blockY + data.player.size, (None, None, 1))]
        data.blocks += [Block(blockX2 + data.player.size*i,
            blockY + 2*data.player.size, (None, None, 1))]
        data.blocks += [Block(blockX3 + data.player.size*i,
            blockY + 3*data.player.size, (None, None, 1))]

    data.blocks += [Block(mBlockX, mBlockY, ("X", numSteps, 1))]

    data.prizes += [Prize(prizeX, prizeY)] + [Prize(prizeX2, prizeY2)]
    data.prizes += [Prize(prizeX3, prizeY3)]

    data.finish = Finish(finishX, finishY)


def setLevel3(data):
    (startX, startY) = (100, 100)

    data.player = PlayerSquare(startX, startY)

    (blockX, blockX2, blockX3) = (100, 500, 300)
    (blockY, blockY2, blockY3) = (240, 240, 320)
    (prizeX, prizeX2) = (300, 460)
    (prizeY, prizeY2) = (280, 280)
    (triggerX, triggerY) = (380, 280)
    (finishX, finishY) = (580, 200)

    for i in range(5):
        data.blocks += [Block(blockX + data.player.size*i, blockY, 
            (None, None, 1))]
        data.blocks += [Block(blockX2 + data.player.size*(i+1),blockY2, 
            (None, None, 1))]

    for i in range(8):
        data.blocks += [Block(blockX3 + data.player.size*i,
            blockY3, (None, None, 1))]

    data.prizes += [Prize(prizeX, prizeY)]
    data.prizes += [Prize(prizeX2, prizeY2)]
    data.triggers += [Trigger(triggerX, triggerY)]
    
    data.finish = Finish(finishX, finishY)


def setLevel4(data):
    (startX, startY) = (700, 100); data.player = PlayerSquare(startX, startY)

    blockX = startX
    blockX2 = 500 - data.player.size
    blockX3 = 300 - 3 * data.player.size
    mBlockX = blockX2 - 2*data.player.size
    mBlockX2 = finishX = blockX3 - 2*data.player.size

    blockY = 300
    blockY2 = blockY + data.player.size
    blockY3 = blockY2 + data.player.size
    mBlockY = blockY - data.player.size
    mBlockY2 = mBlockY - data.player.size
    mBlockY3 = mBlockY + data.player.size
    finishY = mBlockY3 + data.player.size

    numSteps = 60

    for i in range(3):
        data.blocks += [Block(blockX-i*data.player.size,blockY,(None,None,1))]
        data.blocks += [Block(blockX2-i*data.player.size,blockY2,(None,None,1))]
        data.blocks += [Block(blockX3-i*data.player.size,blockY3,(None,None,1))]

    data.prizes += [Prize(blockX3, blockY3 - data.player.size)]

    data.blocks += [Block(mBlockX, mBlockY, ("X", numSteps, 1))]
    data.blocks += [Block(mBlockX, mBlockY2, ("X", numSteps, 1))]
    data.blocks += [Block(mBlockX2, mBlockY, ("X", numSteps, 1))]
    data.blocks += [Block(mBlockX2, mBlockY3, ("X", numSteps, 1))]

    data.finish = Finish(finishX, finishY)


def setLevel5(data):
    (startX, startY) = (700, 100); data.player = PlayerSquare(startX, startY)

    blockX = finishX = startX; blockX2 = 140
    mBlockX = mBlockX2 = mBlockX3 = 260
    mBlockX4 = blockX - 3*data.player.size

    blockY = 160; blockY2 = 320
    blockY3 = mBlockY = mBlockY4 = blockY + 3*data.player.size
    mBlockY2 = mBlockY + 3*data.player.size
    mBlockY3 = mBlockY2 + 3*data.player.size
    finishY = blockY2 - data.player.size

    numSteps = 50

    for i in range(5):
        data.blocks += [Block(blockX-i*data.player.size,blockY,(None,None,1))]

    for i in range(3):
        data.blocks += [Block(blockX-i*data.player.size,blockY2,(None,None,1))]
        data.blocks += [Block(mBlockX+i*data.player.size, mBlockY,
            ("X", numSteps, 1))]
        data.blocks += [Block(mBlockX2+i*data.player.size, mBlockY2,
            ("X", numSteps, -1))]
        data.blocks += [Block(mBlockX3+i*data.player.size, mBlockY3,
            ("X", numSteps, 1))]
    
    data.blocks += [Block(mBlockX4, mBlockY4, ("Y", numSteps, -1))]

    data.triggers += [Trigger(100, mBlockY2 - data.player.size)]
    
    data.finish = Finish(finishX, finishY)


def setLevel6(data):
    (startX, startY) = (660, 60)

    data.player = PlayerSquare(startX, startY)

    (blockX, blockX2, blockX3, blockX4, blockX5) = (660, 620, 100, 140, 260)
    (blockY, blockY2, blockY3, blockY4, blockY5) = (180, 180, 460, 460, 140)

    (triggerX, triggerX2, triggerX3, triggerX4) = (580, 540, 300, 220)
    (triggerY, triggerY2, triggerY3, triggerY4) = (180, 260, 340, 180)

    (finishX, finishY) = (blockX3, blockY3 - data.player.size)

    data.blocks += [Block(blockX, blockY, (None, None, 1))]
    data.blocks += [Block(blockX2, blockY2, (None, None, 1))]
    data.blocks += [Block(blockX3, blockY3, (None, None, 1))]
    data.blocks += [Block(blockX4, blockY4, (None, None, 1))]
    data.blocks += [Block(blockX5, blockY5, (None, None, 1))]

    data.triggers += [Trigger(triggerX, triggerY)]
    data.triggers += [Trigger(triggerX2, triggerY2)]
    data.triggers += [Trigger(triggerX3, triggerY3)]
    data.triggers += [Trigger(triggerX4, triggerY4)]

    data.finish = Finish(finishX, finishY)


def setLevel7(data):
    (startX, startY) = (380, 100); data.player = PlayerSquare(startX, startY)
    
    (rows, cols) = (3, 3)
    (blockX, blockX2, blockX3) = (140, 340, 540)
    (triggerX, triggerY) = (620, 420)
    blockY = 140; space = 160

    (finishX, finishY) = (140, 100)

    for r in range(rows):
        for c in range(cols):
            data.blocks += [Block(blockX + c*data.player.size, blockY+r*space,
                (None, None, 1))]
            data.blocks += [Block(blockX3 + c*data.player.size, blockY+r*space,
                (None, None, 1))]
            if(r == 1): 
                data.blocks += [Block(blockX2 + c*data.player.size, 
                    blockY+r*space, (None, None, 1))]
                
                if(c == 2): 
                    data.triggers += [Trigger(blockX2 + c*data.player.size,
                        blockY+r*space - data.player.size)]
                    data.triggers += [Trigger(blockX + c*data.player.size,
                        blockY+r*space - data.player.size)]

    data.triggers += [Trigger(triggerX, triggerY)]

    data.finish = Finish(finishX, finishY)


def setLevel8(data):
    (startX, startY) = (100, 300); data.player = PlayerSquare(startX, startY)

    (blockX, blockX2, blockX3) = (100, 300, 580)
    (blockY, blockY2, blockY3) = (420, 420, 420)
    (prizeX, prizeY) = (blockX, blockY - data.player.size)
    (triggerX, triggerY) = (blockX2, blockY2 - data.player.size)
    (finishX, finishY) = (blockX3, blockY3 - data.player.size)

    range1 = 5; range2 = 7

    for i in range(range1):
        data.blocks += [Block(blockX + i*data.player.size,blockY,(None,None,1))]
        data.prizes += [Prize(prizeX + i*data.player.size, prizeY)]

    for i in range(range2):
        data.blocks += [Block(blockX2 + i*data.player.size, 
            blockY2 - i*data.player.size, (None, None, 1))]

        data.triggers += [Trigger(triggerX + i*data.player.size,
            triggerY - i*data.player.size)]

    data.blocks += [Block(blockX3, blockY3, (None, None, 1))]

    data.finish = Finish(finishX, finishY)


def setLevel9(data):
    (startX, startY) = (140, 300)

    data.player = PlayerSquare(startX, startY)

    (blockX, blockY) = (140, 420)
    (triggerX, triggerY) = (180, 380)
    (finishX, finishY) = (620, 380)
    length = 13; space = 160; numTriggers = 3

    for i in range(length):
        data.blocks += [Block(blockX+i*data.player.size, blockY, (None,None,1))]

    for i in range(numTriggers):
        data.triggers += [Trigger(triggerX + i*space, triggerY)]

    data.finish = Finish(finishX, finishY)


# unlock a level when current level is completed
def unlockLevel(data):
    if(data.currentLevel < data.totalLevels):
        newLevel = str(data.currentLevel + 1)
        data.levels.add(newLevel)

def triggerEvent(data):
    triggerColor = "Medium Purple"

    if(data.currentLevel == 3):
        eventLevel3(data, triggerColor)

    elif(data.currentLevel == 5):
        eventLevel5(data, triggerColor)

    elif(data.currentLevel == 6):
        eventLevel6(data, triggerColor)

    elif(data.currentLevel == 7):
        eventLevel7(data, triggerColor)

    elif(data.currentLevel == 8):
        eventLevel8(data, triggerColor)

    elif(data.currentLevel == 9):
        eventLevel9(data, triggerColor)


def eventLevel3(data, triggerColor):
    if(data.triggers[0].color == "Green" and not data.triggers[0].isOn):

            newBlock = Block(500, 280, (None, None, 1))
            newBlock.color = triggerColor
            data.blocks += [newBlock]
            data.triggers[0].isOn = True


def eventLevel5(data, triggerColor):
    if(data.triggers[0].color == "Green" and not data.triggers[0].isOn):

            data.prizes += [Prize(620, 280)]
            data.prizes += [Prize(660, 280)]
            data.triggers[0].isOn = True


def eventLevel6(data, triggerColor):
    for i in range(len(data.triggers)):
        if(data.triggers[i].color == "Green" and not data.triggers[i].isOn):

            if(i == 0):
                newBlock = Block(580, 260, (None, None, 1))
                newBlock.color = triggerColor; data.blocks += [newBlock]
                data.triggers[0].isOn = True

            elif(i == 1):
                newBlock1 = Block(540, 340, ("X", 40, -1))
                newBlock2 = Block(580, 340, ("X", 40, -1))
                newBlock3 = Block(340, 340, (None, None, 1))
                newBlock3.color = triggerColor
                data.blocks += [newBlock1] + [newBlock2] + [newBlock3]
                data.triggers[1].isOn = True

            elif(i == 2):
                data.blocks += [Block(300, 460, ("Y", 80, 1))]
                data.triggers[2].isOn = True

            elif(i == 3):
                numBlocks = 3; s = data.player.size
                (blockX, blockY) = (180, 340)
                (prizeX, prizeY) = (blockX, blockY - s)

                for i in range(numBlocks):
                    data.blocks += [Block(blockX + i*s, blockY, (None,None,1))]
                    data.prizes += [Prize(prizeX + i*s, prizeY)]
                    
                data.triggers[3].isOn = True
                

def eventLevel7(data, triggerColor):
    for i in range(len(data.triggers)):
        if(data.triggers[i].color == "Green" and not data.triggers[i].isOn):

            if(i == 0):
                newBlock1 = Block(260, 260, (None, None, 1))
                newBlock2 = Block(300, 260, (None, None, 1))
                newBlock1.color = newBlock2.color = triggerColor
                data.blocks += [newBlock1]
                data.blocks += [newBlock2]
                data.prizes += [Prize(540, 260)]
                data.triggers[0].isOn = True

            elif(i == 1):
                data.blocks += [Block(100, 460, ("Y", 40, 1))]
                data.blocks += [Block(260, 380, ("X", 80, 1))]
                data.prizes += [Prize(580, 260)]
                data.triggers[1].isOn = True

            elif(i == 2):
                data.blocks += [Block(660, 140, ("Y", 80, -1))]
                data.blocks += [Block(260, 140, ("X", 60, 1))]
                data.prizes += [Prize(620, 260)]
                data.triggers[2].isOn = True


def eventLevel8(data, triggerColor):
    for trigger in data.triggers:
        if(trigger.color == "Green" and not trigger.isOn):
            s = data.player.size
            (tempFinishX, tempFinishY) = (data.finish.x1, data.finish.y1)
            (tempBlockX, tempBlockY) = (data.blocks[-1].x1, data.blocks[-1].y1)

            data.blocks.pop(-1)
            data.finish = Finish(tempFinishX, tempFinishY - s)
            data.blocks += [Block(tempBlockX, tempBlockY - s, (None, None, 1))]

            trigger.isOn = True


def eventLevel9(data, triggerColor):
    for i in range(len(data.triggers)):
        if(data.triggers[i].color == "Green" and not data.triggers[i].isOn):

            (rows, cols) = (5, 3) 
            (blockX, blockY) = (180, 140)
            (blockX2, blockY2) = (500, 140)
            space = 160

            if(i == 0 or i == 1):
                for r in range(rows):
                    new = Block(blockX+i*space,blockY+r*data.player.size,
                        (None,None,1))
                    new.color = triggerColor
                    data.blocks += [new]

                data.triggers[i].isOn = True

            elif(i == 2):
                for r in range(rows):
                    for c in range(cols):
                        if(r % 2 == 0 or (r==1 and c==2) or (r==3 and c==0)):

                            new = Block(blockX2 + c*data.player.size,
                                blockY2 + r*data.player.size, (None,None,1))

                            new.color = triggerColor
                            data.blocks += [new]

                data.triggers[i].isOn = True


# check if player reached finish box
def checkFinish(data):
    noMotion = (not data.isRightMotion and not data.isUpRightMotion and 
        not data.isLeftMotion and not data.isUpLeftMotion)

    if(almostEqual(data.player.x1, data.finish.x1) and 
        almostEqual(data.player.y1, data.finish.y1) and noMotion):
        
        data.score += data.finish.points
        unlockLevel(data)
        data.gameIsOn = False
        data.levelPanelIsOn = True
        setLevelSquares(data)


# set a level when appropriate number key is pressed
def chooseLevel(data, event):
    if(data.levelPanelIsOn):
        if(event.char in data.levels):
            data.currentLevel = int(event.char)
            setLevel(data, data.currentLevel)
            data.levelPanelIsOn = False
            data.gameIsOn = True


# set coordinates of level squares
def setLevelSquares(data):
    rows = cols = 3

    for level in data.levels:
        level = int(level)
        x = (data.levelPanel.startGridX + 
            ((level - 1) % cols) * data.levelPanel.spacing)
        y = (data.levelPanel.startGridY + 
            ((level - 1) // cols) * data.levelPanel.spacing)

        data.levelSquares += [LevelSquare(x, y, str(level))]


# draw elements for the game
def drawGame(data, canvas):
    drawSplashScreen(data, canvas)
    drawLevelPanel(data, canvas)
    drawLevel(data, canvas)
    drawMenu(data, canvas)
    drawHelpScreen(data, canvas)
    drawScoreBoard(data, canvas)


# draw splash screen when game is not playing
def drawSplashScreen(data, canvas):
    if(data.splashIsOn):
        data.screen.drawSplashScreen(canvas)


# draw level panel when about to select level
def drawLevelPanel(data, canvas):
    if(data.levelPanelIsOn):
        data.levelPanel.drawLevelPanel(canvas)
        drawLevelSquares(data, canvas)

# draw Level Square when a level is unlocked
def drawLevelSquares(data, canvas):
    for square in data.levelSquares:
        square.drawLevelSquare(canvas)


def drawBackground(data, canvas):
    canvas.create_rectangle(-2, -2, data.width+3, data.height+3, 
        fill="Light Cyan")


# draw level when game is active
def drawLevel(data, canvas):
    if(data.gameIsOn):
        drawBackground(data, canvas)

        for prize in data.prizes:
            prize.drawPrize(canvas)

        for trigger in data.triggers:
            trigger.drawTrigger(canvas)

        for block in data.blocks:
            block.drawBlock(canvas)

        data.finish.drawFinish(canvas)
        data.player.drawSquare(canvas)


# draw menu when pausing game
def drawMenu(data, canvas):
    if(data.gameIsOn and data.menuIsOn):
        data.menu.drawMenu(canvas)


# draw help screen
def drawHelpScreen(data, canvas):
    if(data.helpIsOn):
        data.helpScreen.drawHelpScreen(canvas)


# draw score board
def drawScoreBoard(data, canvas):
    if(data.gameIsOn):
        offsetY = 30
        scoreboard = ("Level: %s   Deaths: %d   Pinkies: %d   Score: %d" 
                % (data.currentLevel, data.deaths, data.pinkies, data.score))

        canvas.create_text(data.width, offsetY, text=scoreboard, 
            font="Helevetica 20 bold", anchor=SE)

    elif(data.levelPanelIsOn and not data.helpIsOn):
        offsetY = data.height - 70
        scoreboard = ("Deaths: %d   Pinkies: %d   Score: %d" 
                % (data.deaths, data.pinkies, data.score))

        canvas.create_text(data.width//2, offsetY, text=scoreboard, 
            font="Helevetica 20 bold")


# turn the splash screen, level panel, or menu on/off depending on conditions
def manageScreens(data, event):
    if(event.char == "w" or event.char == "W"):
        if(data.splashIsOn and not data.helpIsOn):
            data.splashIsOn = False
            data.levelPanelIsOn = True # to go to level panel
            setLevelSquares(data)

        elif(data.gameIsOn and not data.helpIsOn):
            if(not data.menuIsOn): data.menuIsOn = True  # to pause the game

            elif(data.menuIsOn):
                data.menuIsOn = False   # to go back to splash panel
                data.gameIsOn = False
                data.splashIsOn = True

        elif(data.helpIsOn): data.helpIsOn = False

    elif(event.char == "a" or event.char == "A"):    # to go to help screen
        if(data.splashIsOn or data.levelPanelIsOn or 
            (data.gameIsOn and data.menuIsOn)):

            data.helpIsOn = True

    if(data.menuIsOn and not data.helpIsOn):
        # to unpause the game
        if(event.char == "d" or event.char == "D"): data.menuIsOn = False   

        # turn on help screen
        elif(event.char == "a" or event.char == "A"): data.helpIsOn = True

        elif(event.char == "s" or event.char == "S"):
            data.menuIsOn = False
            data.gameIsOn = False
            data.levelPanelIsOn = True


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    manageScreens(data, event)
    chooseLevel(data, event)
    controlPlayer(data, event)
        

def keyReleased(event, data):
    if(event.keysym == "Right" and (data.rightMode or data.upRightMode)):
        data.rightMode = False
        data.upRightMode = False

    elif(event.keysym == "Left" and (data.leftMode or data.upLeftMode)):
        data.leftMode = False
        data.upLeftMode = False
    

# order matters in order for player to interact with Blocks properly
def timerFired(data):
    if(data.gameIsOn and not data.menuIsOn and data.player != None):
        resetPlayer(data)
        movePlayer(data)
        fallPlayer(data)
        moveBlocks(data)
        checkForBlocks(data)
        collectPrize(data)
        activateTrigger(data)
        updateDeaths(data)
        triggerEvent(data)
        checkFinish(data)


def redrawAll(canvas, data):
    drawGame(data, canvas)


# tkinter base provided from course website
# somewhat modified to include keyReleased
# https://www.cs.cmu.edu/~112/notes/hw6.html
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

    def keyReleasedWrapper(event, canvas, data):
        keyReleased(event, data)
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
    data.timerDelay = 60 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyReleasedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Thank you for playing. ^_^")


def playEdge():
    run(800, 600)


playEdge()

