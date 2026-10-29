"""
Session 7 - Task 2: Zomato vs. Swiggy Monthly Orders Correlation
File: session-7/task2_zomato_swiggy.py

Description:
Given data for 6 friends: their monthly Zomato order count and monthly
Swiggy order count, calculate the Pearson correlation coefficient using
numpy's corrcoef(). Prints the complete correlation matrix, the exact
coefficient, and provides an in-depth explanation of whether the correlation
is positive, negative, or zero.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_task2():
    # -------------------------------------------------------------
    # 1. Dataset: Monthly Orders for 6 Friends
    # -------------------------------------------------------------
    friends = ["Friend 1 (Aarav)", "Friend 2 (Bhavna)", "Friend 3 (Chirag)", 
               "Friend 4 (Divya)", "Friend 5 (Eshan)", "Friend 6 (Farhan)"]
    
    # Monthly order counts on Zomato and Swiggy
    zomato_orders = [12, 18,  5, 22,  8, 15]
    swiggy_orders = [14, 20,  4, 25,  7, 17]

    # Convert to numpy arrays
    x = np.array(zomato_orders)
    y = np.array(swiggy_orders)

    # -------------------------------------------------------------
    # 2. Calculate Correlation Coefficient using numpy.corrcoef()
    # -------------------------------------------------------------
    # np.corrcoef returns the 2x2 correlation matrix:
    # [[r_xx, r_xy],
    #  [r_yx, r_yy]]
    corr_matrix = np.corrcoef(x, y)
    r = corr_matrix[0, 1]

    # -------------------------------------------------------------
    # 3. Print Results
    # -------------------------------------------------------------
    print("=" * 70)
    print(" TASK 2: CORRELATION BETWEEN ZOMATO & SWIGGY MONTHLY ORDERS")
    print("=" * 70)
    print(f"{'Friend':<20} | {'Zomato Orders':<16} | {'Swiggy Orders':<16}")
    print("-" * 70)
    for name, z, s in zip(friends, zomato_orders, swiggy_orders):
        print(f"{name:<20} | {z:<16} | {s:<16}")
    print("-" * 70)
    print(f"{'Mean':<20} | {np.mean(x):<16.2f} | {np.mean(y):<16.2f}")
    print(f"{'Std Dev (Sample)':<20} | {np.std(x, ddof=1):<16.2f} | {np.std(y, ddof=1):<16.2f}")
    print("=" * 70)
    
    print("\nNUMPY CORRCOEF MATRIX:")
    print("-------------------------------------------------------------")
    print(corr_matrix)
    print("-------------------------------------------------------------")
    print(f"Extracted Correlation Coefficient (r) = {r:.5f} (approx. {r:.4f})")
    print("=" * 70)

    # -------------------------------------------------------------
    # 4. Statistical & Domain Explanation
    # -------------------------------------------------------------
    print("\nEXPLANATION OF CORRELATION (POSITIVE, NEGATIVE, OR ZERO):")
    print("=" * 70)
    if r > 0.05:
        corr_type = "POSITIVE CORRELATION"
        strength = "Very Strong Positive" if r >= 0.8 else "Moderate Positive" if r >= 0.5 else "Weak Positive"
    elif r < -0.05:
        corr_type = "NEGATIVE CORRELATION"
        strength = "Very Strong Negative" if r <= -0.8 else "Moderate Negative" if r <= -0.5 else "Weak Negative"
    else:
        corr_type = "ZERO (OR NEGLIGIBLE) CORRELATION"
        strength = "No linear association"

    print(f"Classification : {corr_type} ({strength})")
    print(f"Numeric Value  : r = +{r:.4f}")
    print("-" * 70)
    print("Statistical Interpretation:")
    print(f"1. Since r > 0 (+{r:.4f}), the correlation is strongly POSITIVE.")
    print("2. Both variables move in the same direction: friends who order food")
    print("   frequently on Zomato also order frequently on Swiggy.")
    print("3. Conversely, friends who rarely order on Zomato (e.g. Chirag with 5 orders)")
    print("   also maintain a very low order count on Swiggy (4 orders).")
    print("\nReal-World Behavioral Meaning:")
    print("- Propensity to Order: This demonstrates an overall consumer propensity")
    print("  for online food delivery. 'Foodies' or busy working professionals")
    print("  (like Divya, with 22 Zomato and 25 Swiggy orders) order food online")
    print("  almost every day across both major apps, switching between them for")
    print("  menu variety, discount coupons, or faster delivery.")
    print("- Those who cook at home place very few orders on either app.")
    print("=" * 70)

    # -------------------------------------------------------------
    # 5. Scatter Plot Visualization
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 6), dpi=150)
    plt.scatter(x, y, color="#CB202D", s=130, edgecolors="black", linewidth=1.5, zorder=3, label="Friends")
    
    # Fit line
    m, c = np.polyfit(x, y, 1)
    x_line = np.linspace(min(x) - 2, max(x) + 2, 50)
    plt.plot(x_line, m * x_line + c, color="#FC8019", linestyle="--", linewidth=2, 
             label=f"Fit Line: y = {m:.2f}x + {c:.2f} (r = +{r:.3f})")

    # Annotate points
    for i, txt in enumerate(["Aarav", "Bhavna", "Chirag", "Divya", "Eshan", "Farhan"]):
        plt.annotate(
            f"{txt} ({x[i]}, {y[i]})",
            (x[i], y[i]),
            textcoords="offset points",
            xytext=(8, -4),
            fontsize=9,
            fontweight="semibold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#ccc", alpha=0.9)
        )

    plt.title("Zomato vs. Swiggy Monthly Order Counts (6 Friends)\nCorrelation Analysis using numpy.corrcoef()",
              fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Monthly Zomato Orders (Count)", fontsize=11, fontweight="semibold")
    plt.ylabel("Monthly Swiggy Orders (Count)", fontsize=11, fontweight="semibold")
    plt.grid(True, linestyle=":", alpha=0.6, zorder=0)
    plt.legend(loc="upper left")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(script_dir, "zomato_swiggy_scatter_plot.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"\n[+] Scatter plot saved successfully to: {plot_path}")

if __name__ == "__main__":
    run_task2()
