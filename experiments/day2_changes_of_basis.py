import numpy as np
import matplotlib.pyplot as plt


# Original vector
v = np.array([3, 4])


# Rotation angle: 30 degrees
angle = np.radians(30)


# 2D rotation matrix
R = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])


# rotate the vector
v_rotated = R @ v


# Print results
print("Original vector:", v)
print("Rotated vector:", v_rotated)


# Check lengths
original_length = np.linalg.norm(v)
rotated_length = np.linalg.norm(v_rotated)

print("Original length:", original_length)
print("Rotated length:", rotated_length)


# Create figure
fig, ax = plt.subplots(figsize=(8, 8))


# Original vector
ax.quiver(
    0, 0,
    v[0], v[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    label="Original vector"
)


# rotated vector
ax.quiver(
    0, 0,
    v_rotated[0], v_rotated[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="orange",
    label="Rotated vector (30°)"
)


# Axis limits
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)


# equal scaling on both axes
ax.set_aspect("equal", adjustable="box")


# X and Y axes
ax.axhline(0, linewidth=0.8)
ax.axvline(0, linewidth=0.8)


# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("2D Vector Rotation by 30°")


# grid and legend
ax.grid(True)
ax.legend()


# plot figure
plt.savefig(
    "experiments-results/day2_change_of_basis.png",
    dpi=150,
    bbox_inches="tight"
)


# show plot
plt.show()