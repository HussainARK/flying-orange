import turtle
import time
import winsound
from tkinter import messagebox

def main():
    # Creating important Variables
    right_border = 390
    left_border = -390
    top_border = 290
    down_border = -290

    max_speed = 70
    lowest_speed = 5

    # Creating the Window
    window = turtle.Screen()
    window.title('Orange')
    window.bgcolor('Green')
    window.setup(width=800, height=600)
    window.tracer(0)

    # Creating the Orange (Melek)
    orange = turtle.Turtle()
    orange.speed(0)
    orange.shape('circle')
    orange.color('orange')
    orange.shapesize(stretch_wid=3, stretch_len=3)
    orange.penup()
    orange.goto(0, 0)
    orange.dy = 30
    orange.dx = 30

    # Creating the Title
    title = turtle.Turtle()
    title.speed(0)
    title.color("White")
    title.penup()
    title.hideturtle()
    title.goto(0, 270)
    title.write('Orange', align="center", font=("Arial", 20, "normal"))

    # Creating the Speed Monitor
    speed_monitor = turtle.Turtle()
    speed_monitor.speed(0)
    speed_monitor.color("White")
    speed_monitor.penup()
    speed_monitor.hideturtle()
    speed_monitor.goto(-290, -250)
    speed_monitor.write(f'Speed: {orange.dx}', align="center", font=("Arial", 10, "normal"))

    # Functions

    def show_help():
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

    def orange_go_forward():
        orange.sety(orange.ycor() + orange.dy)

    def orange_go_right():
        orange.setx(orange.xcor() + orange.dx)

    def orange_go_back():
        orange.sety(orange.ycor() - orange.dy)

    def orange_go_left():
        orange.setx(orange.xcor() - orange.dx)

    def orange_increase_speed():
        if orange.dx >= max_speed:
            msg_box = messagebox.showwarning("Orange", "You've reached the Highest Speed")
        else:
            orange.dx += lowest_speed
            orange.dy += lowest_speed
            speed_monitor.clear()
            speed_monitor.write(f'Speed: {orange.dx}', align="center", font=("Arial", 10, "normal"))


    def orange_decrease_speed():
        if orange.dx <= lowest_speed:
            message_box = messagebox.showwarning("Orange", "You've reached the lowest speed")
        else:
            orange.dx -= lowest_speed
            orange.dy -= lowest_speed
            speed_monitor.clear()
            speed_monitor.write(f'Speed: {orange.dx}', align="center", font=("Arial", 10, "normal"))

    # Keybindings

    window.listen()
    window.onkeypress(orange_go_forward, "Up")
    window.onkeypress(orange_go_right, "Right")
    window.onkeypress(orange_go_back, "Down")
    window.onkeypress(orange_go_left, "Left")

    window.onkeypress(orange_increase_speed, "+")
    window.onkeypress(orange_decrease_speed, "minus")

    window.onkeypress(show_help, "F1")

    try:
        while True:
            window.update()

            if orange.ycor() > top_border:
                orange.goto(orange.xcor(), down_border)
            
            if orange.ycor() < down_border:
                orange.goto(orange.xcor(), top_border)
            
            if orange.xcor() > right_border:
                orange.goto(left_border, orange.ycor())
            
            if orange.xcor() < left_border:
                orange.goto(right_border, orange.ycor())

        window.exitonclick()
    except:
        pass

main()
