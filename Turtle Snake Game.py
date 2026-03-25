import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle Snake Game")
screen.screensize(600,600)
screen.bgcolor("yellow")
screen.tracer(0)



snake=turtle.Turtle()
snake.speed(8)
snake.fillcolor("black")
snake.shape("square")
snake.penup()
snake.home()
snake.direction = "stop"

food=turtle.Turtle()
food.fillcolor("red")
food.shape("square")
food.penup()
food.home()
food.goto(0,100)

numscore=0
score=turtle.Turtle()
score.penup()
score.goto(0,260)
score.write(f"Score={numscore}",align="center",font=("ds-digital", 24, "normal"))
score.hideturtle()

def go_up():
    if snake.direction !="down":
        snake.direction ="up"

def go_down():
    if snake.direction !="up":
        snake.direction ="down"

def go_left():
    if snake.direction !="right":
        snake.direction ="left"

def go_right():
    if snake.direction !="left":
        snake.direction ="right"

def move():
    if snake.direction =="up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")


segment = []

while True:
    time.sleep(0.5)    
    screen.update()

    if snake.distance(food) <20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        newsnake= snake.clone()
        segment.append(newsnake)
        numscore+=1
        score.clear()
        score.write(f"Score={numscore}",align="center",font=("ds-digital", 24, "normal"))


    for index in range(len(segment) -1, 0, -1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)

    if len(segment)>0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x,y)

    move()


screen.mainloop()
