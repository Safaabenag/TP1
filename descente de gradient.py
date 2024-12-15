import matplotlib.pyplot as plt
import numpy as np

# Définir la fonction à minimiser
def fonction(x, y):
    return x**2 + y**2

# Définir le gradient (dérivées partielles) de la fonction
def gradient_fonction(x, y):
    g_x = 2 * x
    g_y = 2 * y
    return g_x, g_y

# Création de la grille pour X et Y
X = np.arange(-3, 3, 0.1)
Y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(X, Y)

# Calcul des valeurs de Z pour les courbes de niveau
Z = fonction(X, Y)

# Initialiser le graphique
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour, ax=ax, label="Valeur de f(x, y)")

# Initialisation du point de départ aléatoire pour la descente de gradient
x = 3
y = 3

# Taux d'apprentissage
lr = 0.2

# Configuration de la boucle de descente de gradient
max_iterations = 50
tolerance = 2e-6  # Tolérance pour convergence

# Tracer le point de départ
ax.scatter(x, y, color='red', label='Départ (x=3, y=3)')

# Boucle de descente de gradient
i = 0
while i < max_iterations:
    g_x, g_y = gradient_fonction(x, y)

    # Mise à jour des paramètres avec la descente de gradient
    x = x - lr * g_x
    y = y - lr * g_y

    # Tracer le point courant dans le chemin de descente
    ax.scatter(x, y, color='blue', s=10)

    # Afficher les informations de l'itération actuelle
    print(f"Itération {i+1:3d}  -> x={x:+7.5f} y={y:+7.5f}")

    # Pause pour visualiser le mouvement pas à pas
    plt.pause(0.05)

    # Vérification de la convergence (si le gradient est proche de zéro)
    if np.abs(g_x) < tolerance and np.abs(g_y) < tolerance:
        print(f"Convergence après {i+1} itérations.")
        break

    # Incrémenter le compteur d'itérations
    i += 1

# Ajouter des labels et une légende
ax.set_xlabel("Paramètre 1 (x)")
ax.set_ylabel("Paramètre 2 (y)")
ax.legend()

# Afficher le tracé final
plt.title("Descente de gradient en 2D")
plt.show()