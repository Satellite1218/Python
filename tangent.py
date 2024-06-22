import matplotlib.pyplot as plt
import numpy as np

# Define the theta range from 0 to 2*pi radians
theta_radians = np.linspace(0, 2*np.pi, 400)

# Calculate the tangent values
tan_values = np.tan(theta_radians)

# Convert radians to degrees for x-axis labeling (optional)
theta_degrees = np.rad2deg(theta_radians)

# Set up the plot
plt.figure(figsize=(10, 6))
plt.plot(theta_degrees, tan_values, label='$y = \\tan(x)$', color='blue')

# Highlight the vertical asymptotes at multiples of pi/2
for k in range(-1, 4):
    plt.axvline(x=k * 90, color='gray', linestyle='--')

# Labels and title
plt.title('tan')
plt.xlabel('angle (degrees)')
plt.ylabel('$\\tan(x)$')
plt.ylim(-10, 10)
plt.xlim(0, 360)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
