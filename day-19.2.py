from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "green", "yellow", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    zee = Turtle(shape="turtle")
    zee.color(colours[turtle_index])
    zee.penup()
    zee.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(zee)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_colour} turtle is the winner.")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

     
screen.exitonclick()