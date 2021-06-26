from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title="Who will win?", prompt="Choose a turtle:").lower()

colours = ["blue", "red", "purple", "orange"]
y_start = [45, 15, -15, -45]
all_turtles = []

for turtle_index in range(0,4):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colours[turtle_index])
    turtle.setposition(x=-200, y=y_start[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 230:
            if turtle.pencolor() == user_bet:
                print("You win!")
            else:
                print("You lose")
            is_race_on = False

screen.exitonclick()