"""
Session 7 - Task 4: Spotify Listening Time vs. Test Marks (Strong Negative Correlation)
File: session-7/task4_spotify_marks.py

Description:
Simulates a dataset generated via ChatGPT containing 10 pairs of numbers
demonstrating a strong negative correlation between:
1. Daily time spent on Spotify (in hours)
2. Marks scored in a test (out of 100)
Calculates the correlation coefficient using numpy's corrcoef() and plots
the dataset as a scatter plot using matplotlib with a fitted trendline.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_task4():
    # -------------------------------------------------------------
    # 1. ChatGPT-Generated Dataset (10 Students)
    # Prompt: "Generate 10 pairs of numbers with a strong negative
    #          correlation between time spent on Spotify (hours) and
    #          marks scored in a test (out of 100)."
    # -------------------------------------------------------------
    students = [f"Student {i+1}" for i in range(10)]
    
    # Variable X: Daily Time Spent on Spotify (hours)
    spotify_hours = [0.5, 1.0, 1.5, 2.0, 2.8, 3.5, 4.0, 4.8, 5.2, 6.0]
    
    # Variable Y: Marks Scored in Test (out of 100)
    test_marks = [95, 91, 86, 82, 75, 68, 60, 52, 45, 34]

    x = np.array(spotify_hours)
    y = np.array(test_marks)

    # -------------------------------------------------------------
    # 2. Correlation Calculation using numpy
    # -------------------------------------------------------------
    corr_matrix = np.corrcoef(x, y)
    r = corr_matrix[0, 1]

    print("=" * 68)
    print(" TASK 4: SPOTIFY USAGE VS. TEST MARKS (CHATGPT DATASET)")
    print("=" * 68)
    print(f"{'Student':<12} | {'Spotify Time (Hours/Day)':<26} | {'Test Marks (Out of 100)':<22}")
    print("-" * 68)
    for s, h, m in zip(students, spotify_hours, test_marks):
        print(f"{s:<12} | {h:<26.1f} | {m:<22}")
    print("-" * 68)
    print(f"{'Mean':<12} | {np.mean(x):<26.2f} | {np.mean(y):<22.2f}")
    print(f"{'Std Dev':<12} | {np.std(x, ddof=1):<26.2f} | {np.std(y, ddof=1):<22.2f}")
    print("-" * 68)
    print(f"NumPy Correlation Matrix:\n{corr_matrix}")
    print(f"Pearson Correlation Coefficient (r): {r:.5f} (approx. {r:.4f})")
    print("=" * 68)

    print("\nINTERPRETATION:")
    print("=" * 68)
    print(f"- Value of r: {r:.4f}")
    print("- Classification: STRONG NEGATIVE CORRELATION (r close to -1.0)")
    print("- Meaning: As daily time spent listening to Spotify increases,")
    print("  the marks scored in the test steadily and noticeably decrease.")
    print("  The points form a downward sloping trajectory from top-left to bottom-right.")
    print("=" * 68)

    # -------------------------------------------------------------
    # 3. Scatter Plot with Matplotlib
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 6), dpi=150)

    # Scatter points
    plt.scatter(
        x, y, 
        color="#1DB954",        # Spotify brand green
        s=130, 
        edgecolor="#121212", 
        linewidth=1.5, 
        zorder=3, 
        label="Student Scores"
    )

    # Linear trendline (Line of best fit)
    slope, intercept = np.polyfit(x, y, 1)
    x_vals = np.linspace(min(x) - 0.3, max(x) + 0.3, 100)
    y_vals = slope * x_vals + intercept
    plt.plot(
        x_vals, y_vals, 
        color="#E74C3C", 
        linestyle="--", 
        linewidth=2, 
        label=f"Trendline: y = {slope:.2f}x + {intercept:.2f}\n(r = {r:.4f})"
    )

    # Annotate points with coordinates
    for x_i, y_i in zip(x, y):
        plt.annotate(
            f"({x_i}h, {y_i}m)",
            xy=(x_i, y_i),
            xytext=(0, 9),
            textcoords="offset points",
            ha="center",
            fontsize=8.5,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#ddd", alpha=0.9)
        )

    # Chart formatting
    plt.title("Time Spent on Spotify vs. Test Marks\nDemonstration of Strong Negative Correlation", 
              fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Daily Time Spent on Spotify (Hours/Day)", fontsize=11, fontweight="semibold")
    plt.ylabel("Test Marks (Out of 100)", fontsize=11, fontweight="semibold")
    plt.xlim(0.0, 6.5)
    plt.ylim(20, 105)
    plt.grid(True, linestyle=":", alpha=0.6, zorder=0)
    plt.legend(loc="upper right", frameon=True)

    # Explanation Callout
    desc_box = (
        f"Strong Negative Correlation\n"
        f"r = {r:.4f}\n"
        f"- Downward slope (top-left to bottom-right)\n"
        f"- Higher Spotify hours correspond to lower test marks"
    )
    plt.gca().text(
        0.05, 0.08, 
        desc_box, 
        transform=plt.gca().transAxes,
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#FDEDEC", edgecolor="#E74C3C", alpha=0.95)
    )

    plt.tight_layout()

    # Save figure
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "spotify_vs_marks_scatter.png")
    plt.savefig(output_path)
    plt.close()

    print(f"\n[+] Scatter plot saved successfully to: {output_path}")

if __name__ == "__main__":
    run_task4()

