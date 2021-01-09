import time
import turtle
from turtle import Turtle, Screen
from cars import Cars, car_list
from racer import Racer
from finishline import RaceLine
from levels import Level

# a turtle crossing game. Get the turtle to the finish line without hitting a car. Move forward with spacebar

turtle.listen()
# generate screen
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# generate game objects 
car = Cars()
racer_turtle = Racer()
finish_line = RaceLine(250)
start_line = RaceLine(-250) 
level_start = Level()
# instructions = level_start.instructions()
# start game
game_on = True
while game_on:
    time.sleep(level_start.time_set)
    screen.update()
    for car in car_list:
        car.move()
        # generate one car after previous reaches a given coordinate
        if car_list[-1].xcor() in range(200, 250):
            car = Cars()
        # Detect if turtle collides with car, end game
        if car.distance(racer_turtle) <= 20:
            level_start.game_over()
            game_on = False
        # Reset turtle and increase speed of cars after crossing finish line
        if racer_turtle.ycor() > 250:
            racer_turtle.reset_pos()
            level_start.next_level()

    turtle.onkey(fun=racer_turtle.move_racer, key="space")


screen.exitonclick()
