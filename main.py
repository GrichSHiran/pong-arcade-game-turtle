import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Top-level Constants
SCORE_LIMIT = 3
R_PADDLE_UP = 'i'
R_PADDLE_DOWN = 'k'
L_PADDLE_UP = 'e'
L_PADDLE_DOWN = 'd'

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

# GUI Object
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Game Objects
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
board = Scoreboard(screen)

# Event Listeners
screen.listen()
screen.onkey(r_paddle.move_up, R_PADDLE_UP)
screen.onkey(r_paddle.move_down, R_PADDLE_DOWN)
screen.onkey(l_paddle.move_up, L_PADDLE_UP)
screen.onkey(l_paddle.move_down, L_PADDLE_DOWN)

is_game_over = False
while is_game_over is False:

    # Refresh Screen & Move Pong Ball
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Wall Bounce Logic
    if ball.ycor() > 290:
        ball.bounce(DOWN)

    elif ball.ycor() < -290:
        ball.bounce(UP)

    # Paddle Bounce Logic
    if ball.xcor() > 315 and ball.distance(r_paddle) <= 50:
        ball.bounce(RIGHT)
        ball.is_hit()

    elif ball.xcor() < - 315 and ball.distance(l_paddle) <= 50:
        ball.bounce(LEFT)
        ball.is_hit()

    # Respawn Logic
    if ball.xcor() > 380:
        board.add_left()
        ball.respawn("left")
        screen.update()
        time.sleep(3)

    elif ball.xcor() < -380:
        board.add_right()
        ball.respawn("right")
        screen.update()
        time.sleep(3)

    # Loop-breaking Condition (Game Over)
    if board.r_score >= SCORE_LIMIT or board.l_score >= SCORE_LIMIT:
        is_game_over = True
        board.game_over()
        screen.update()


screen.exitonclick()