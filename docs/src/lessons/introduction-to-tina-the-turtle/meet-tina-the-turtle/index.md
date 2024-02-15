---
title: Meet Tina the Turtle

---


# Meet Tina the Turtle

Tina is a Turtle that you control with code.  Press run to see what this program does, and see if you can figure out what line tells Tina to say,`"Why, hello there!"`

<iframe width="100%" height="600" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=%23%20Tina%20The%20Turtle%20from%20https%3A//trinket.io/eric-busboom/courses/introduction-to-python-programming%0A%0Aimport%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Atina.forward%2820%29%0Atina.write%28%22Why%2C%20hello%20there%21%22%29%0Atina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Don't worry if you don't understand all of the code.  You don't have to to get started, and more and more of it will become familiar to you as you keep going.

As we saw in the last example, Tina can move!  When she moves, she draws a line.  She can move `forward` and `backward` and turn `right` or `left` a certain number of degrees.

Run this example to see her move:

<iframe width="100%" height="600" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%22turtle%22%29%0A%0Atina.forward%2850%29%0Atina.left%2890%29%0Atina.forward%2850%29%0Atina.left%2890%29%0Atina.forward%2850%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Turtles like Tina have a pen that draws when they move.  We can tell them to pick the pen up, so that they can move without drawing a line.  Then we can tell them to put the pen down, and they'll draw again.  We tell them this with the `penup()` and `pendown()` commands.

<iframe width="100%" height="600" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Atina.goto%280%2C100%29%0Atina.write%28%22I%20don%27t%20draw%20when%20my%20pen%20is%20up%21%22%29%0Atina.goto%280%2C50%29%0Atina.pendown%28%29%0Atina.write%28%22I%20do%20draw%20when%20my%20pen%20is%20down%21%22%29%0Atina.goto%28-50%2C50%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Thanks to [Tinket](https://trinket.io/) for the original Tina code. 
