import turtle



def draw_petal(t, radius, angle):
    """Draw a single petal"""
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, petals, radius, angle):
    """Draw a flower with the specified number of petals."""
    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)

def main():
    # adding color and how petal information
    screen = turtle.Screen()
    screen.bgcolor((173/255, 230/255, 230/255))  # Light blue background color in RGB!

    petal_turtle = turtle.Turtle()
    petal_turtle.color((1, 1, 1))  # white color in RGB !
    petal_turtle.speed(0)  # Setting the speed to the fastest to be able to see the flower faster

    # Draw a flower
    draw_flower(petal_turtle, petals=12, radius=100, angle=45)

    # Hiding the little turtle 
    petal_turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
