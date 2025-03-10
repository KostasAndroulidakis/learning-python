"""Simulates a ball's movement and collision with the edges of a screen."""

def move(position, speed, right_wall):
    """Returns the ball's new position after one millisecond of movement."""
    new_position = position + speed
    if new_position >= right_wall:
        new_position = right_wall
    elif new_position <= 0:
        new_position = 0
    return new_position

def maybe_bounce(position, speed, right_wall):
    """Returns the ball's new speed, which stays the same unless the ball
    bounces off of a wall.
    """
    if position >= right_wall:
        # Reverses direction and loses a bit of speed.
        speed = speed * -0.75
    elif position == 0:
        speed = speed * -0.75

    return speed
