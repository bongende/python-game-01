"""
simple plong in with python 3
By christo
part 1 getting started
"""

import turtle
import winsound

wn = turtle.Screen()
wn.title("Simple plong game by Christo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score

score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: {} + player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Functions for paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if paddle_a.ycor() > 240 :
        y = 240
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if paddle_a.ycor() < -240 :
        y = -240
    paddle_a.sety(y)



def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if paddle_b.ycor() > 240 :
        y = 240
    paddle_b.sety(y)



def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if paddle_b.ycor() < -240 :
        y = -240
    paddle_b.sety(y)


# Keyboard

wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop

while True:
    wn.update()
    """"
    ans = input("type \"yes\" if you want to continte")
    if ans == "yes": """

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Touche.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Touche.wav", winsound.SND_ASYNC)
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write("player A: {} + player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {} + player B: {} ".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))




    # paddle and ball collision

    if ball.xcor() > 330 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40 ) :
        ball.setx(330)
        winsound.PlaySound("Un seul pop.wav", winsound.SND_ASYNC)
        ball.dx *= -1
    if ball.xcor() < -330 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40 ) :
        ball.setx(-330)
        winsound.PlaySound("Un seul pop.wav", winsound.SND_ASYNC)
        ball.dx *= -1
