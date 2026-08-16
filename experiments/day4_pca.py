"""
Day 4: Covariance and PCA visualization.

Goal: show that PCA is just "find the eigenvectors of the covariance
matrix" — those eigenvectors point along the natural axes of spread
in the data, and the eigenvalues tell you how much variance lies
along each axis.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# 1. Generate a correlated synthetic dataset (elongated, tilted cloud)
mean_true = [0, 0]
cov_true = [[3, 2],
            [2, 2]]
n_samples = 300

data = np.random.multivariate_normal(mean=mean_true, cov=cov_true, size=n_samples)

print("Data shape:", data.shape)

# 2. Compute the covariance matrix of the data ourselves.
# IMPORTANT: np.cov expects variables as ROWS, observations as COLUMNS.
# Our `data` is (300 samples, 2 features), so we must transpose it:
# np.cov(data.T) -> 2x2. np.cov(data) would instead treat each of the
# 300 samples as a "variable" and give a 300x300 matrix -- wrong shape.
cov_computed = np.cov(data.T)

print("\nTrue covariance (used to generate data):\n", np.array(cov_true))
print("\nComputed covariance (from np.cov(data.T)):\n", cov_computed)
print("\nDifference (sampling noise):\n", cov_computed - np.array(cov_true))

# 3. Eigendecomposition of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_computed)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors (as columns):\n", eigenvectors)


# 4. Plot: scatter of data + eigenvectors as arrows from the data's mean,
# scaled by their eigenvalues so the "biggest spread" direction is the
# longest arrow.
data_mean = data.mean(axis=0)

plt.figure(figsize=(7, 7))
plt.scatter(data[:, 0], data[:, 1], alpha=0.4, s=20, color="tab:blue", label="data")

colors = ["tab:red", "tab:green"]
labels = ["PC1 (largest eigenvalue)", "PC2 (smaller eigenvalue)"]

# Scale factor just for visibility -- eigenvalues are in variance units,
# so sqrt(eigenvalue) is closer to a "standard deviation" length scale.
# We additionally multiply by a constant so the arrows are clearly visible
# against the scatter (a purely cosmetic choice, doesn't change direction).
scale = 2.0

for i in range(2):
    vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i]) * scale
    plt.arrow(
        data_mean[0], data_mean[1], vec[0], vec[1],
        head_width=0.15, length_includes_head=True,
        color=colors[i], linewidth=2.5, zorder=5,
        label=labels[i],
    )

plt.axhline(0, color="lightgray", linewidth=0.8, zorder=0)
plt.axvline(0, color="lightgray", linewidth=0.8, zorder=0)
plt.gca().set_aspect("equal")
plt.title("PCA: eigenvectors of the covariance matrix")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("experiments-results/day4_pca.png", dpi=150)
print("\nSaved plot to day4_pca.png")