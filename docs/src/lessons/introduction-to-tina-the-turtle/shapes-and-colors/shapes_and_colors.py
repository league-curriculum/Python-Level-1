import turtle as turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
myTurtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
myTurtle.shape('turtle')  # ;

# Set your turtle's speed using .speed(2)
myTurtle.speed(0)  # ;

# Set your turtle's color using .color('green') and .pencolor('blue')
myTurtle.color('green')  # ;
myTurtle.pencolor('blue')  # ;

# Move your turtle forward using .forward(100)
myTurtle.forward(100)  # ;

# Move your turtle left or right using .left(90) or .right(90)
myTurtle.left(90)  # ;
myTurtle.forward(100)  # ;

# Now put the forward and left/right code into a for loop to repeat 4 times.
# Did your Robot draw a square?
for i in range(4):  # ;
    myTurtle.forward(100)  # ;
    myTurtle.right(90)  # ;

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
myTurtle.goto(-100,-100)  # ;

# Have your turtle draw a circle using .circle(radius, steps=50)
myTurtle.begin_fill()  # ;
myTurtle.circle(100, steps=50)  # ;
myTurtle.end_fill()  # ;

# Add color to your shape by adding .begin_fill() before drawing the shape
# and .end_fill() after

# Draw 3 more shapes with different fill colors!
# Draw a triangle  # ;
myTurtle.goto(100,100)  # ;
myTurtle.begin_fill()  # ;
for i in range(3):  # ;
    myTurtle.forward(100)  # ;
    myTurtle.right(120)  # ;
myTurtle.end_fill()  # ;

# Draw a pentagon  # ;
myTurtle.goto(-100,100)  # ;
myTurtle.begin_fill()  # ;
for i in range(5):  # ;
    myTurtle.forward(100)  # ;
    myTurtle.right(72)  # ;
myTurtle.end_fill()  # ;

# Draw a hexagon  # ;
myTurtle.goto(100,-100)  # ;
myTurtle.begin_fill()  # ;
for i in range(6):  # ;
    myTurtle.forward(100)  # ;
    myTurtle.right(60)  # ;
myTurtle.end_fill()  # ;


# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
