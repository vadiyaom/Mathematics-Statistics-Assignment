"""
Task 2: Two-Sample t-Test for Zomato Home Page Average Order Value
File: zomato_ttest.py
"""
from scipy import stats
import math

def perform_zomato_ttest():
    # Given data
    mean_A = 350.0   # Group A (New Home Page)
    std_A  = 50.0
    n_A    = 30

    mean_B = 320.0   # Group B (Old Home Page)
    std_B  = 50.0
    n_B    = 30

    alpha = 0.05

    # 1. Degrees of Freedom
    df = n_A + n_B - 2  # 30 + 30 - 2 = 58

    # 2. Pooled Standard Deviation & Standard Error
    # Since std_A == std_B == 50, pooled std is exactly 50
    sp = math.sqrt(((n_A - 1) * (std_A ** 2) + (n_B - 1) * (std_B ** 2)) / df)
    se = sp * math.sqrt((1 / n_A) + (1 / n_B))

    # 3. Calculated t-statistic
    t_stat_manual = (mean_A - mean_B) / se

    # 4. Calculation using scipy.stats
    t_stat, p_val_two_tailed = stats.ttest_ind_from_stats(
        mean1=mean_A, std1=std_A, nobs1=n_A,
        mean2=mean_B, std2=std_B, nobs2=n_B,
        equal_var=True
    )
    p_val_one_tailed = p_val_two_tailed / 2.0

    print("=" * 70)
    print(" Zomato Home Page A/B Test - Two-Sample t-Test Results")
    print("=" * 70)
    print(f"Group A (New Page) : Mean = Rs. {mean_A:.2f}, SD = Rs. {std_A:.2f}, n = {n_A}")
    print(f"Group B (Old Page) : Mean = Rs. {mean_B:.2f}, SD = Rs. {std_B:.2f}, n = {n_B}")
    print(f"Degrees of Freedom : {df}")
    print(f"Pooled Std Dev (sp): Rs. {sp:.2f}")
    print(f"Standard Error (SE): Rs. {se:.4f}")
    print(f"t-Statistic        : {t_stat:.4f}")
    print("-" * 70)
    print(f"Two-Tailed p-value : {p_val_two_tailed:.5f} (approx. 0.0237)")
    print(f"One-Tailed p-value : {p_val_one_tailed:.5f} (approx. 0.0118)")
    print(f"Significance Level : alpha = {alpha}")
    print("=" * 70)

    # Statistical Decision
    print("\nDECISION & INTERPRETATION:")
    print("=" * 70)
    if p_val_two_tailed < alpha:
        print(f"Result : p-value ({p_val_two_tailed:.4f}) < alpha (0.05)")
        print("Decision: REJECT THE NULL HYPOTHESIS (H0).")
        print("Conclusion: There is statistically significant evidence that the new Zomato")
        print("            home page design increases the average order value (Rs. 350 vs Rs. 320).")
    else:
        print(f"Result : p-value ({p_val_two_tailed:.4f}) >= alpha (0.05)")
        print("Decision: FAIL TO REJECT (ACCEPT) THE NULL HYPOTHESIS (H0).")
        print("Conclusion: The difference is not statistically significant.")
    print("=" * 70)

if __name__ == "__main__":
    perform_zomato_ttest()
