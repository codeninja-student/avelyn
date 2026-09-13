import turtle
screen=turtle.Screen()
slow_turtle=turtle.Turtle()
for i in range(4):
    slow_turtle.forward(5)
    slow_turtle.right(90)
for i in range (3):
    for s in range(4):
        slow_turtle.forward(50)
        slow_turtle.right(90)
    slow_turtle.penup()
    slow_turtle.forward(60)
    slow_turtle.pendown()
for i in range(4):
    for j in range(4):
        slow_turtle.forward(100)
        slow_turtle.right(90)
    slow_turtle.right(45)
for i in range(12):
    slow_turtle.right(30)
    for r in range(6):
        slow_turtle.circle(50)
        slow_turtle.right(60)                
screen.mainloop()