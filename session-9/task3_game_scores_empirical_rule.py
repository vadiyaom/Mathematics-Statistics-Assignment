"""
Session 9 - Task 3: Online Game Player Scores Simulation & 68-95-99.7 Rule
File: session-9/task3_game_scores_empirical_rule.py

Description:
Simulates scores of 200 online game players (PUBG / Free Fire) using a normal
distribution with:
- Mean (mu) = 70
- Standard Deviation (sigma) = 15
Counts the number of players scoring within one standard deviation [55, 85]
and verifies the result against the theoretical 68-95-99.7 Empirical Rule.
Generates a visualization plot saved to session-9/game_scores_distribution.png.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_task3(seed=42):
    if seed is not None:
        np.random.seed(seed)

    # -------------------------------------------------------------
    # 1. Simulation Parameters
    # -------------------------------------------------------------
    n_players = 200
    mu = 70.0
    sigma = 15.0

    # 1 SD Interval: [mu - sigma, mu + sigma] = [55.0, 85.0]
    lower_1sd = mu - sigma   # 55.0
    upper_1sd = mu + sigma   # 85.0

    # 2 SD Interval: [mu - 2*sigma, mu + 2*sigma] = [40.0, 100.0]
    lower_2sd = mu - 2 * sigma  # 40.0
    upper_2sd = mu + 2 * sigma  # 100.0

    # 3 SD Interval: [mu - 3*sigma, mu + 3*sigma] = [25.0, 115.0]
    lower_3sd = mu - 3 * sigma  # 25.0
    upper_3sd = mu + 3 * sigma  # 115.0

    # -------------------------------------------------------------
    # 2. Simulate 200 Player Scores
    # -------------------------------------------------------------
    scores = np.random.normal(loc=mu, scale=sigma, size=n_players)

    # Count players within 1 standard deviation
    within_1sd_mask = (scores >= lower_1sd) & (scores <= upper_1sd)
    count_1sd = int(np.sum(within_1sd_mask))
    pct_1sd = (count_1sd / n_players) * 100.0

    # Count players within 2 standard deviations
    within_2sd_mask = (scores >= lower_2sd) & (scores <= upper_2sd)
    count_2sd = int(np.sum(within_2sd_mask))
    pct_2sd = (count_2sd / n_players) * 100.0

    # Count players within 3 standard deviations
    within_3sd_mask = (scores >= lower_3sd) & (scores <= upper_3sd)
    count_3sd = int(np.sum(within_3sd_mask))
    pct_3sd = (count_3sd / n_players) * 100.0

    # -------------------------------------------------------------
    # 3. Theoretical Expectations via 68-95-99.7 Empirical Rule
    # -------------------------------------------------------------
    expected_pct_1sd = 68.27
    expected_count_1sd = n_players * (expected_pct_1sd / 100.0)  # ~136.54 players

    expected_pct_2sd = 95.45
    expected_count_2sd = n_players * (expected_pct_2sd / 100.0)  # ~190.90 players

    expected_pct_3sd = 99.73
    expected_count_3sd = n_players * (expected_pct_3sd / 100.0)  # ~199.46 players

    print("=" * 72)
    print(" TASK 3: ONLINE GAME PLAYER SCORES (PUBG / FREE FIRE) SIMULATION")
    print("=" * 72)
    print(f"Total Players Simulated (N)        : {n_players}")
    print(f"Population Mean (mu)               : {mu:.1f}")
    print(f"Population Std Dev (sigma)         : {sigma:.1f}")
    print(f"1 Standard Deviation Range [55, 85]: [{lower_1sd:.1f}, {upper_1sd:.1f}]")
    print("-" * 72)
    print("EMPIRICAL OBSERVATIONS VS. 68-95-99.7 RULE:")
    print("-" * 72)
    print(f"1. Players within 1 SD (55 to 85):")
    print(f"   - Observed Count      : {count_1sd} / {n_players} players ({pct_1sd:.2f}%)")
    print(f"   - Theoretical (68.27%): ~{expected_count_1sd:.1f} players ({expected_pct_1sd}%)")
    print(f"   - Discrepancy         : {abs(count_1sd - expected_count_1sd):.2f} players ({abs(pct_1sd - expected_pct_1sd):.2f}%)")
    print("-" * 72)
    print(f"2. Players within 2 SD (40 to 100):")
    print(f"   - Observed Count      : {count_2sd} / {n_players} players ({pct_2sd:.2f}%)")
    print(f"   - Theoretical (95.45%): ~{expected_count_2sd:.1f} players ({expected_pct_2sd}%)")
    print("-" * 72)
    print(f"3. Players within 3 SD (25 to 115):")
    print(f"   - Observed Count      : {count_3sd} / {n_players} players ({pct_3sd:.2f}%)")
    print(f"   - Theoretical (99.73%): ~{expected_count_3sd:.1f} players ({expected_pct_3sd}%)")
    print("=" * 72)

    # -------------------------------------------------------------
    # 4. Visualization Plot
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 6), dpi=150)

    # Histogram of player scores
    counts, bins, patches = plt.hist(
        scores, 
        bins=20, 
        color="#85C1E9", 
        edgecolor="#1B4F72", 
        alpha=0.75,
        label=f"Player Scores (N = {n_players})"
    )

    # Highlight the 1 SD region [55, 85]
    plt.axvspan(lower_1sd, upper_1sd, color="#F9E79F", alpha=0.35, 
                label=f"1 SD Region [55, 85]\n({count_1sd} players, {pct_1sd:.1f}%)")

    # Vertical reference lines
    plt.axvline(mu, color="#C0392B", linestyle="--", linewidth=2, label=f"Mean (mu = {mu:.0f})")
    plt.axvline(lower_1sd, color="#D35400", linestyle=":", linewidth=2, label=f"-1 SD ({lower_1sd:.0f})")
    plt.axvline(upper_1sd, color="#D35400", linestyle=":", linewidth=2, label=f"+1 SD ({upper_1sd:.0f})")

    plt.title(f"Simulation of 200 Online Game Scores (PUBG / Free Fire)\n68-95-99.7 Empirical Rule Verification", 
              fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Player Match Score", fontsize=11, fontweight="bold")
    plt.ylabel("Number of Players", fontsize=11, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right", frameon=True, fontsize=9)

    # Text summary box
    summary_txt = (
        f"68-95-99.7 Rule Verification:\n"
        f"Within [55, 85] (1 SD):\n"
        f"  - Observed: {count_1sd} players ({pct_1sd:.1f}%)\n"
        f"  - Expected: ~137 players (68.3%)\n"
        f"Sample Mean: {np.mean(scores):.1f}\n"
        f"Sample SD: {np.std(scores, ddof=1):.1f}"
    )
    plt.gca().text(
        0.04, 0.94, summary_txt,
        transform=plt.gca().transAxes,
        fontsize=8.5,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FDFEFE', edgecolor='#BDC3C7', alpha=0.95)
    )

    plt.tight_layout()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "game_scores_distribution.png")
    plt.savefig(output_path)
    plt.close()

    print(f"\n[+] Game scores distribution plot saved to: {output_path}")

if __name__ == "__main__":
    run_task3()

