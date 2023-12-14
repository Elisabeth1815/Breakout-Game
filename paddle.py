from turtle import Turtle


class Paddle(Turtle):

	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("#B9B4C7")
		self.fillcolor("#FAF0E6")
		self.shapesize(stretch_wid=1, stretch_len=6)
		self.penup()
		self.goto(position)

	def go_right(self):
		self.fd(40)

	def go_left(self):
		self.bk(40)

	def move_right(self):
		self.speed(100)
		self.goto(500, -310)

	def move_left(self):
		self.speed(100)
		self.goto(-500, -310)

