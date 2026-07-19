import turtle
screen=turtle.Screen()
slow_turtle=turtle.Turtle()
slow_turtle.shape("turtle")
slow_turtle.forward(100)
slow_turtle.right(90)
slow_turtle.forward(100)
slow_turtle.pensize(10)
slow_turtle.right(90)
slow_turtle.forward(100)
slow_turtle.color("lightSkyBlue")
slow_turtle.pensize(16)
slow_turtle.right(90)
slow_turtle.forward(100)

r = 0
g = 0
b = 0

# turtle.colormode(255)

size = 1
for i in range(400):
    # slow_turtle.color(r, g, b)
    slow_turtle.pensize(size)
    slow_turtle.forward(100)
    slow_turtle.right(90)
    size = size + 20100
    # r = r + 1
    # g = g + 1
    # b = b + 30

screen.mainloop()














































































