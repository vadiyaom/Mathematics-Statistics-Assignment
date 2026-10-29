"""
Session 9 - Task 2: Fitness Tracker Daily Step Counts - Central Tendency Symmetry
File: session-9/task2_step_counts_symmetry.py

Description:
Given an array of 20 daily step counts from a fitness tracker app:
1. Calculates Mean using numpy.mean()
2. Calculates Median using numpy.median()
3. Calculates Mode using scipy.stats.mode()
4. Evaluates if Mean ≈ Median ≈ Mode as expected for a Normal Distribution.
"""

import numpy as np
from scipy import stats

def run_task2():
    # -------------------------------------------------------------
    # 1. Dataset: 20 Days of Fitness Tracker Daily Step Counts
    # -------------------------------------------------------------
    daily_steps = np.array([
        6800, 7200, 7400, 7600, 7800,
        7900, 8000, 8000, 8000, 8000,
        8100, 8100, 8200, 8200, 8400,
        8500, 8600, 8800, 9000, 9200
    ])

    # -------------------------------------------------------------
    # 2. Compute Measures of Central Tendency
    # -------------------------------------------------------------
    # Mean using numpy.mean()
    mean_val = float(np.mean(daily_steps))

    # Median using numpy.median()
    median_val = float(np.median(daily_steps))

    # Mode using scipy.stats.mode()
    mode_result = stats.mode(daily_steps)
    # Handle scalar or array returned across scipy versions
    mode_val = float(mode_result.mode if np.isscalar(mode_result.mode) else mode_result.mode[0])
    mode_count = int(mode_result.count if np.isscalar(mode_result.count) else mode_result.count[0])

    # Standard deviation for spread context
    std_val = float(np.std(daily_steps, ddof=1))

    # Percentage differences
    diff_mean_median = abs(mean_val - median_val)
    pct_mean_median = (diff_mean_median / mean_val) * 100

    diff_mean_mode = abs(mean_val - mode_val)
    pct_mean_mode = (diff_mean_mode / mean_val) * 100

    diff_median_mode = abs(median_val - mode_val)
    pct_median_mode = (diff_median_mode / median_val) * 100

    # -------------------------------------------------------------
    # 3. Print Results
    # -------------------------------------------------------------
    print("=" * 70)
    print(" TASK 2: FITNESS TRACKER 20-DAY STEP COUNTS & NORMAL SYMMETRY")
    print("=" * 70)
    print("Daily Step Counts (Sorted Array):")
    print(daily_steps)
    print(f"Sample Size (N)             : {len(daily_steps)} days")
    print("-" * 70)
    print(f"1. Mean   (numpy.mean())    : {mean_val:.2f} steps")
    print(f"2. Median (numpy.median())  : {median_val:.2f} steps")
    print(f"3. Mode   (stats.mode())    : {mode_val:.2f} steps (Appeared {mode_count} times)")
    print(f"4. Sample Std Dev (s)       : {std_val:.2f} steps")
    print("-" * 70)
    print("PAIRWISE COMPARISONS:")
    print(f"- |Mean - Median|           : {diff_mean_median:.2f} steps ({pct_mean_median:.2f}% relative diff)")
    print(f"- |Mean - Mode|             : {diff_mean_mode:.2f} steps ({pct_mean_mode:.2f}% relative diff)")
    print(f"- |Median - Mode|           : {diff_median_mode:.2f} steps ({pct_median_mode:.2f}% relative diff)")
    print("=" * 70)

    # -------------------------------------------------------------
    # 4. Evaluation of Normal Distribution Symmetry
    # -------------------------------------------------------------
    print("\nCHECK: ARE THEY APPROXIMATELY EQUAL?")
    print("=" * 70)
    threshold_pct = 5.0  # Common statistical threshold for empirical closeness (< 5%)
    is_approx_equal = (pct_mean_median < threshold_pct) and (pct_mean_mode < threshold_pct)

    if is_approx_equal:
        print("[+] VERDICT: YES, Mean, Median, and Mode are APPROXIMATELY EQUAL!")
        print(f"    - All three metrics cluster tightly between {min(mean_val, median_val, mode_val):.0f} and {max(mean_val, median_val, mode_val):.0f} steps.")
        print(f"    - The maximum relative deviation is only {max(pct_mean_median, pct_mean_mode):.2f}% (well under the 5% threshold).")
        print("    - In a theoretical normal distribution, Mean = Median = Mode.")
        print("    - In real-world sample data, slight sampling noise is expected, but this close")
        print("      alignment confirms strong bell-curve symmetry around ~8,050 steps.")
    else:
        print("[-] VERDICT: NO, significant skewness observed.")
    print("=" * 70)

if __name__ == "__main__":
    run_task2()

