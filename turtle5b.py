import turtle
screen=turtle.Screen()
slow_turtle=turtle.Turtle()
print("Which shape would you like to draw?")
shape_choice= input("Square, Triangle,or Circle: ").lower()
print("you want to draw a ",shape_choice)
if shape_choice=="square":
    for _ in range (4):
        slow_turtle.forward(100)
        slow_turtle.right(90)
elif shape_choice== "triangle":
    for _ in range(3):
        slow_turtle.forward(100)
        slow_turtle.right(120)
elif shape_choice == "circle":
    slow_turtle.circle(50)
else:
    print("Sorry,i don't knownhow to draw thhat shape.")
screen.mainloop()
