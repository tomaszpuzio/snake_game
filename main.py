from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My ping pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True
speed = 0.05
while is_game_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.update_l_score()


    #Detect if L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.update_r_score()


screen.exitonclick()