from turtle import Turtle
import time
FONT="Arial", 35, "normal"

class Start_Game(Turtle):
    def __init__(self):
        super().__init__()
    def gameisstarting(self):
        self.penup()
        self.goto(0,-100)
        self.hideturtle()
        self.color("yellow")
        self.write("Blue Ball: 2 Points\n\nRed Ball: 1 Point\n\nYellow Bal: Die", align="center", font=(FONT))
        time.sleep(7)
        self.clear()

