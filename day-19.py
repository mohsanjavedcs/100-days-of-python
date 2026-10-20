from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def rotate_ccl():
    tim.left(10)
def rotate_cl():
    tim.right(10)
def tim_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_ccl)
screen.onkey(key="d", fun=rotate_cl)
screen.onkey(key="c", fun=tim_clear)

screen.exitonclick()
