# create a cars class that generates a random number of cars and moves them across the screen
from turtle import Turtle
import random

colors = ['blue', 'yellow', 'pink', 'violet',
          'grey', 'brown', 'purple', 'red', 'orange']
car_list = []


class Cars(Turtle):

    def __init__(self):
        """Create a car of random color and move it across the screen"""
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.goto(random.randint(300, 350), random.randint(-240, 240))
        car_list.append(self)

    def move(self):
        self.forward(10)
