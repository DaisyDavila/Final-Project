import turtle

# Global variable to count clicks
click_count = 0

def draw_petal(t, radius, angle):
    """Draw a single petal."""
    t.begin_fill()
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.end_fill()

def draw_flower(t, petals, radius, angle):
    """Draw a flower with a specified number of petals."""
    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)

def draw_stem(t, length):
    """Draw a stem below the flower."""
    t.left(90)  # Turn to the left to draw stem
    t.forward(length)  # Draw stem

def click(x, y):
    """Turtle for clicking"""
    global click_count
    if click_count < 3:
        fill_turtle.penup()
        fill_turtle.goto(x, y)
        fill_turtle.pendown()
        fill_turtle.dot(30, (255/255, 234/255, 13/255))  # Yellow Bud color
        click_count += 1
    else:
        # Create a turtle to display the message
        message_turtle = turtle.Turtle()
        message_turtle.hideturtle()
        message_turtle.color((255/255, 105/255, 180/255))  # Pink font color
        message_turtle.penup()
        message_turtle.goto(0, -200)  
        message_turtle.write("You've reached the maximum limit of clicks!", align="center", font=("Arial", 14, "normal"))

def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor((173/255, 230/255, 230/255))  # Light blue background color in RGB!

    # Draw the flower in the center
    petal_turtle_center = turtle.Turtle()
    petal_turtle_center.color("white")  # White Daisy Petals
    petal_turtle_center.speed(0)  # Setting the speed to the fastest to be able to see the flower faster
    petal_turtle_center.begin_fill()  # Begin filling petals
    draw_flower(petal_turtle_center, petals=11, radius=100, angle=36)  # Draw the center flower
    petal_turtle_center.end_fill()  # End filling petals

    # Draw the flower on the left
    petal_turtle_left = turtle.Turtle()
    petal_turtle_left.color("white")  # White Daisy Petals
    petal_turtle_left.speed(0)
    petal_turtle_left.penup()
    petal_turtle_left.goto(-200, 0)  
    petal_turtle_left.pendown()
    petal_turtle_left.begin_fill()
    draw_flower(petal_turtle_left, petals=11, radius=100, angle=36)
    petal_turtle_left.end_fill()

    # Draw the flower on the right
    petal_turtle_right = turtle.Turtle()
    petal_turtle_right.color("white")  # White Daisy Petals
    petal_turtle_right.speed(0)
    petal_turtle_right.penup()
    petal_turtle_right.goto(200, 0)  
    petal_turtle_right.pendown()
    petal_turtle_right.begin_fill()
    draw_flower(petal_turtle_right, petals=11, radius=100, angle=36)
    petal_turtle_right.end_fill()

    # Calculate the stem length to touch the center of the petals
    stem_length = 120  
    # Draw the stem for the central flower
    stem_turtle_center = turtle.Turtle()
    stem_turtle_center.penup()
    stem_turtle_center.goto(0, -stem_length)  
    stem_turtle_center.pendown()
    stem_turtle_center.color((50/255, 205/255, 50/255))
    draw_stem(stem_turtle_center, length=stem_length)

    # Draw the stem for the flower on the left
    stem_turtle_left = turtle.Turtle()
    stem_turtle_left.penup()
    stem_turtle_left.goto(-200, -stem_length)  
    stem_turtle_left.pendown()
    stem_turtle_left.color((50/255, 205/255, 50/255))
    draw_stem(stem_turtle_left, length=stem_length)

    # Draw the stem for the flower on the right
    stem_turtle_right = turtle.Turtle()
    stem_turtle_right.penup()
    stem_turtle_right.goto(200, -stem_length)  
    stem_turtle_right.pendown()
    stem_turtle_right.color((50/255, 205/255, 50/255))
    draw_stem(stem_turtle_right, length=stem_length)

    # A turtle for placing the yellow bud on flowers!
    global fill_turtle
    fill_turtle = turtle.Turtle()
    fill_turtle.hideturtle()
    fill_turtle.speed(0)
    fill_turtle.penup()

    # Write "Complete the flower!" text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.color((255/255, 105/255, 180/255))
    text_turtle.penup()
    text_turtle.goto(0, 250)
    text_turtle.write("Complete the flower!", align="center", font=("Arial", 24, "normal"))

    # Write "Add a bud to the center of the Daisy!" text
    text_turtle.goto(0, 220)
    text_turtle.write("Add a bud to the center of the Daisy!", align="center", font=("Arial", 12, "normal"))

    # Bind click event to add the yellow bud
    screen.onclick(click)

    screen.mainloop()

if __name__ == "__main__":
    main()
