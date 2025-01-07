from turtle import Turtle, Screen
timmy=Turtle()
screen=Screen()
def move_forward():
    timmy.forward(10)

def move_right():
    timmy.right(10)

def move_left():
    timmy.left(10)

def move_backward():
    timmy.backward(10)

def clear():
    timmy.penup()
    timmy.clear()
    timmy.setposition(0,0)
    timmy.pendown()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='space', fun=clear)


screen.exitonclick()
