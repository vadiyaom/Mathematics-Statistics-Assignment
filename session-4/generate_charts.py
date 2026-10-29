"""
Session 4: Generate Graphs for Task 1 and Task 4
File: generate_charts.py
"""
import matplotlib.pyplot as plt
import numpy as np
import os

def create_charts():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    # -------------------------------------------------------------
    # Chart 1: Swiggy Daily Order Counts (Task 1) - Right Skewed
    # -------------------------------------------------------------
    swiggy_orders = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]
    days = [f"Day {i+1}" for i in range(len(swiggy_orders))]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Bar plot across days
    colors = ['#3b82f6' if x < 100 else '#ef4444' for x in swiggy_orders]
    ax1.bar(days, swiggy_orders, color=colors, edgecolor='black', alpha=0.85)
    ax1.set_title("Swiggy Delivery Partner Daily Orders (10 Days)", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Days", fontsize=10)
    ax1.set_ylabel("Order Count", fontsize=10)
    ax1.tick_params(axis='x', rotation=45)
    ax1.axhline(np.mean(swiggy_orders), color='red', linestyle='--', label=f"Mean = {np.mean(swiggy_orders):.1f}")
    ax1.axhline(np.median(swiggy_orders), color='green', linestyle='-', label=f"Median = {np.median(swiggy_orders):.1f}")
    ax1.legend()
    
    # Histogram showing distribution shape
    ax2.hist(swiggy_orders, bins=15, color='#f97316', edgecolor='black', alpha=0.8)
    ax2.set_title("Distribution Shape: Long Tail to the Right (Right-Skewed)", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Order Count Range", fontsize=10)
    ax2.set_ylabel("Frequency (Days)", fontsize=10)
    ax2.axvline(np.mean(swiggy_orders), color='red', linestyle='--', label=f"Mean = {np.mean(swiggy_orders):.1f}")
    ax2.axvline(np.median(swiggy_orders), color='green', linestyle='-', label=f"Median = {np.median(swiggy_orders):.1f}")
    ax2.legend()
    
    plt.tight_layout()
    chart1_path = os.path.join(output_dir, "swiggy_orders_plot.png")
    plt.savefig(chart1_path, dpi=150)
    plt.close()
    print(f"Created Chart 1: {chart1_path}")
    
    # -------------------------------------------------------------
    # Chart 2: Flipkart Product Ratings (Task 4) - Left Skewed
    # -------------------------------------------------------------
    ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
    unique_ratings = [1, 2, 3, 4, 5]
    counts = [ratings.count(r) for r in unique_ratings]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(unique_ratings, counts, color='#10b981', edgecolor='black', width=0.6, alpha=0.85)
    
    # Annotate bar counts
    for bar in bars:
        yval = bar.get_height()
        if yval > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, str(yval), ha='center', va='bottom', fontweight='bold')
            
    mean_val = np.mean(ratings)
    median_val = np.median(ratings)
    mode_val = 5
    
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f"Mean = {mean_val:.2f}")
    ax.axvline(median_val, color='blue', linestyle='-.', linewidth=2, label=f"Median = {median_val:.1f}")
    ax.axvline(mode_val, color='purple', linestyle=':', linewidth=2, label=f"Mode = {mode_val}")
    
    ax.set_title("Flipkart Product Ratings Distribution (Left-Skewed / Negative Skew)", fontsize=12, fontweight='bold')
    ax.set_xlabel("Star Rating", fontsize=11)
    ax.set_ylabel("Number of Reviews (Frequency)", fontsize=11)
    ax.set_xticks(unique_ratings)
    ax.set_ylim(0, 6)
    ax.legend()
    
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, "flipkart_ratings_plot.png")
    plt.savefig(chart2_path, dpi=150)
    plt.close()
    print(f"Created Chart 2: {chart2_path}")

if __name__ == "__main__":
    create_charts()
