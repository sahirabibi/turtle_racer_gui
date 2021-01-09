from turtle import Turtle
# draw the racelines for race


class RaceLine(Turtle):

    def __init__(self, y_coordinate):
        """Generate a line across the screen at chosen y-coordinate)"""
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=30)
        self.goto(0, y_coordinate)
