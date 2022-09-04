from turtle import Turtle,Screen
FONT="Arial", 24, "normal"
import time
screen=Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("record.txt") as  data:
            self.high_score=int(data.readline(1))
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=(FONT))

    def resetgame(self):
        if self.score>self.high_score:
            self.high_score=self.score

            name = screen.textinput(title="Recording", prompt="Enter name to record")

            with open("record.txt",mode="w") as  data:
                data.write(f"{self.high_score}\n{name}")
            time.sleep(1)
            screen.bye()


        self.score=0
        self.update_scoreboard()

    def increasesore(self):
        self.score += 1
        self.update_scoreboard()
    def paused(self):
        self.goto(0,0)
        self.write("PAUSED FOR 5 SECONDS", align="center", font=(FONT))
        time.sleep(5)
        self.clear()
        self.update_scoreboard()