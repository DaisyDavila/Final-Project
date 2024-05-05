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
