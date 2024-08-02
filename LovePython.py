import turtle

# Setup turtle
pen = turtle.Turtle()
pen.speed(1)  # Fastest speed
pen.width(3)  # Thicker line

# Function to draw a curve for the heart
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Function to draw the heart
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

# Function to write text inside the heart
def txt():
    pen.up()
    pen.setpos(-70, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write("I LOVE YOU", font=("Verdana", 12, "bold"))



# Function to print the name below the heart
def print_name():
    pen.up()
    pen.setpos(-60, -150)
    pen.down()
    pen.color('blue')
    pen.write("by 0xcybervenom", font=("Verdana", 12, "bold"))
    pen.hideturtle()

# Draw heart, text, arrow, and print name
heart()
txt()
print_name()

# Hide the turtle and display the window
turtle.done()
