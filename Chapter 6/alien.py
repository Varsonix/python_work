alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'fast'
}

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on it's current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position + the new position
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")