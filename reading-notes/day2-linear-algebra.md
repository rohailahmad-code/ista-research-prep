# Day 2 — Linear Algebra

A basis is a set of vectors that we use as reference directions to describe other vectors. For example, in normal 2D coordinates, we use the x-axis and y-axis as our basis, so a vector like (3, 4) means 3 units in the x direction and 4 units in the y direction.

We can also change the basis by using different directions, such as rotated axes. The actual vector does not change, but its coordinates can become different because we are describing it using a different reference system. This means that the same thing can have multiple valid representations depending on the basis we choose.

This idea is important in machine learning because a latent representation is also a way of describing data using different directions or features. A representation might look disentangled in one basis, but after changing the basis, the information can become mixed or entangled while still representing the same data. This connects to the idea from yesterday's paper that there may not be a unique "correct" representation without additional assumptions.

A change of basis therefore does not necessarily change the underlying information; it changes how that information is represented. Matrix multiplication can be used to perform these transformations, which is why understanding vectors, matrices, and bases is important for understanding neural networks and representation learning.