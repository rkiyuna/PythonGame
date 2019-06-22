'''
Created on Jun 11, 2019

'''
import turtle
import os 
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

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

#create the player 
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
def fire_bullet():
    global bulletstate
    
    if bulletstate == "ready":
        bulletstate = "fire"

        x = player.xcor()
        y = player.ycor()
        
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# PLAYER MOVEMENT
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

#KEYBINDINGS 
turtle.Screen().listen()
turtle.Screen().onkey(move_left, "a")
turtle.Screen().onkey(move_right, "d")
turtle.Screen().onkey(fire_bullet, "space")

#create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle") 
enemy.penup()
enemy.speed(0)
enemy.setpos(-200,250)
enemyspeed = 2

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
    
     #move the bullet
    y=bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
    
    #check if bullet has gone to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #check for collision between bullet and enemy
    if isCollision(bullet, enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #reset the enemy
        enemy.setposition(-200,250)
         
        
    
    
wn.exitonclick()
