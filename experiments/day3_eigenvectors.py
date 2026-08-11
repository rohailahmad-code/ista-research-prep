import numpy as np
import matplotlib.pyplot as plt

# Non-orthogonal-looking but symmetric 2x2 matrix
A = np.array([[2, 1],
              [1, 2]])

# Eigenvalues / eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Matrix A:\n", A)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors (as columns):\n", eigenvectors)

# The i-th eigenvector is the i-th COLUMN: eigenvectors[:, i]
v1 = eigenvectors[:, 0]
v2 = eigenvectors[:, 1]
print(f"\nCheck: A @ v1 = {A @ v1}, lambda1 * v1 = {eigenvalues[0] * v1}")
print(f"Check: A @ v2 = {A @ v2}, lambda2 * v2 = {eigenvalues[1] * v2}")

# A random - non-eigen - vector
np.random.seed(0)
v_random = np.random.randn(2)
v_random = v_random / np.linalg.norm(v_random)
Av_random = A @ v_random

# One actual eigenvector
eigvec = eigenvectors[:, 0] / np.linalg.norm(eigenvectors[:, 0])
Aeigvec = A @ eigvec

# Plotting 
fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))


def plot_arrows(ax, v_in, v_out, title):
    lim = max(np.abs([*v_in, *v_out])) * 1.4
    ax.axhline(0, color="lightgray", linewidth=0.8, zorder=0)
    ax.axvline(0, color="lightgray", linewidth=0.8, zorder=0)
    ax.arrow(0, 0, *v_in, head_width=0.08, length_includes_head=True,
              color="tab:blue", linewidth=2, label="v (input)")
    ax.arrow(0, 0, *v_out, head_width=0.08, length_includes_head=True,
              color="tab:red", linewidth=2, label="A @ v (output)")
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)


plot_arrows(axes[0], v_random, Av_random,
            "Random vector: A@v rotates AND stretches")
plot_arrows(axes[1], eigvec, Aeigvec,
            "Eigenvector: A@v only stretches (same direction)")

plt.tight_layout()
plt.savefig("experiments-results/day3_eigenvectors.png", dpi=150)
print("\nSaved plot to day3_eigenvectors.png")