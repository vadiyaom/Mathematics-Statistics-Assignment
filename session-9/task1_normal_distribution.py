"""
Session 9 - Task 1: Normal Distribution Generation & Bell Curve Plot
File: session-9/task1_normal_distribution.py

Description:
Generates 100 random numbers following a normal distribution with:
- Population Mean (mu) = 50
- Population Standard Deviation (sigma) = 10
using numpy.random.normal(). Plots the frequency histogram overlaid with
the continuous theoretical Gaussian bell curve using matplotlib.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_task1(seed=42):
    if seed is not None:
        np.random.seed(seed)

    # -------------------------------------------------------------
    # 1. Generate 100 Normally Distributed Random Numbers
    # -------------------------------------------------------------
    mu = 50.0      # Specified mean
    sigma = 10.0   # Specified standard deviation
    n = 100        # Sample size

    # Generate samples using numpy.random.normal
    samples = np.random.normal(loc=mu, scale=sigma, size=n)

    # Calculate empirical sample statistics
    sample_mean = float(np.mean(samples))
    sample_std = float(np.std(samples, ddof=1))
    sample_median = float(np.median(samples))
    sample_min = float(np.min(samples))
    sample_max = float(np.max(samples))

    print("=" * 68)
    print(" TASK 1: NORMAL DISTRIBUTION GENERATION (N = 100, MU = 50, SIGMA = 10)")
    print("=" * 68)
    print(f"Target Distribution Parameters : Mean (mu) = {mu}, Std Dev (sigma) = {sigma}")
    print(f"Generated Sample Size (N)      : {n}")
    print("-" * 68)
    print(f"Sample Mean (x_bar)            : {sample_mean:.4f} (Expected: {mu:.1f})")
    print(f"Sample Standard Deviation (s)  : {sample_std:.4f} (Expected: {sigma:.1f})")
    print(f"Sample Median                  : {sample_median:.4f}")
    print(f"Sample Minimum                 : {sample_min:.4f}")
    print(f"Sample Maximum                 : {sample_max:.4f}")
    print("-" * 68)
    print("First 10 Generated Numbers (preview):")
    print(np.round(samples[:10], 2))
    print("=" * 68)

    # -------------------------------------------------------------
    # 2. Plot the Bell Curve using Matplotlib
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 6), dpi=150)

    # Plot histogram of samples with density=True (so area integrates to 1)
    count, bins, ignored = plt.hist(
        samples, 
        bins=15, 
        density=True, 
        color="#3498DB", 
        edgecolor="#1B4F72", 
        alpha=0.65, 
        label=f"Sample Histogram (N = {n})"
    )

    # Generate smooth theoretical normal PDF (Gaussian Bell Curve)
    x_axis = np.linspace(mu - 3.5 * sigma, mu + 3.5 * sigma, 300)
    # PDF Formula: (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma)^2)
    pdf = (1.0 / (sigma * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((x_axis - mu) / sigma) ** 2)
    plt.plot(x_axis, pdf, color="#C0392B", linewidth=2.5, label="Theoretical Bell Curve (PDF)")

    # Overlay vertical lines for Mean and +/- 1 Standard Deviation
    plt.axvline(mu, color="#27AE60", linestyle="--", linewidth=2, label=f"Mean (mu = {mu:.0f})")
    plt.axvline(mu - sigma, color="#8E44AD", linestyle=":", linewidth=1.8, label=f"-1 Std Dev ({mu - sigma:.0f})")
    plt.axvline(mu + sigma, color="#8E44AD", linestyle=":", linewidth=1.8, label=f"+1 Std Dev ({mu + sigma:.0f})")

    # Chart details
    plt.title(f"Normal Distribution Bell Curve (N = {n}, $\\mu$ = {mu:.0f}, $\\sigma$ = {sigma:.0f})", 
              fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Value (X)", fontsize=11, fontweight="bold")
    plt.ylabel("Probability Density", fontsize=11, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right", frameon=True, fontsize=9)

    # Information callout box
    info_text = (
        f"Distribution Details:\n"
        f"Expected Mean (mu): {mu:.1f}\n"
        f"Sample Mean (x_bar): {sample_mean:.2f}\n"
        f"Expected SD (sigma): {sigma:.1f}\n"
        f"Sample SD (s): {sample_std:.2f}\n"
        f"Symmetric around X = 50"
    )
    plt.gca().text(
        0.04, 0.94, info_text,
        transform=plt.gca().transAxes,
        fontsize=8.5,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FDFEFE', edgecolor='#BDC3C7', alpha=0.95)
    )

    plt.tight_layout()

    # Save chart in session-9 folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "normal_distribution_bell_curve.png")
    plt.savefig(output_path)
    plt.close()

    print(f"\n[+] Normal distribution bell curve plot saved to: {output_path}")

if __name__ == "__main__":
    run_task1()

