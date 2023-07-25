# 2022-12-17 16:26:58

import turtle
import pandas


states_data = pandas.read_csv(
    "./Day 25/229 us-states-game-start/us-states-game-start/50_states.csv"
)
state_list = (states_data["state"]).to_list()

typer_turtle = turtle.Turtle()
typer_turtle.penup()
typer_turtle.hideturtle()

screen = turtle.Screen()
score = 0
screen.title("U.S. States Game ")
gif_shape = (
    "./Day 25/229 us-states-game-start/us-states-game-start/blank_states_img.gif"
)
screen.addshape(gif_shape)
turtle.shape(gif_shape)
correct_guesses = []

while score < 50:
    state_index = -1
    guess_state_popup = screen.textinput(
        title=f"Guess the State ({score}/50)", prompt="Whats another State."
    )

    if guess_state_popup.title() == "Exit":
        break
    # if guess_state_popup.title() in correct_guesses == False:
    for state in state_list:
        state_index += 1
        if (state) == guess_state_popup.title():
            cordinate_data = (
                states_data[states_data.state == guess_state_popup.title()]
            ).to_dict()
            # print(states_data.index("state"==state))
            # print(cordinate_data)
            # print(state_index)
            x_cor = int(cordinate_data["x"][state_index])
            y_cor = int(cordinate_data["y"][state_index])
            typer_turtle.goto(x_cor, y_cor)
            typer_turtle.pendown()
            typer_turtle.write(f"{state}")
            typer_turtle.penup()
            score += 1
            correct_guesses.append(state)

missing_states_list = []
c = None
for a_s in state_list:
    if a_s in correct_guesses:
        pass
    else:
        missing_states_list.append(a_s)
        # c=a_s
print(state_list)
print(correct_guesses)
missing_states_dict = {"missing_state": missing_states_list}

d = pandas.DataFrame(missing_states_dict)

d.to_csv("./Day 25/229 us-states-game-start/us-states-game-start/missing_states.csv")


# print(guess_state_popup)
# turtle.mainloop()
# screen.exitonclick()
