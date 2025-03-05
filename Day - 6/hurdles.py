import turtle

# ------------------------
# The Hurdle Challenge (Simulating Karel's Movement)
# ------------------------

# Function to make the turtle turn right
def turn_right():
    """Makes the turtle turn right by 90 degrees."""
    turtle.right(90)

# Function to simulate jumping
def jump():
    """Simulates the turtle jumping over an obstacle."""
    turtle.forward(20)  # Move forward
    turtle.left(90)
    turtle.forward(20)  # Jump up
    turn_right()
    turtle.forward(20)  # Move forward
    turn_right()
    turtle.forward(20)  # Jump down
    turtle.left(90)

# Setup the turtle
turtle.speed(5)

# Simulate the hurdle challenge
for _ in range(6):  # Repeat jumping 6 times
    jump()

# End the turtle graphics properly
turtle.done()
