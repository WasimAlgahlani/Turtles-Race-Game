from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle is going to win the race? Enter a color: ")
y_pos = -100
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-235, y=y_pos)
    all_turtles.append(new_turtle)
    y_pos += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winner = turtle.fillcolor()
            is_race_on = False
            break
        turtle.forward(random.randint(0, 10))

if user_bet == winner:
    print(f"You win! The {winner} is the winner.")
else:
    print(f"You lose! The {winner} is the winner.")
screen.exitonclick()
