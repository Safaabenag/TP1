import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
print(plt.style.available)
plt.style.use("dark_background")
# Définir la fonction J(x, y)
def J(x, y):
    return (x - 1)**2 + 10 * (x**2 - y)**2

# Créer une grille de valeurs pour x et y
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Calculer les valeurs Z basées sur la fonction J(x, y)
Z = J(X, Y)

# Créer le graphique 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface 3D
ax.plot_surface(X, Y, Z, cmap='viridis')

# Ajouter des labels et un titre
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('J(x, y)')
ax.set_title('Surface 3D de J(x, y)')

# Afficher le graphique
plt.show()
