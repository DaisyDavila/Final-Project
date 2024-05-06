import turtle

def draw_petal(t, radius, angle):
    """Draw a single petal"""
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, petals, radius, angle):
    """Drawing the flower petals"""
    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)

def draw_stem(t, length):
    """Draw a stem below the flower"""
    t.left(90)  # Turn left to draw stem
    t.forward(length)  # Draw stem

def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor((173/255, 230/255, 230/255))  # Light blue background color in RGB!

    petal_turtle = turtle.Turtle()
    petal_turtle.color((1, 1, 1))  # Outline of the colors are White!
    petal_turtle.speed(0)  # Setting the speed to the fastest to be able to see the flower faster

    # Draw a flower
    draw_flower(petal_turtle, petals=11, radius=100, angle=45)

    # Make the stem touch the center of the petals
    stem_length = 300  # Adjust this value as needed

    # Turtle for drawing stem
    stem_turtle = turtle.Turtle()

    # Draw a stem below the flower
    stem_turtle.penup()
    stem_turtle.goto(0, -stem_length)  # Move turtle below the flower
    stem_turtle.pendown()
    stem_turtle.color((50/255, 205/255, 50/255))
    draw_stem(stem_turtle, length=stem_length)

    # Hiding the little turtle 
    petal_turtle.hideturtle()
    stem_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
