from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Znake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    snake2 = Turtle("square")
    snake2.color("white")
    snake2.goto(position)







screen.exitonclick()