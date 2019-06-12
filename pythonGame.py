'''
Created on Jun 11, 2019

@author: jonicmecija
'''
import turtle
import os 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Game")

#border
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

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setpos(0, -250)
player.setheading(90)

playerspeed = 15 

#make player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.25,0.25)
bullet.hideturtle()

bulletspeed = 20

#define the bullet state

#state 1: ready to fire
bulletstate = "ready"

#state 2: fire, bullet is firing
#move the player left and right
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x+= playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    
    x = player.xcor()
    y = player.ycor()
    
    bullet.setposition(x, y + 10)
    bullet.showturtle()
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "a") 
turtle.onkey(move_right, "d")

#create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setpos(-200,250)

enemyspeed=5



#main game loop
while True:
    
    #move the enemy
    x = enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)
    
    if x > 280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        
    if x < -280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        
        
    
    
wn.exitonclick()
