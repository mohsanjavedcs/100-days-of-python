import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_count = 0

answer_state = screen.textinput(title=f"{guess_count}/50 States Correct", prompt="What's another state name?")

answer = df[df["state"] == answer_state]
states = df["state"]
x_cor = df["x"]
y_cor = df["y"]

for state in states:
    if answer_state == state:
        answer_x = answer["x"]
        answer_y = answer["y"]
        print(f"State: {state}, Cor:{answer_x},{answer_y}")