"""
Session 7 - Task 1: Instagram Hours vs. Daily Posts Scatter Plot
File: session-7/task1_instagram.py

Description:
Creates two Python lists representing:
1. Daily hours spent on Instagram across 7 days (one week).
2. Number of posts made each day.
Plots these on a scatter plot using matplotlib and visually analyzes
the correlation (positive, negative, or zero).
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless plot generation
import matplotlib.pyplot as plt

def run_task1():
    # -------------------------------------------------------------
    # 1. Dataset: 7 Days of Instagram Usage & Posts Made
    # -------------------------------------------------------------
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # List 1: Number of hours spent on Instagram each day
    instagram_hours = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 4.5]
    
    # List 2: Number of posts made each day
    posts_made = [0, 1, 1, 2, 2, 4, 3]

    # Calculate Pearson correlation coefficient using numpy
    corr_matrix = np.corrcoef(instagram_hours, posts_made)
    r = corr_matrix[0, 1]

    print("=" * 65)
    print(" TASK 1: INSTAGRAM HOURS VS. POSTS MADE (7 DAYS)")
    print("=" * 65)
    print(f"{'Day':<12} | {'Hours on Instagram (hrs)':<25} | {'Posts Made':<12}")
    print("-" * 65)
    for d, h, p in zip(days, instagram_hours, posts_made):
        print(f"{d:<12} | {h:<25.1f} | {p:<12}")
    print("-" * 65)
    print(f"Calculated Correlation Coefficient (r): {r:.4f}")
    print("=" * 65)

    # -------------------------------------------------------------
    # 2. Scatter Plot using Matplotlib
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 6), dpi=150)
    
    # Plot scatter points
    plt.scatter(
        instagram_hours, 
        posts_made, 
        color="#833AB4",          # Instagram theme purple
        s=120, 
        edgecolors="#262626", 
        linewidths=1.5, 
        zorder=3,
        label="Daily Observations"
    )

    # Fit a linear trend line (y = mx + c) to visually highlight direction
    slope, intercept = np.polyfit(instagram_hours, posts_made, 1)
    trendline_x = np.linspace(min(instagram_hours) - 0.2, max(instagram_hours) + 0.2, 50)
    trendline_y = slope * trendline_x + intercept
    plt.plot(trendline_x, trendline_y, color="#E1306C", linestyle="--", linewidth=2, 
             label=f"Trendline (Slope = +{slope:.2f})")

    # Annotate each point with day and coordinates
    for i, (x_val, y_val, d) in enumerate(zip(instagram_hours, posts_made, days)):
        plt.annotate(
            f"{d} ({x_val}h, {y_val}p)",
            xy=(x_val, y_val),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=8.5,
            fontweight="medium",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="lightgray", alpha=0.85)
        )

    # Chart details
    plt.title("Instagram Daily Usage vs. Posts Made (1 Week)\nVisual Correlation Analysis", 
              fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Time Spent on Instagram (Hours/Day)", fontsize=11, fontweight="semibold")
    plt.ylabel("Number of Posts Made (Posts/Day)", fontsize=11, fontweight="semibold")
    
    plt.xlim(0.5, 5.0)
    plt.ylim(-0.5, 5.0)
    plt.yticks(range(0, 6))
    plt.grid(True, linestyle=":", alpha=0.6, zorder=0)
    plt.legend(loc="upper left", frameon=True)

    # Text box with visual correlation description
    description_text = (
        f"Visual Relationship: POSITIVE CORRELATION\n"
        f"r = +{r:.2f} (Strong Positive)\n"
        f"- Upward drift from bottom-left to top-right.\n"
        f"- As Instagram hours increase, the number of\n"
        f"  posts created also tends to increase."
    )
    plt.gca().text(
        0.97, 0.05, 
        description_text, 
        transform=plt.gca().transAxes,
        fontsize=9,
        verticalalignment='bottom',
        horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.6", facecolor="#FDF2E9", edgecolor="#E67E22", alpha=0.95)
    )

    plt.tight_layout()

    # Save chart to session-7 folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "instagram_scatter_plot.png")
    plt.savefig(output_path)
    plt.close()

    print(f"\n[+] Scatter plot saved successfully to: {output_path}")

    # -------------------------------------------------------------
    # 3. Visual Relationship Description
    # -------------------------------------------------------------
    print("\nVISUAL CORRELATION DESCRIPTION:")
    print("=" * 65)
    print("1. Orientation of Points: The data points form an upward-sloping")
    print("   pattern that extends from the lower-left quadrant toward the")
    print("   upper-right quadrant.")
    print("2. Variable Co-movement: As the daily time spent on Instagram increases")
    print("   from 1.0 hour to 4.5 hours, the daily number of posts uploaded")
    print("   also climbs from 0 to 4 posts.")
    print(f"3. Classification: This visual pattern clearly signifies a POSITIVE")
    print(f"   CORRELATION (Pearson's r = +{r:.4f}). When a user devotes more time")
    print("   to the platform, they tend to be more active content creators.")
    print("=" * 65)

if __name__ == "__main__":
    run_task1()
