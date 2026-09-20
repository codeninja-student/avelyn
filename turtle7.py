import turtle
screen=turtle.Screen()
slow_turtle=turtle.Turtle()
size=100
for i in range(4):
    slow_turtle.forward(size)
    slow_turtle.right(90)
radius=10
for i in range(5):
    slow_turtle.circle(radius)
    radius +=10
for y in range(3):
    for x in range(5):
        slow_turtle.goto(x * 20,y *20)
        slow_turtle.dot()
    slow_turtle.goto(0,y * 20)
for i in range (4):
    slow_turtle.forward(size)
    slow_turtle.right(90)
slow_turtle.penup()
slow_turtle.forward(20)
slow_turtle.penup()
for i in range(5):
    slow_turtle.goto(-10 * i, -10)
    slow_turtle.pendown()
    for r in range(4):
        slow_turtle.forward(20 * (1+1))
        slow_turtle.right(90)
screen.mainloop()