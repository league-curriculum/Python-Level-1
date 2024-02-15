import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 130  # the length of the flaming arms

# Make a new turtle
myTurtle = turtle.Turtle()  # ;

# Make the turtle shape 'turtle', .shape('turtle')
myTurtle.shape("turtle")  # ;

# Set the turtle width to 2
myTurtle.width(2)  # ;

# Set the turtle speed to max (0)
myTurtle.speed(0)  # ;

# Use a for loop to repeat all of the code below ONE time (we will change this later)
for i in range(25):
    # After the code is working to make the flame pattern you can change the pen color to a random color:  Enter the code to change the pen color to a random color here, hint: you can use the getRandomColor() function or the getNextColor() function
    myTurtle.pencolor(getRandomColor())

    # After the code is working to make the flame pattern you can change the fill color to a random color:  Enter the code to change the fill color to a random color here, hint: you can use the getRandomColor() function or the getNextColor() function
    myTurtle.fillcolor(getRandomColor())  # ;
    # myTurtle.fillcolor("orange")
    myTurtle.begin_fill()

    # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees will turn a full circle)
    myTurtle.right(360 / 8)  # ;
    # DRAW           Move the turtle 64 pixels
    myTurtle.forward(64)  # ;

    # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative numbers will turn the turtle counter-clockwise.)
    myTurtle.left(40)  # ;

    # DRAW FLAME     Move the turtle the distance in the variable flameSize
    myTurtle.forward(flameSize)  # ;

    #                Turn the turtle to the right 170 degrees
    myTurtle.right(170)  # ;

    #                Move the turtle the distance in the variable flameSize (again)
    myTurtle.forward(flameSize)  # ;

    #  TURN RIGHT    Turn the turtle 62 degrees to the right
    myTurtle.right(62)  # ;

    #  DRAW          Move the turtle the distance in the variable baseSize
    myTurtle.forward(baseSize)  # ;

    myTurtle.end_fill()

# Hide your turtle so you can see the pattern.
myTurtle.hideturtle()  # ;

# TEST   Run the program. Check that your shape is the same as the first picture in the recipe.
#        This is one arm of the ninja star.

# COLOR  Change the turtle's pen color so that the flame is a different color to the rest of the star.  Add code to change the color of the turtle's pen to a random color.
#        You can use code like this: myTurtle.pencolor(getRandomColor())  ** This will need to be added in the beginning of the for loop.

# Run the program again. Check the second picture in the recipe.

# LOOP   When you have one arm looking right, change your for loop to repeat 25 times.

# call the turtle .done() method
turtle.done()  # ;
