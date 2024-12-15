import numpy as np
import matplotlib.pyplot as plt


# 1. Fonction J(x, y) et son gradient
def J(x, y):
    return (x - 1) ** 2 + 10 * (x ** 2 - y) ** 2


def gradient_J(x, y):
    dJ_dx = 2 * (x - 1) + 40 * x * (x ** 2 - y)  # Dérivée partielle par rapport à x
    dJ_dy = -20 * (x ** 2 - y)  # Dérivée partielle par rapport à y
    return np.array([dJ_dx, dJ_dy])


# 2. Algorithme de descente de gradient
def gradient_descent(grad, x0, y0, alpha, max_iter=1000, tol=1e-6):
    x, y = x0, y0  # Initialisation du point de départ
    trajectory = [(x, y)]  # Pour suivre l'évolution des points

    for k in range(max_iter):
        grad_eval = grad(x, y)  # Calcul du gradient au point actuel
        x_new = x - alpha * grad_eval[0]
        y_new = y - alpha * grad_eval[1]

        # Critère d'arrêt : si la variation est très faible
        if np.linalg.norm([x_new - x, y_new - y]) < tol:
            print(f"Convergence atteinte en {k} itérations.")
            break

        x, y = x_new, y_new
        trajectory.append((x, y))

    return x, y, trajectory


# 3. Paramètres initiaux
x0, y0 = -1, 1  # Point de départ
alpha = 0.001  # Pas fixe (à ajuster pour observer la convergence)

# 4. Lancer la méthode du gradient
x_min, y_min, trajectory = gradient_descent(gradient_J, x0, y0, alpha)

print(f"Minimum atteint en ({x_min:.6f}, {y_min:.6f})")

# 5. Visualisation de la convergence
trajectory = np.array(trajectory)
x_vals, y_vals = trajectory[:, 0], trajectory[:, 1]

# Créer les lignes de niveau de la fonction
X, Y = np.linspace(-2, 2, 400), np.linspace(-1, 3, 400)
X, Y = np.meshgrid(X, Y)
Z = J(X, Y)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=50, cmap="viridis")
plt.colorbar(label='Valeur de J(x, y)')
plt.plot(x_vals, y_vals, 'r.-', label="Trajectoire du gradient")
plt.scatter(x0, y0, color='white', zorder=5, label="Point initial")
plt.scatter(x_min, y_min, color='red', zorder=5, label="Point final")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Descente de gradient à pas constant')
plt.legend()
plt.show()
