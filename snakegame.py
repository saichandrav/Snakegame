import turtle
import time
import random

delay = 0.19
score = 0
highscore = 0

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Snake Game")

# Snake head
headofsnake = turtle.Turtle()
headofsnake.speed(0)
headofsnake.shape("square")
headofsnake.color("green")
headofsnake.penup()
headofsnake.goto(0,0)
headofsnake.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)

# Score text
text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f"score : {score}  High Score : {highscore}", align="center", font=("ariel", 17, "normal"))

snake_body = []

# Movement functions
def go_up():
    if headofsnake.direction != "down":
        headofsnake.direction = "up"

def go_down():
    if headofsnake.direction != "up":
        headofsnake.direction = "down"

def go_left():
    if headofsnake.direction != "right":
        headofsnake.direction = "left"

def go_right():
    if headofsnake.direction != "left":
        headofsnake.direction = "right"

def move():
    if headofsnake.direction == "up":
        y = headofsnake.ycor()
        headofsnake.sety(y + 20)
    if headofsnake.direction == "down":
        y = headofsnake.ycor()
        headofsnake.sety(y - 20)
    if headofsnake.direction == "left":
        x = headofsnake.xcor()
        headofsnake.setx(x - 20)
    if headofsnake.direction == "right":
        x = headofsnake.xcor()
        headofsnake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 's')
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_right, 'd')

# Main game loop with crash-safe exit
try:
    while True:
        screen.update()

        # Check collision with wall
        if headofsnake.xcor() < -290 or headofsnake.xcor() > 290 or headofsnake.ycor() < -290 or headofsnake.ycor() > 290:
            time.sleep(1)
            headofsnake.goto(0,0)
            headofsnake.direction = "stop"
            for k in snake_body:
                k.goto(1000, 1000)
            snake_body.clear()
            score = 0
            delay = 0.1
            text.clear()
            text.write(f"score : {score}  High Score : {highscore}", align="center", font=("ariel", 17, "normal"))

        # Check collision with food
        if headofsnake.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            tail = turtle.Turtle()
            tail.speed(0)
            tail.shape("square")
            tail.color("light green")
            tail.penup()
            snake_body.append(tail)

            delay -= 0.001
            score += 1
            if score > highscore:
                highscore = score
            text.clear()
            text.write(f"score : {score}  High Score : {highscore}", align="center", font=("ariel", 17, "normal"))

        # Move the end segments first in reverse order
        for i in range(len(snake_body) - 1, 0, -1):
            x = snake_body[i - 1].xcor()
            y = snake_body[i - 1].ycor()
            snake_body[i].goto(x, y)

        # Move segment 0 to head
        if len(snake_body) > 0:
            x = headofsnake.xcor()
            y = headofsnake.ycor()
            snake_body[0].goto(x, y)

        move()

        # Check collision with body
        for k in snake_body:
            if k.distance(headofsnake) < 20:
                time.sleep(1)
                headofsnake.goto(0,0)
                headofsnake.direction = "stop"
                for k in snake_body:
                    k.goto(1000, 1000)
                snake_body.clear()
                score = 0
                delay = 0.1
                text.clear()
                text.write(f"score : {score}  High Score : {highscore}", align="center", font=("ariel", 17, "normal"))

        time.sleep(delay)

except turtle.Terminator:
    pass  # User closed the window
