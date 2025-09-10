# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Fredy Cortez
# Shraavan Sudhish
# Erick Lugo
# Bryson Tran
# Section: 509
# Assignment: Lab 13.00
# Date: 12 03 2023

import turtle
import random
import time
'''Let Program run for about 5 seconds before moving snake'''

delay = 0.1
# redefining turtle to become snake and setting snake attributes
snake = turtle.Turtle()

# Using a separate turtle to update score
turtle_score = turtle.Turtle()
turtle_hscore = turtle.Turtle()

def create_border():
    """Draws a 650x650 border. If the snake touches this border, the game resets. Also colors outside/inside the
    border."""
    global snake
    snake.speed(0)
    snake.goto(-400, 400)
    snake.pendown()
    snake.fillcolor("dark green")
    snake.begin_fill()
    for i in range(4):
        snake.forward(800)
        snake.right(90)
    snake.end_fill()
    snake.penup()
    snake.color("black")
    snake.goto(-325, 325)
    snake.pendown()
    snake.fillcolor("green")
    snake.begin_fill()
    for i in range(4):
        snake.forward(650)
        snake.right(90)
    snake.end_fill()
    snake.penup()
    snake.color("white")

def highscore_updater():
    """Uses a separate turtle that updates high score when the game ends"""
    global score
    global high_score
    global count
    turtle_hscore.hideturtle()
    turtle_hscore.speed(0)
    turtle_hscore.color("blue")
    turtle_hscore.penup()
    turtle_hscore.goto(-325, 330)
    turtle_hscore.pendown()
    if count == 0:
        turtle_hscore.write(f"High Score: {high_score}", font=("Arial", 50, "normal"))
        count = 1
    if score > high_score:
        high_score = score
        turtle_hscore.clear()
        turtle_hscore.write(f"High Score: {high_score}", font=("Arial", 50, "normal"))

def score_updater():
    """Uses a separate turtle that constantly updates the score when the snake eats an apple"""
    global score
    turtle_score.hideturtle()
    turtle_score.speed(0)
    turtle_score.color("red")
    turtle_score.penup()
    turtle_score.goto(100, 330)
    turtle_score.pendown()
    turtle_score.clear()
    turtle_score.write(f"Score: {score}", font=("Arial", 50, "normal"))

def snake_look_up():
    """Sets the snake direction to "up", this allows the snake to move up later with the
    move function. Even though the function has 1 line of code, the command window.onkeypress
    takes in a function as the first argument so that's why a function was made to do this."""
    if snake.direction != "down":
        snake.direction = "up"

def snake_look_down():
    """Sets the snake direction to "down", this allows the snake to move down later with the
    move function."""
    if snake.direction != "up":
        snake.direction = "down"

def snake_look_right():
    """Sets the snake direction to "right", this allows the snake to move right later with the
    move function."""
    if snake.direction != "left":
        snake.direction = "right"

def snake_look_left():
    """Sets the snake direction to "left", this allows the snake to move left later with the
    move function."""
    if snake.direction != "right":
        snake.direction = "left"

def control_snake():
    """This allows the snake to move. It takes the direction of the snake, and adds +20 to its position
    continuously. Also tried to move snake with snake.forward(), but the screen was too slow in recording
    the position of the snake that it had to be coded in increments of +20."""
    if snake.direction == "up":  # w key
        position = snake.ycor()
        snake.sety(position + 15)
    elif snake.direction == "left":  # a key
        position = snake.xcor()
        snake.setx(position - 15)
    elif snake.direction == "down":  # s key
        position = snake.ycor()
        snake.sety(position - 15)
    elif snake.direction == "right":  # d key
        position = snake.xcor()
        snake.setx(position + 15)
    else:
        pass

def game_end_early():
    """Moves snake in a position so the game can end"""
    snake.speed(0)
    snake.goto(-1000, 1000)
    snake.direction = "Stop"

