from turtle import Turtle
import random

COLOR_LIST = ["#FFB100", "#FBC252", "#508D69", "#F3B664", "#A8DF8E", "#94ED88", "#3BB873"]


class Brick(Turtle):

	def __init__(self, x_cor, y_cor):
		super().__init__()
		self.shape("square")
		self.shapesize(stretch_wid=1, stretch_len=3)
		self.color(random.choice(COLOR_LIST))
		self.penup()
		self.goto(x=x_cor, y=y_cor)

	# 	Borders of the brick
		self.bottom_border = self.ycor() - 10
		self.top_border = self.ycor() + 10
		self.right_border = self.xcor() + 28
		self.left_border = self.xcor() - 28


class Bricks:
	def __init__(self):
		self.y_start = 110
		self.y_end = 310
		self.bricks = []
		self.create_rows()

	def create_row(self, y_cor):
		for i in range(-460, 480, 65):
			brick = Brick(i, y_cor)
			self.bricks.append(brick)

	def create_rows(self):
		for i in range(self.y_start, self.y_end, 30):
			self.create_row(i)


