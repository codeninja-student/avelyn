import turtle
screen=turtle.Screen()
slow_turtle=turtle.Turtle()
size=100
for i in range(4):
    slow_turtle.forward(size)
    slow_turtle.right(90)
for i in range(5):
    slow_turtle.circle(radius)
    radius +=10
screen.mainloop()