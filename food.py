import random
from turtle import Turtle

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
    def foodlocation(self):
        self.randomx=random.randint(-290,290)
        self.randomy=random.randint(-290,290)
        self.goto(self.randomx,self.randomy)

