STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
from turtle import Turtle



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        self.movedistance=MOVE_DISTANCE
    def add_segment(self,position):
        newsegment = Turtle("circle")
        newsegment.penup()
        newsegment.color("turquoise")
        newsegment.goto(position)
        self.segments.append(newsegment)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def resetsnake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

