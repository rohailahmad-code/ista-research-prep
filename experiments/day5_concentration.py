import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

true_mean = 0.5
n_trials = 1000
n_values = [10, 100, 1000]
deviation_threshold = 0.1  # Check deviation greater than 0.1


# Simulate sample averages
sample_averages = {}

for n in n_values:
    # Flip a fair coin n times in each trial
    head_counts = np.random.binomial(n, 0.5, size=n_trials)

    # Convert number of heads into fraction of heads
    p_hat = head_counts / n
    sample_averages[n] = p_hat


# Plot the results
fig, axes = plt.subplots(1, len(n_values), figsize=(15, 4.5), sharey=False)

for ax, n in zip(axes, n_values):
    p_hat = sample_averages[n]

    # Histogram of sample averages
    ax.hist(p_hat, bins=30, color="tab:blue", alpha=0.7, edgecolor="white")

    # Show the true mean
    ax.axvline(
        true_mean,
        color="black",
        linestyle="--",
        linewidth=1,
        label="true mean"
    )

    # Show the deviation range
    ax.axvline(
        true_mean - deviation_threshold,
        color="tab:red",
        linestyle=":",
        linewidth=1
    )

    ax.axvline(
        true_mean + deviation_threshold,
        color="tab:red",
        linestyle=":",
        linewidth=1,
        label="±0.1 band"
    )

    ax.set_title(f"n = {n}")
    ax.set_xlabel("sample average (fraction heads)")
    ax.set_xlim(0, 1)
    ax.legend(fontsize=8)

axes[0].set_ylabel("count (out of 1000 trials)")

plt.suptitle(
    "Distribution of sample averages, 1000 trials each, for different n"
)

plt.tight_layout()
plt.savefig("experiments-results/day5_concentration.png", dpi=150)

print("Saved plot to day5_concentration.png")


# Calculate empirical probability
empirical_probs = {}

for n in n_values:
    p_hat = sample_averages[n]

    # Check if deviation is greater than 0.1
    exceed = np.abs(p_hat - true_mean) > deviation_threshold

    # Fraction of trials that exceeded the limit
    empirical_probs[n] = exceed.mean()


# Calculate Hoeffding's upper bound
# P(|X_bar - E[X]| > t) <= 2 * exp(-2 * n * t^2)

t = deviation_threshold
hoeffding_bounds = {}

for n in n_values:
    bound = 2 * np.exp(-2 * n * t**2)
    hoeffding_bounds[n] = bound


# Print the results
print(
    f"\n{'n':>6} | "
    f"{'empirical P(|p_hat-0.5|>0.1)':>30} | "
    f"{'Hoeffding bound':>18} | "
    f"{'bound holds?':>12}"
)

print("-" * 76)

for n in n_values:
    emp = empirical_probs[n]
    bound = hoeffding_bounds[n]

    # Check if the empirical result is below the bound
    holds = emp <= bound

    print(
        f"{n:>6} | "
        f"{emp:>30.4f} | "
        f"{bound:>18.6f} | "
        f"{str(holds):>12}"
    )