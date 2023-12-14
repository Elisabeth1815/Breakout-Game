from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("#FAF0E6")
		self.penup()
		self.hideturtle()
		self.score = 0
		self.lives = 4
		self.scoreboard_update()

	def scoreboard_update(self):
		self.clear()
		self.goto(355, 308)
		self.write(f"Lives: {self.lives}    Score: {self.score}", align="center", font=("Roboto", 15, "normal"))

	def point(self):
		self.score += 1
		self.scoreboard_update()

	def live_decrease(self):
		self.lives -= 1
		self.scoreboard_update()

	def game_over(self):
		if self.lives == 0:
			self.goto(0, 0)
			self.write("GAME OVER", align="center", font=("Roboto", 30, "normal"))

	def win(self):
		self.goto(0, 0)
		self.write("YOU WIN!", align="center", font=("Roboto", 30, "normal"))
