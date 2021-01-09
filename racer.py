# create turtle class
from turtle import Turtle
import turtle


class Racer(Turtle):

    def __init__(self):
        """Generate a turtle object at lower end of screen"""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(0, -275)

    def move_racer(self):
        self.forward(10)

    def reset_pos(self):
        self.goto(0, -275)
