import turtle
import random

window = turtle.Screen()
window.screensize(600,600)  
window.bgcolor("light blue")
window.title("Catch The Turtle")

gamer = turtle.Turtle()
gamer.color("green")
gamer.shapesize(2)
gamer.penup()

score = 0

point = turtle.Turtle()
point.speed(0)
point.shape("square")
point.color("white")
point.penup()
point.hideturtle()
point.goto(-200,200)
point.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))

speed = 1

max_aim = 5
aims = []
for i in range(max_aim):
    aims.append(turtle.Turtle())
    aims[i].penup()
    aims[i].shape("turtle")
    aims[i].color("orange")
    aims[i].speed(0)
    aims[i].setposition(random.randint(-300, 300), random.randint(-300, 300))

def turnLeft():
    gamer.left(30)


def turnRight():
    gamer.right(30)


def increaseSpeed():
    global speed
    speed = speed + 1    

def decreaseSpeed():
    global speed
    speed = speed - 1

window.listen()
window.onkey(turnLeft, 'Left')
window.onkey(turnRight, 'Right')
window.onkey(increaseSpeed, 'Up')
window.onkey(decreaseSpeed, 'Down')

while True:
    gamer.forward(speed)

    if gamer.xcor() > 340 or gamer.xcor() < -340:
        print("GAME OVER")
        quit()
    if gamer.ycor() > 300 or gamer.ycor() < -300:
        print("GAME OVER")
        quit()

    for i in range(max_aim):
        aims[i].forward(1)

        if aims[i].xcor() > 500 or aims[i].xcor() < -500:
            aims[i].right(random.randrange(150, 250))
        if aims[i].ycor() > 500 or aims[i].ycor() < -500:
            aims[i].right(random.randrange(150, 250))

        if gamer.distance(aims[i]) < 30:
            aims[i].setposition(random.randint(-290, 290), random.randint(-290, 290))
            aims[i].right(random.randint(0, 360))
            score = score + 1
            point.clear()
            point.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))

turtle.done()