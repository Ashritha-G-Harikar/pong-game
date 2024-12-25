from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
t = 0.1

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
game_on = True
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
score = Scoreboard()


screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


while game_on:
    time.sleep(t)
    screen.update()
    ball.move()

    # Detect collision with upside or downside wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right or left wall
    if right_paddle.distance(ball) < 50 and ball.xcor() >= 300 or left_paddle.distance(ball) < 50 and ball.xcor() <= -300:
        ball.bounce_x()

    # Get ball back to its origin when the ball moves out of bounds
    # Left paddle misses the ball
    if ball.xcor() > 450:
        ball.move_ball()
        ball.bounce_x()
        score.add_score_l()
        score.update_score()

    # Right paddle misses the ball
    if ball.xcor() < -450:
        ball.move_ball()
        ball.bounce_x()
        score.add_score_r()
        score.update_score()


screen.exitonclick()