def body_movement(body):
    """ Here we make every body_part move to the next body_part in reverse order except for the body_part closest to the
    snake head which follows the snake head"""
    if len(body) > 0:
        body[0].goto(snake.xcor(), snake.ycor())
    for i in range(len(body)-1,0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

def body_collisions():
    """Here we check for body_collisions; the function returns true if the coordinates of the snake head and snake body
       part are the same"""
    for i in body:
        if i.xcor() == snake.xcor() and i.ycor() == snake.ycor():
            return True
    return False

score = 0
high_score = 0
count = 0

# Screen for game
window = turtle.Screen()
window.setup(width=800, height=800)
window.bgcolor("black")

# Snake/Game Setup
snake.penup()
snake.goto(0, 0)
create_border()
highscore_updater()
score_updater()
snake.shape("square")
snake.direction = "Stop"

# Apple Setup
apple = turtle.Turtle()
apple.penup()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.goto(random.randint(-320, 320), random.randint(-320, 320))
apple.pendown()

#body_setup
body = []

# Allows the program to read input and changes the direction of snake based on input
window.listen()
window.onkeypress(snake_look_up, "w")
window.onkeypress(snake_look_left, "a")
window.onkeypress(snake_look_down, "s")
window.onkeypress(snake_look_right, "d")
window.onkeypress(game_end_early, "space")

# Prints game rules
print("You're now playing Snake Game")
print("Controls: press 'w' to move up, 's' to move down, 'a' to move left 'd' to move right")
print("Click space bar twice if you want to end the game early")
print("To play, have your snake touch the red apples to increase its size and score")
print("The better the score, the better the run was made by the player")
print("Goal: get the highest score possible without dying")
print("You can die by either touching the game border or your own body")
print("Good Luck!")

# Game Loop so window keeps refreshing
while True:
    window.update()
    control_snake()
    if (snake.xcor() + 10) >= -1000 >= (snake.xcor() - 10) and (
            snake.ycor() + 10) >= 1000 >= (snake.ycor() - 10):  # end game early using space bar
        with open("Scores list",  "a") as myfile:  # saves the score achieved on the current run
            myfile.write(f"Score achieved on run: {score}\n")
        print()
        print("You have ended the game early")
        review = True
        break
    if (snake.xcor() > 325 or snake.ycor() > 325 or snake.xcor() < -325 or snake.ycor() < -325) or body_collisions():  # if snake goes out
        # of bounds, restart game
        time.sleep(1)
        with open("Scores list.txt  ","a") as myfile:  # saves the score achieved on the current run
            myfile.write(f"Score achieved on run: {score}\n")
        for i in body:
            i.goto(1000,1000)
        body.clear()
        highscore_updater()
        score = 0
        score_updater()
        snake.goto(0, 0)
        snake.direction = "Stop"
        delay = 0.1
    if (apple.xcor() + 10) >= snake.xcor() >= (apple.xcor() - 10) and (
            apple.ycor() + 10) >= snake.ycor() >= (apple.ycor() - 10):  # Runs when snake touches the apple +- 10 of
        # the coordinates, if the snake coordinate was equal to apple coordinate, you would have to be really precise
        # and was honestly impossible to hit the apple

        # shortens the delay
        delay -= .010

        # adds to the size of the snake
        body_part = turtle.Turtle()
        body_part.penup()
        body_part.speed(0)
        body_part.shape("square")
        body_part.color("white")
        body.append(body_part)
        score += 1
        apple.penup()
        apple.goto(random.randint(-320, 320), random.randint(-320, 320))
        apple.pendown()
        score_updater()
    time.sleep(delay)
    body_movement(body)
if review:
    turtle.Screen().bye()
    try:  # gives the user the chance to rate the game, and writes their score in a file
        rating = float(input("Give us a rating from 1-5: "))
        with open("Scores list.txt", "a") as myfile:
            myfile.write(f"The score that the user gave from the experience is {rating}/5\n")
    except:  # if the user gives an invalid rating it prints an error statement
        print("Invalid rating")