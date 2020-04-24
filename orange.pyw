import turtle
import time
import winsound
from tkinter import messagebox

# Creating important Variables
right_border_coordinates = 290
left_border_coordinates = -290
top_border_coordinates = 390
down_border_coordinates = -390

# Creating the Window
window = turtle.Screen()
window.title('Orange')
window.bgcolor('Green')
window.setup(width=800, height=600)
window.tracer(0)

# Creating the Title
title = turtle.Turtle()
title.speed(0)
title.color("White")
title.penup()
title.hideturtle()
title.goto(0, 270)
title.write('Orange', align="center", font=("Arial", 20, "normal"))

# Creating the Orange (Melek)
orange = turtle.Turtle()
orange.speed(0)
orange.shape('circle')
orange.color('orange')
orange.shapesize(stretch_wid=3, stretch_len=3)
orange.penup()
orange.goto(0, 0)
orange.dy = 20
orange.dx = 20

msg_box = messagebox.showinfo(
    "Orange", 
    """\
Controls:
    
    Movement:
        Up Arrow - Moves Up
        Down Arrow - Moves Down
        Left Arrow - Moves Left
        Right Arrow - Moves Right

        (+) - Increases Speed
        (-) - Decreases Speed
""")

# Functions

def orange_go_forward():
    orange.sety(orange.ycor() + orange.dy)

def orange_go_right():
    orange.setx(orange.xcor() + orange.dx)

def orange_go_back():
    orange.sety(orange.ycor() - orange.dy)

def orange_go_left():
    orange.setx(orange.xcor() - orange.dx)

def orange_increase_speed():
    if orange.dx >= 50:
        msg_box = messagebox.showwarning("Orange", "You've reached the Highest Speed")
    else:
        orange.dx += 5
        orange.dy += 5

def orange_decrease_speed():
    if orange.dx <= 5:
        message_box = messagebox.showwarning("Orange", "You've reached the lowest speed")
    else:
        orange.dx -= 5
        orange.dy -= 5

# Keybindings

window.listen()
window.onkeypress(orange_go_forward, "Up")
window.onkeypress(orange_go_right, "Right")
window.onkeypress(orange_go_back, "Down")
window.onkeypress(orange_go_left, "Left")
window.onkeypress(orange_increase_speed, "+")
window.onkeypress(orange_decrease_speed, "-")

try:
    while True:
        window.update()

        if orange.ycor() > right_border_coordinates:
            orange.goto(orange.xcor(), left_border_coordinates)
        
        if orange.ycor() < left_border_coordinates:
            orange.goto(orange.xcor(), right_border_coordinates)
        
        if orange.xcor() > down_border_coordinates:
            orange.goto(top_border_coordinates, orange.ycor())
        
        if orange.xcor() < top_border_coordinates:
            orange.goto(down_border_coordinates, orange.ycor())

    window.exitonclick()
except:
    pass
