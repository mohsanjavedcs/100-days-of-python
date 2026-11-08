import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

    states = df.state.to_list()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("_states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data["x"].item()), int(state_data["y"].item()))
        t.write(answer_state)