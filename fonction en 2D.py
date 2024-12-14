import numpy as np
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use("dark_background")

# Define the function J(x, y)
def J(x, y):
    return (x - 1)**2 + 10 * (x**2 - y)**2

# Create a meshgrid for x and y values
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Compute the Z values based on the function J(x, y)
Z = J(X, Y)

# Create a 2D contour plot (filled contour) for the function J(x, y)
plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, Z, 50, cmap='viridis')  # 50 levels of contour

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Filled Contour Plot of J(x, y)')

# Add a color bar to show the scale of function values
plt.colorbar(cp)

# Show the plot
plt.show()
