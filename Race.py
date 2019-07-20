import turtle
from random import randint

names = []
players = []
winner = 23 #Default value(you can do whatever you want)
window = turtle.Screen() #For window settings

def Window(window_width,window_length): #To define window settings
    window.screensize(window_width,window_length)
    window.bgpic("TurtleRace.gif") #This file is for background.And if you want you can create or find another background and use that one

def lineSet(): #To define race lines
    lines = turtle.Turtle("arrow") #This is the shape of the pen that draws the lines
    lines.color("black")
    lines.pencolor("black")
    lines.penup()
    lines_x = -260 #Start coordinate(x)
    distance = 100 #distance between lines
    for line in range(6): # To draw the lines
        lines.setposition(lines_x + line*distance,300)
        lines.write(str(line*distance)+"m",align="center") #To write line's meter
        lines.pendown()
        lines.right(90)
        lines.forward(350)
        lines.up()
        lines.left(90) # EVERY TIME PEN IS UP, ITS DIRECTION IS 90 DEGREE RIGHT.WE HAVE TO TURN LEFT SO THAT PEN CAN DRAW DOWN EVERY TIME İN NEXT LOOP VALUE

def turtlesSet(color_list):
    xposition_player = -260 #Turtle's starting coordinate -x
    yposition_player = 220 #-y
    distance = 30 # Distance between turtles
    parameter = 0 #To set every turtle's position in y coordinate
    for col in range(6):
        player = turtle.Turtle(shape="turtle")
        player.color(color_list[col])
        player.pencolor(color_list[col])
        player.penup()
        player.setposition(xposition_player,yposition_player + parameter*distance)
        players.append(player)
        parameter -= 1

def Movement():
    gameover = True #To finish race when any turtle has come to the finish line
    while gameover == True:
        for col in range(6):
            players[col].pendown()
            players[col].forward(randint(1, 5))
            if players[col].xcor() >= 240:
                gameover = False
                break
            else:
                pass
    players[col].write(names[col],align="left",font=("ARIAL",15)) #To write winner's name next to his turtle
    window.mainloop() #To wait when game is over(If you erase that function window will close when race is finished)

color_list = ['purple','red','green','blue','orange','yellow'] #These are the colors of turtles(You can change whatever you want
names = ["Turtle_1","Turtle_2","Turtle_3","Turtle_4","Turtle_5","Turtle_6"] #These are the names of players(You can change whatever you want)
Window(1366,768) #This is my PC's max resolution so you can change if you want
lineSet()
turtlesSet(color_list)
Movement()