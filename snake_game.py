# import modules
import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()  # create a window
wn.title("Snake Game")  # set the screen title to Snake Game
wn.bgcolor("yellow")  # set background colour to yellow
wn.setup(width=600, height=600)  # sets window screen to 600 pixels(width) x 600 pixels(height)
wn.tracer(0)  # turn off screen updates

# snake head
head = turtle.Turtle()  # initialize the head variable
head.speed(0)  # set the speed to 0
head.shape("square")  # set the head shape to square
head.color("black")  # set the head colour to black
head.penup()  # move snake without drawing the snake path
head.goto(0, 0)  # position the snake at x-coordinate - 0, y-coordinate - 0
head.direction = "stop"  # stop the snake from moving

# snake food
food = turtle.Turtle()  # initialize the food variable
food.speed(0)  # set the speed to 0
food.shape("square")  # set the food shape to square
food.color("red")  # set the food colour to red
food.penup()  # move the snake without drawing the snake path
food.goto(0, 100)  # position the food at x-coordinate - 0, y-coordinate - 100

segments = []  # to create the snake body

# scoreboards
sc = turtle.Turtle()  # initialize sc as the variable
sc.speed(0)  # set the speed to 0
sc.shape("square")  # set the scoreboard shape to square
sc.color("black")  # set the scoreboard colour to black
sc.penup()  # move snake without drawing the path
sc.hideturtle()  # hide the turtle
sc.goto(0, 260)  # position scoreboard at x-coordinate - 0 , y-coordinate - 260
# write the score and high score on the window screen
sc.write("score: 0  High score: 0", align="center", font=("ds-digital", 24, "normal"))


# Functions for directions
def go_up():  # move the snake up
    if head.direction != "down":
        head.direction = "up"


def go_down():  # move the snake down
    if head.direction != "up":
        head.direction = "down"


def go_left():  # move the snake left
    if head.direction != "right":
        head.direction = "left"


def go_right():  # move the snake right
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()  # y-coordinate of the turtle
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()  # y-coordinate of the turtle
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()  # x-coordinate of the turtle
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()  # x-coordinate of the turtle
        head.setx(x + 20)

# keyboard bindings
wn.listen()  # to detect the keys the user press
wn.onkeypress(go_up, "w")  # click on w key to move snake up
wn.onkeypress(go_down, "s")  # click on s key to move snake down
wn.onkeypress(go_left, "a")  # click on a key to move snake left
wn.onkeypress(go_right, "d")  # click on d key to move snake right

# Main loop
while True:
    wn.update()  # update window screen

    # check collision with border area
    # coordinates of the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # stop the game for one second
        head.goto(0, 0)  # get snake back to original position at x-coordinate - 0, y-coordinate - 0
        head.direction = "stop"  # stop the snake from moving
        # food.goto(0,100) # get food to original position

        # hide the segments of body
        for segment in segments:
            segment.goto(1000, 1000)  # out of window range
        # clear the segments
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        sc.clear()
        # Update the score and high score
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

    # check collision with food
    if head.distance(food) < 20:  # distance between snake head and food
        # move the food to random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)  # new position

        # add a new segment to the head
        new_segment = turtle.Turtle()  # initialize the new_segment variable
        new_segment.speed(0)  # set the speed to 0
        new_segment.shape("square")  # set the new_segment head to square
        new_segment.color("black")  # set the new_segment colour to black
        new_segment.penup()  # move the snake without drawing the snake path
        segments.append(new_segment)  # add new_segment to segments

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        # set new high score
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

    # move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # call the move function

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:  # distance between segment and head
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # food.goto(0,100) # get food to original position

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # out of window range
            # clear the segments
            segments.clear()
            # reset the score
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                     font=("ds-digital", 24, "normal"))
    time.sleep(delay)  # to reduce snake speed
wn.mainloop()  # start event loop