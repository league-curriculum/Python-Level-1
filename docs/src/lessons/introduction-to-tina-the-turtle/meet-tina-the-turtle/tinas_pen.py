import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(0,100)
tina.write("I don't draw when my pen is up!")
tina.goto(0,50)
tina.pendown()
tina.write("I do draw when my pen is down!")
tina.goto(-50,50)
