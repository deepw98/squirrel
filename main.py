import turtle as t
import time
import random
screen = t.Screen()
screen.setup(800, 700)
# co-ordinates for creating the main snake body
seg_pos = [(0, 0), (-20, 0), (-40, 0)]
# List for storing turtle objects for creating snake body
seg_list = []
screen.tracer(0)


# The function for creating snake body
def body():
    t_obj = t.Turtle("square")
    t_obj.hideturtle()
    screen.tracer(0)
    t_obj.color("red")
    t_obj.penup()
    if for_original:
        t_obj.goto(pos)
        t_obj.showturtle()
    screen.update()
    seg_list.append(t_obj)


# Loop for creating original turtle body
for pos in seg_pos:
    for_original = True
    body()


# Functions for movement of snake body
def do_up():
    if seg_list[0].heading() != 270:
        seg_list[0].setheading(90)


def do_down():
    if seg_list[0].heading() != 90:
        seg_list[0].setheading(270)


def do_left():
    if seg_list[0].heading() != 0:
        seg_list[0].setheading(180)


def do_right():
    if seg_list[0].heading() != 180:
        seg_list[0].setheading(0)


# Function for creating snake food in random coordinates
def food():
    list_x = []
    list_y = []
    for pos1 in range(380, -390, -10):
        list_x.append(pos1)
    for pos2 in range(280, -330, -10):
        list_y.append(pos2)

    pos_x = random.choice(list_x)
    pos_y = random.choice(list_y)
    t.penup()
    t.goto(pos_x, pos_y)
    t.dot(10)
    t.hideturtle()


# Creating turtle for score writing
score = 0
t_write = t.Turtle()
t_write.hideturtle()
pen = t_write.getpen()

#Creating squirrel
squ = t.Turtle("square")
squ.color("brown")
squ.penup()
squ.goto(0, 30)

# For squirrel score
squ_score = 0
s_write = t.Turtle()
s_write.hideturtle()
pen2 = s_write.getpen()


# Function for score writing
def write(score):
    t_write.penup()
    t_write.hideturtle()
    t_write.goto(x=-50, y=300)

    pen.clear()
    pen.write(f"Score:{score}", font=("calibari", 20, "bold"))

# For squirrel score writing
def write2(squ_score):
    s_write.penup()
    s_write.hideturtle()
    s_write.goto(x=-300, y=305)
    pen2.clear()
    pen2.write(f"Squirrel Score: {squ_score}", font=("calibari", 15, "bold"))


# Setting first score as zero for both snake and squirrel
write(0)
write2(0)

# Creating turtle for drawing a line to separate the score and the game
t_line = t.Turtle()
t_line.hideturtle()
t_line.penup()
t_line.goto(x=-550, y=291)
t_line.pendown()
t_line.goto(x=550, y=291)

screen.listen()      # function for being able to use keyboard
moving = True       # Setup for moving loop
food()             # Generating first food

# Function for moving the squirrel
def go_on():
    squ.setheading(0)
    if squ.xcor() != t_x:
        if t_x > squ.xcor():
            squ.forward(6)
            print(squ.xcor())
        if t_x < squ.xcor():
            squ.back(6)
    squ.setheading(90)

    if squ.ycor() != t_y:
        if t_y > squ.ycor():
            squ.forward(6)
        if t_y < squ.ycor():
            squ.back(6)


# Moving loop is used for making the snake move constantly
while moving:
    screen.update()     # It is used so that the new segments of turtle
    time.sleep(0.1)    # It is used for slowing the turtle down enough to move
    seg_list[0].speed(5)

    # This for block is used for the various segments to follow each other in various direction
    # even after appended with new segments
    for seg in range(len(seg_list)-1, 0, -1):
        new_x = seg_list[seg-1].xcor()
        new_y = seg_list[seg-1].ycor()
        seg_list[seg].goto(new_x, new_y)
        seg_list[seg].showturtle()
    # print(seg_list[0].pos())
    t_x = t.xcor()    # food turtle x- coordinate
    t_y = t.ycor()    # food turtle y- coordinate

    go_on()          # Using the function for squirrel movement

    # This if block is used for replacing food that is black dot with white dot and
    # Creating new food and incrementing the score for both snake and squirrel
    if t_x+12 > seg_list[0].xcor() > t_x-12:
        if t_y+12 > seg_list[0].ycor() > t_y-12:
            t.goto(t_x, t_y)
            t.dot(10, "white")
            screen.update()
            for_original = False
            body()
            screen.update()
            food()
            score += 1
            write(score)

    elif t_x + 10 > squ.xcor() > t_x - 10:
        if t_y + 10 > squ.ycor() > t_y - 10:
            t.goto(t_x, t_y)
            t.dot(10, "white")
            screen.update()
            for_original = False
            screen.update()
            food()
            squ_score += 1
            write2(squ_score)

    # This if block is used for collision of snake with left and right walls
    if seg_list[0].xcor() > 380 or seg_list[0].xcor() < -390:
        t_stop = t.Turtle()
        t_stop.hideturtle()
        t_stop.penup()
        t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
        t_stop.goto(-135, -40)
        t_stop.write("You lost!! The snake is dead", font=("caliberi", 20, "bold"))
        t_stop.goto(-135, -80)
        t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
        break
    # This if block is used for collision of snake with up and down walls
    if seg_list[0].ycor() > 280 or seg_list[0].ycor() < -330:
        t_stop = t.Turtle()
        t_stop.hideturtle()
        t_stop.penup()
        t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
        t_stop.goto(-135, -40)
        t_stop.write("You lost!! The snake is dead", font=("caliberi", 20, "bold"))
        t_stop.goto(-135, -80)
        t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
        break

    # Making the snake always move forward
    seg_list[0].forward(10)

    # Making the keyboard keys operable
    screen.onkey(key="Up", fun=do_up)
    screen.onkey(key="Down", fun=do_down)
    screen.onkey(key="Left", fun=do_left)
    screen.onkey(key="Right", fun=do_right)
    # Creating a second list without the first segment of snake and
    # calling the first segment head
    seg_list2 = []
    for i in range(1, len(seg_list)):
        seg_list2.append(seg_list[i])
    head = seg_list[0]
    flag = 1

    # This for loop is used for detection of collision of snake with its tail
    for segments in seg_list2:
        if head.distance(segments) < 5:
            flag = 0
            t_stop = t.Turtle()
            t_stop.hideturtle()
            t_stop.penup()
            t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
            t_stop.goto(-135, -40)
            t_stop.write("You lost!!The snake bit itself", font=("caliberi", 20, "bold"))
            t_stop.goto(-135, -80)
            t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
            break

    if flag == 0:
        break

    if score == 10 or squ_score == 10:
        if score > squ_score:
            stop2 = t.Turtle()
            stop2.hideturtle()
            stop2.penup()
            stop2.write("Game over", align="center", font=("caliberi", 40, "bold"))
            stop2.goto(-120, -60)
            stop2.write("You won!!", align="center", font=("caliberi", 40, "bold"))
            break
        if score < squ_score:
            stop2 = t.Turtle()
            stop2.hideturtle()
            stop2.penup()
            stop2.write("Game over", align="center", font=("caliberi", 40, "bold"))
            stop2.goto(0, -60)
            stop2.write("You lost!!", align="center", font=("caliberi", 40, "bold"))
            break

# Exit game after clicking on screen
screen.exitonclick()
