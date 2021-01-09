from turtle import Turtle

# increase level and difficulty after turtle reaches finish line


class Level(Turtle):

    def __init__(self):
        """Generate a level board to keep track of current level"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.setposition(-250, 275)
        self.write(f"Level: {self.level}", align='left',
                   font=("Courier", 20, "normal"))
        self.time_set = 0.5
    
    # def instructions(self):
    #     self.setposition(75, 275)
    #     self.write(f"Press/Hold spacebar to move turtle.", align='left',
    #                font=("Courier", 10, "normal"))


    def next_level(self):
        """Increase level and speed of cars with each level increase"""
        self.clear()
        self.level += 1
        self.time_set *= 0.5
        self.write(f"Level: {self.level}", align='left',
                   font=("Courier", 20, "normal"))

    def game_over(self):
        """End game after collision with car"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Courier", 40, "bold"))

