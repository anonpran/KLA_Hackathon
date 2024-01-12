import numpy as np
import matplotlib.pyplot as plt

def split_and_rotate_x_axis(diameter, num_points, theta_degrees):
    # Calculate the radius based on the given diameter
    radius = diameter / 2

    # Generate equidistant points on the x-axis
    x_points = np.linspace(-radius, radius, num_points)

    # Rotate points by the given angle (theta) in degrees
    theta_radians = np.radians(theta_degrees)
    x_rotated = x_points * np.cos(theta_radians) - np.zeros_like(x_points) * np.sin(theta_radians)
    y_rotated = x_points * np.sin(theta_radians) + np.zeros_like(x_points) * np.cos(theta_radians)

    return x_rotated, y_rotated

# Example usage
diameter = 300  # Example diameter
num_points = 30  # Example number of points
theta_degrees = 45  # Example rotation angle in degrees

x_rotated, y_rotated = split_and_rotate_x_axis(diameter, num_points, theta_degrees)

# Plot the original and rotated points
plt.plot(x_rotated, y_rotated, marker='o', label='Rotated Points')
plt.axhline(0, color='black', linestyle='--', label='X-axis')
plt.axvline(0, color='black', linestyle='--', label='Y-axis')
plt.title(f'Rotated Points by {theta_degrees} degrees')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
