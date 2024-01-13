import random
import turtle as t
import time as T

Game_Width = 700
Game_Height = 700
Speed = 50
Padle_Color = "#FF0000"
Pong_Color = "#0000FF"
Background_Color = "#000000"
Padle1_height = 0
Padle2_height = 0
window = t.Screen()
winner = "the winner"

mult = -1

PAscore = 0
PBscore = 0

direction = "Up"

window.title("Ping Pong")
# window.resizable(True,True)

window.setup(width=Game_Width, height=Game_Height)
window.bgcolor(Background_Color)

window.tracer(0)
# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()


# Left Paddle
Lpaddle = t.Turtle()
Lpaddle.speed(0)
Lpaddle.shape("square")
Lpaddle.color(Padle_Color)
Lpaddle.shapesize(stretch_wid=10, stretch_len=1)
Lpaddle.penup()
Lpaddle.goto(-300, 100)

# Right Paddle
Rpaddle = t.Turtle()
Rpaddle.speed(0)
Rpaddle.shape("square")
Rpaddle.color(Padle_Color)
Rpaddle.shapesize(stretch_wid=5, stretch_len=1)
Rpaddle.penup()
Rpaddle.goto(300, 100)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(Pong_Color)
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()
ball.goto(0, 350)
ballx = 0.2
bally = 0.2

# Pen for updating score board
pen = t.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("score", align="center", font=('Arial', 24, 'normal'))

# mode
'''mode = (input("would you like to play easy or hard mode?"))
if mode.lower() == "hard":
    mult == -1.1
    T.sleep(3)
else:
    T.sleep(3)
    pass'''


# moving the Rpaddle
def Rpaddleup():
    y = Rpaddle.ycor()
    y = y + 50
    Rpaddle.sety(y)


def Rpaddledown():
    y = Rpaddle.ycor()
    y = y - 50
    Rpaddle.sety(y)


# Moving LPaddle
def Lpaddleup():
    y = Lpaddle.ycor()
    y = y + 50
    Lpaddle.sety(y)


def Lpaddledown():
    y = Lpaddle.ycor()
    y = y - 50
    Lpaddle.sety(y)


# Assign keys to play
window.listen()
window.onkeypress(Lpaddleup, 'w')
window.onkeypress(Rpaddleup, 'Up')
window.onkeypress(Lpaddledown, 's')
window.onkeypress(Rpaddledown, 'Down')


def game_over():
    ballx = 0
    bally = 0
    ball.goto(0, 2000)
    Lpaddle.goto(1000, 1000)
    Rpaddle.goto(1000, 1000)
    pen.clear()
    pen.write((winner + " is the winner"), align="center", font=('Arial', 24, 'normal'))


def AI():
    rand = 50  # random.randint(50, 100)
    rand2 = random.randint(1, 300)
    if int(rand2) == 1:
        Lpaddle.sety(Lpaddle.ycor() + rand)
    elif int(rand2) == 2:
        Lpaddle.sety(Lpaddle.ycor() - rand)
    print(rand2)


def check_paddle():
    if Lpaddle.ycor() > 300:
        Lpaddle.sety(Lpaddle.ycor() - 75)
    if Lpaddle.ycor() < -300:
        Lpaddle.sety(Lpaddle.ycor() + 75)
    if Rpaddle.ycor() > 300:
        Rpaddle.sety(Rpaddle.ycor() - 50)
    if Rpaddle.ycor() < -300:
        Rpaddle.sety(Rpaddle.ycor() + 50)


def move_ball():
    ball.setx(ball.xcor() + ballx)
    ball.sety(ball.ycor() + bally)


while True:
    window.update()
    AI()
    check_paddle()
    move_ball()

    LY = Lpaddle.ycor()
    RY = Rpaddle.ycor()

    rand = random.randint(0, 1)
    randint = 0
    if rand == 1:
        randint = 1
    else:
        randint = -1

    # Ball Border
    if ball.ycor() > 330:
        ball.sety(320)
        bally = (bally * randint)
    if ball.ycor() < -330:
        ball.sety(-320)
        bally = (bally * randint)

    if ball.xcor() > 350:
        # mult -= 0.01
        ballx = (ballx * -1)
        ball.goto(0, 0)
        # ballx = (ballx* mult)
        PAscore = PAscore + 1
        pen.clear()
        pen.write("player A:{}      Player B:{}".format(PAscore, PBscore), align='center', font=('Arial'))

    if ball.xcor() < -350:
        # mult -= 0.01
        ballx = (ballx * -1)
        ball.goto(0, 0)
        # ballx = (ballx*mult)
        PBscore = PBscore + 1
        pen.clear()
        pen.write("player A:{}      Player B:{}".format(PAscore, PBscore), align='center', font=('Arial'))

    if (((ball.xcor()) > 280) and ((ball.xcor()) < 320)) and (
            ((ball.ycor()) < (RY + 30)) and ((ball.ycor()) > (RY - 30))):
        ball.setx((ball.xcor() - 10))
        if mult < -1.6:
            mult -= 0.01
        if ballx < 0.5 and ballx > -0.5:
            ballx += 0.1
        ballx = (ballx * mult)

    if (((ball.xcor()) < -280) and ((ball.xcor()) > -320)) and (
            ((ball.ycor()) < (LY + 75)) and ((ball.ycor()) > (LY - 75))):
        ball.setx((ball.xcor() + 10))
        if mult < -1.6:
            mult -= 0.01
        if ballx < 0.5 and ballx > -0.5:
            ballx -= 0.1
        ballx = (ballx * mult)

    if PAscore >= 10:
        winner = "player A"
        game_over()
    else:
        pass
    if PBscore >= 10:
        winner = "player B"
        game_over()
    else:
        pass
    print(ballx, bally, mult)

window.mainloop()