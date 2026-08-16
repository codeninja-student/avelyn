import turtle 
screen=turtle.Screen()       
slow_turtle=turtle.Turtle()
color = input("Enter the color for the Turtle: ")
slow_turtle.color(color)
distance = int(input("Enter how far to move: "))
slow_turtle.forward(distance)
size = int(input("Enter the size of the shape: "))
for _ in range (4):
    slow_turtle.forward(size)
    slow_turtle.right(90)
size = int(input("Enter the size"))
for _ in range(3):
    slow_turtle.forward(size)
    slow_turtle.right(120)
screen.mainloop()