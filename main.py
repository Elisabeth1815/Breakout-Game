from turtle import Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#1B2430")
screen.setup(width=1000, height=700)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -310))

bricks = Bricks()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move()

# Detect collision with side walls
	if ball.xcor() > 480 or ball.xcor() < -480:
		ball.bounce_x()

# Detect collision with top wall
	if ball.ycor() > 320:
		ball.bounce_y()

# Detect when paddle misses
	if ball.ycor() < - 340:
		ball.reset_position()
		scoreboard.live_decrease()
		scoreboard.game_over()

	if scoreboard.lives == 0:
		break

# Detect collision with paddle
	if ball.distance(paddle) < 60 and ball.ycor() < -280:
		ball.bounce_y()

# Detect collision with bricks

	for brick in bricks.bricks:
		if ball.distance(brick) < 35:
			brick.clear()
			brick.goto(1500, 1500)
			bricks.bricks.remove(brick)

			# Detect bottom collision
			if ball.ycor() < brick.bottom_border:
				ball.bounce_y()
				scoreboard.point()

			# Detect top collision
			if ball.ycor() > brick.top_border:
				ball.bounce_y()
				scoreboard.point()

			# Detect right collision
			if ball.xcor() > brick.right_border:
				ball.bounce_x()
				scoreboard.point()

			# Detect left collision
			if ball.xcor() < brick.left_border:
				ball.bounce_x()
				scoreboard.point()

# Detect crossing a wall and show up at other side
	if paddle.xcor() < -500:
		paddle.move_right()
	elif paddle.xcor() > 500:
		paddle.move_left()

# Detect victory
	if len(bricks.bricks) == 0:
		scoreboard.win()
		break


screen.exitonclick()


