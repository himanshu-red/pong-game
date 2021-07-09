from turtle import Screen
from pad import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height = 600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
        # game_on = False
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if  ball.distance (r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()



    if ball.xcor() > 340 :
        ball.reset_position()
        scoreboard.right_score()

    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.left_score()


screen.exitonclick()
