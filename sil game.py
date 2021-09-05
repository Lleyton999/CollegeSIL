import math
import turtle
import os
import random
import winsound


#setting up the screen
mainscreen= turtle.Screen()
mainscreen.bgcolor('green')
mainscreen.title('space invaders')
mainscreen.bgpic('space invaders back grounf.gif')
mainscreen.tracer(0)


turtle.register_shape ('Space-Invaders-Free-PNG-Image.gif')
turtle.register_shape ('player-.gif')


#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()



score = 0


score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'score: %s' %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14,'normal'))
score_pen.hideturtle()


#create player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('player-.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player.speed = 0


#number of invaders
num_of_invaders = 30
invaders = []


for i in range(num_of_invaders):
    invaders.append(turtle.Turtle())

invader_start_x = -225
invader_start_y = 250
invader_number = 0


#create the invaders
for invader in invaders:
    invader.color('red')
    invader.shape('Space-Invaders-Free-PNG-Image.gif')
    invader.penup()
    invader.speed(0)
    x = invader_start_x + (50 * invader_number)
    y= invader_start_y
    invader.setposition(x,y)
    invader_number += 1
    if invader_number == 10:
        invader_start_y -=50
        invader_number = 0



invaderpos = 0.05








#create the bullet
bullet= turtle.Turtle()
bullet.color('purple')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()



bulletpos = 10

#bullet states
#ready
#firing
bulletstate = 'ready'

#move the player left and right
def move_left():
    player.speed = -1

def move_right():
    player.speed = 1


    player.setx(x)
def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = - 280
    if x > 280 :
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound("shoot", winsound.SND_ASYNC)
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor() ,2)+math.pow(t1.ycor()-t2.ycor() ,2))
    if distance < 15:
        return True
    else:
        return False




#create key binds
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')


#game loop
while True:
    mainscreen.update()
    move_player()

    for invader in invaders:
        #moving the invader
        x = invader.xcor()
        x += invaderpos
        invader.setx(x)


        if invader.xcor() > 280:
            for inva in invaders:

                y = inva.ycor()
                y -= 40
                inva.sety(y)
            invaderpos *= -1


        if invader.xcor() < -280:
            for inva in invaders:
                invaderpos *= -1
                y = inva.ycor()
                y -= 40
                inva.sety(y)
            invaderpos *= -1


        if iscollision(bullet, invader):
            winsound.PlaySound("invaderkilled", winsound.SND_ASYNC)
            # reset bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            # reset invader
            invader.setposition(0, 50000)
            score += 10
            scorestring = 'score: %s' % score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if iscollision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print('Game over!')
            break

    #moving the bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletpos
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'

    if score == 300:
        scorestring = "You Win! "
        score_pen.write(scorestring, False, font=("Arial", 72, "normal"))

mainscreen.mainloop()