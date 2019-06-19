'''
Created on Jun 18, 2019

@author: jonicmecija
'''

import os
import turtle


#create window

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pong")

#create border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

#create player1 left
p1 = turtle.Turtle()
p1.shape("square")
p1.color("blue")
p1.shapesize(5, 1, 1)
p1.speed(0)
p1.penup()
p1.setpos(-280, 15)

playerspeed = 15
#create player2 right

p2 = turtle.Turtle()
p2.shape("square")
p2.color("red")
p2.shapesize(5, 1, 1)
p2.speed(0)
p2.penup()
p2.setpos(280, 15)

playerspeed2 = 15

def move_up():
    y = p1.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    p1.sety(y)

def move_down():
    y = p1.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    p1.sety(y)
    
def move_up2():
    y = p2.ycor()
    y += playerspeed2
    if y > 280:
        y = 280
    p2.sety(y)

def move_down2():
    y = p2.ycor()
    y -= playerspeed2
    if y < -280:
        y = -280
    p2.sety(y)


#create keyboard bindings
turtle.listen()
turtle.onkey(move_up, "w") 
turtle.onkey(move_down, "s") 
turtle.onkey(move_up2, "Up") 
turtle.onkey(move_down2, "Down") 

wn.exitonclick()
