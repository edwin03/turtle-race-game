from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_cord = -100

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    y_cord += 30
    tim.goto(x=-230, y=y_cord)
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    random_dist = random.randint(0, 10)
    for tims in turtles:
        tims.fd(random_dist)


screen.exitonclick()