# Day 3 — Eigenvalues and Eigenvectors

An **eigenvector** is a non-zero vector whose direction stays the same when a matrix is applied to it. The vector can become longer, shorter, or point in the opposite direction, but it remains on the same line (the same span). This relationship is written as:

$$
A\mathbf{v} = \lambda\mathbf{v}
$$

The **eigenvalue** $\lambda$ tells us how the eigenvector changes when the matrix is applied:

- $\lambda > 1$ → stretches the vector
- $0 < \lambda < 1$ → compresses the vector
- $\lambda < 0$ → flips the vector's direction
- $\lambda = 1$ → the vector stays unchanged

## Finding Eigenvalues

To find the eigenvalues, we solve the **characteristic equation**:

$$
\det(A - \lambda I) = 0
$$

## Finding Eigenvectors

Once the eigenvalues are found, we find the corresponding eigenvectors by solving:

$$
(A - \lambda I)\mathbf{v} = 0
$$

## Verification

We can verify the result by checking whether:

$$
A\mathbf{v} = \lambda\mathbf{v}
$$


Eigenvectors represent the **special directions** of a matrix transformation, while eigenvalues describe **how those directions are scaled or changed**.