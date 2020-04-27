import turtle
import winsound
import math
from tkinter import messagebox

def main():
    # Creating Some Variables
    right_border = 390
    left_border = -390
    top_border = 290
    down_border = -290
    msg_title = "Orange"

    orange_max_speed = 50
    orange_lowest_speed = 10
    orange_default_speed = 25

    enemy_speed = 1.0

    # Creating the Window
    window = turtle.Screen()
    window.title('Orange')
    window.bgcolor('White')
    window.setup(width=800, height=600)
    window.tracer(0)

    # Creating the Orange (Player)
    orange = turtle.Turtle()
    orange.speed(0)
    orange.shape('circle')
    orange.color('orange')
    orange.shapesize(stretch_wid=3, stretch_len=3)
    orange.penup()
    orange.goto(0, 0)
    orange.dy = orange_default_speed
    orange.dx = orange_default_speed

    # Creating the Vegetable (Enemy)
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape('square')
    enemy.color('gray')
    enemy.shapesize(stretch_wid=5, stretch_len=1)
    enemy.penup()
    enemy.goto(100, 100)
    enemy.dx = enemy_speed
    enemy.dy = enemy_speed

    # Creating the Title
    title = turtle.Turtle()
    title.speed(0)
    title.color("Black")
    title.penup()
    title.hideturtle()
    title.goto(0, 270)
    title.write('Orange', align="center", font=("Arial", 20, "normal"))

    # Creating the Speed Monitor
    speed_monitor = turtle.Turtle()
    speed_monitor.speed(0)
    speed_monitor.color("Black")
    speed_monitor.penup()
    speed_monitor.hideturtle()
    speed_monitor.goto(-290, -250)
    speed_monitor.write(f'Speed: {orange.dx}', align="center", font=("Arial", 10, "normal"))

    # Functions

    def exit_game():
        exit()
    
    def refresh_pen(turtle_pen):
        turtle_pen.clear()
        turtle_pen.write(f'Speed: {orange.dx}', align="center", font=("Arial", 10, "normal"))

    def pause_game():
        msg_answer = messagebox.askyesno(msg_title, "Game Paused, Do you want to continue?")

        if msg_answer == True:
            pass
        elif msg_answer == False:
            window.bye()

    def restart_game():
        orange.goto(0, 0)
        orange.dx = orange_default_speed
        orange.dy = orange_default_speed
        enemy.goto(100, 100)
        refresh_pen(speed_monitor)

    def check_collision(turtle1, turtle2):
        d = math.sqrt(
            (turtle1.xcor() - turtle2.xcor()) ** 2
            +
            (turtle1.ycor() - turtle2.ycor()) ** 2
        )
        
        if d < 20:
            return True
        else:
            return False

    def show_help():
        msg_box = messagebox.showinfo(
            msg_title, 
            """\
Help:
    Controls:
        
        Movement:
            Up Arrow - Moves Up
            Down Arrow - Moves Down
            Left Arrow - Moves Left
            Right Arrow - Moves Right

            (+) - Increases Speed
            (-) - Decreases Speed

        Other:
            (F1) - Displays this Help Box
            (Space) - Pauses the Game
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
        if orange.dx >= orange_max_speed:
            msg_box = messagebox.showwarning(msg_title, "You've reached the Highest Speed")
        else:
            orange.dx += 5
            orange.dy += 5

    def orange_decrease_speed():
        if orange.dx <= orange_lowest_speed:
            message_box = messagebox.showwarning(msg_title, "You've reached the lowest speed")
        else:
            orange.dx -= 5
            orange.dy -= 5

    msg_answer = messagebox.askyesno(msg_title, 
    """\
Welcome to the Flying Orange Game,
People are throwing sticks on you to eat you.
So, You should not touch them.

Do you want to play the Game?
""")

    if msg_answer == True:
        pass
    else:
        exit_game()

    # Keybindings

    window.listen()
    window.onkeypress(orange_go_forward, "Up")
    window.onkeypress(orange_go_right, "Right")
    window.onkeypress(orange_go_back, "Down")
    window.onkeypress(orange_go_left, "Left")

    window.onkeypress(orange_increase_speed, "+")
    window.onkeypress(orange_decrease_speed, "minus")

    window.onkeypress(show_help, "F1")
    window.onkeypress(pause_game, "space")

    try:
        while True:
            window.update()

            enemy.setx(enemy.xcor() + enemy.dx)
            enemy.sety(enemy.ycor() + enemy.dy)

            if orange.ycor() > top_border:
                orange.goto(orange.xcor(), down_border)
            
            if orange.ycor() < down_border:
                orange.goto(orange.xcor(), top_border)
            
            if orange.xcor() > right_border:
                orange.goto(left_border, orange.ycor())
            
            if orange.xcor() < left_border:
                orange.goto(right_border, orange.ycor())



            if enemy.ycor() > top_border:
                enemy.goto(enemy.xcor(), down_border)
            
            if enemy.ycor() < down_border:
                enemy.goto(enemy.xcor(), top_border)
            
            if enemy.xcor() > right_border:
                enemy.goto(left_border, enemy.ycor())
            
            if enemy.xcor() < left_border:
                enemy.goto(right_border, enemy.ycor())



            if check_collision(orange, enemy):
                winsound.PlaySound('lose.wav', winsound.SND_ASYNC)
                msg_answer = messagebox.askretrycancel('Orange', 'You losed, Do you want to retry?')
                if msg_answer == True:
                    restart_game()
                else:
                    exit_game()
            
            refresh_pen(speed_monitor)
    except:
        pass

main()
