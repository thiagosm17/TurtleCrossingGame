from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 300))
            self.all_cars.append(new_car)

    def move(self, level):
        for x in range(len(self.all_cars)):
            self.all_cars[x].backward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)



