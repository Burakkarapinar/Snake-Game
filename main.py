from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
from StartGame import Start_Game


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("YILANNNNN")
screen.tracer(0)

snake=Snake()
food=Food()
food.foodlocation()
scoreboard=Scoreboard()

poisonfood=Food()
poisonfood.foodlocation()
poisonfood.shapesize(1,1)
poisonfood.color("Yellow")

bonusfood=Food()
bonusfood.foodlocation()
bonusfood.shapesize(1,1)
bonusfood.color("Blue")

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(scoreboard.paused,"p")

gamestart=Start_Game()
gamestart.gameisstarting()

gameison=True
while gameison:
    screen.update()
    time.sleep(0.08)
    snake.move()

    randombonus = random.randint(1, 200)
    if randombonus==1:
        bonusfood.foodlocation()

    randompoison=random.randint(1, 100)
    if randompoison==1:
        poisonfood.foodlocation()

    #control to eat food
    if snake.head.distance(food)<15:
        food.foodlocation()
        scoreboard.increasesore()
        snake.extend()

    #detect wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.resetgame()
        snake.resetsnake()

    #detect poison food
    if snake.head.distance(poisonfood) <15:
        scoreboard.resetgame()
        snake.resetsnake()

    #detect bonus food
    if snake.head.distance(bonusfood) < 15:
        bonusfood.goto(1000,1000)
        scoreboard.increasesore()
        scoreboard.increasesore()
        snake.extend()
        snake.extend()


    #detect tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.resetgame()
            snake.resetsnake()










screen.exitonclick()
