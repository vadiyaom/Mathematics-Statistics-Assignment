"""
Session 8 - Task 2: Dice Rolling Simulation (100 Trials)
File: session-8/task2_dice_simulation.py

"""

import os
import random
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_task2(seed=42):
    # Set seed for reproducible run results, but the code works with any seed
    if seed is not None:
        random.seed(seed)

    num_rolls = 100
    rolls = []
    count_6 = 0

    # -------------------------------------------------------------
    # 1. Simulate 100 Dice Rolls using random.randint(1, 6)
    # -------------------------------------------------------------
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        rolls.append(roll)
        if roll == 6:
            count_6 += 1

    # -------------------------------------------------------------
    # 2. Probability Calculations
    # -------------------------------------------------------------
    # Experimental (Empirical) Probability: count / total trials
    experimental_prob = count_6 / num_rolls
    
    # Theoretical Probability for a fair 6-sided die: 1/6
    theoretical_prob = 1.0 / 6.0

    # Error analysis
    abs_error = abs(experimental_prob - theoretical_prob)
    rel_error = (abs_error / theoretical_prob) * 100

    # Count occurrences of all faces for complete breakdown
    face_counts = Counter(rolls)

    print("=" * 68)
    print(" TASK 2: 100 DICE ROLLS SIMULATION & EXPERIMENTAL PROBABILITY")
    print("=" * 68)
    print(f"Total Simulation Trials (N)      : {num_rolls}")
    print(f"Target Face                      : '6'")
    print(f"Number of times '6' appeared     : {count_6}")
    print("-" * 68)
    print(f"Experimental Probability P_exp(6): {count_6} / {num_rolls} = {experimental_prob:.4f} ({experimental_prob * 100:.2f}%)")
    print(f"Theoretical Probability P_th(6)  : 1 / 6    = {theoretical_prob:.4f} ({theoretical_prob * 100:.2f}%)")
    print(f"Absolute Difference              : {abs_error:.4f} ({abs_error * 100:.2f} percentage points)")
    print(f"Relative Percentage Error        : {rel_error:.2f}%")
    print("-" * 68)
    print("Full Frequency Distribution Across All 6 Faces:")
    print(f"{'Face':<8} | {'Occurrences':<14} | {'Experimental Prob':<18} | {'Theoretical Prob':<18}")
    print("-" * 68)
    for face in range(1, 7):
        cnt = face_counts.get(face, 0)
        prob = cnt / num_rolls
        print(f"  {face:<6} | {cnt:<14} | {prob:<18.4f} | {theoretical_prob:<18.4f}")
    print("=" * 68)

    # -------------------------------------------------------------
    # 3. Demonstration of Law of Large Numbers (Convergence)
    # -------------------------------------------------------------
    print("\nLAW OF LARGE NUMBERS CONVERGENCE CHECK:")
    print("-" * 68)
    print("Trials (N) | Count of 6s | Experimental P(6) | Theoretical P(6) | Difference")
    print("-" * 68)
    for n_test in [100, 1000, 10000, 100000]:
        c6 = sum(1 for _ in range(n_test) if random.randint(1, 6) == 6)
        p_exp = c6 / n_test
        diff = abs(p_exp - theoretical_prob)
        print(f"{n_test:<10} | {c6:<11} | {p_exp:<17.4f} | {theoretical_prob:<16.4f} | {diff:.4f}")
    print("=" * 68)

    # -------------------------------------------------------------
    # 4. Visualization Bar Chart
    # -------------------------------------------------------------
    faces = list(range(1, 7))
    counts = [face_counts.get(f, 0) for f in faces]
    colors = ['#3498DB' if f != 6 else '#E74C3C' for f in faces]

    plt.figure(figsize=(8, 5.5), dpi=150)
    bars = plt.bar(faces, counts, color=colors, edgecolor='black', linewidth=1.2, width=0.6, zorder=3)
    
    # Add counts on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                 f"{int(height)}", ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Add theoretical expected value line (100 * 1/6 = 16.67)
    expected_count = num_rolls * theoretical_prob
    plt.axhline(expected_count, color='#2ECC71', linestyle='--', linewidth=2,
                label=f"Expected Frequency = {expected_count:.2f} (16.67%)", zorder=4)

    plt.title(f"Simulation of 100 Dice Rolls (Face '6' Frequency = {count_6})", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Dice Face (Outcomes 1 to 6)", fontsize=11, fontweight='semibold')
    plt.ylabel("Observed Frequency (Count)", fontsize=11, fontweight='semibold')
    plt.xticks(faces)
    plt.ylim(0, max(counts) + 5)
    plt.grid(axis='y', linestyle=':', alpha=0.7, zorder=0)
    plt.legend(loc='upper right', frameon=True)

    # Add text summary box
    summary_txt = (
        f"Trial Count: 100\n"
        f"Face '6' Count: {count_6}\n"
        f"P_exp(6): {experimental_prob:.4f} ({experimental_prob*100:.1f}%)\n"
        f"P_th(6): {theoretical_prob:.4f} ({theoretical_prob*100:.2f}%)"
    )
    plt.gca().text(
        0.04, 0.94, summary_txt,
        transform=plt.gca().transAxes,
        fontsize=9,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FDFEFE', edgecolor='#BDC3C7', alpha=0.95)
    )

    plt.tight_layout()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "dice_simulation_plot.png")
    plt.savefig(output_path)
    plt.close()

    print(f"\n[+] Dice simulation bar plot saved successfully to: {output_path}")


if __name__ == "__main__":
    run_task2()

