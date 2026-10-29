"""
Task 4: Salary Variance, Standard Deviation, and Spread Interpretation
File: salary_spread.py
"""
import math
import statistics

def analyze_salaries(salaries):
    n = len(salaries)
    mean_val = sum(salaries) / n
    deviations = [x - mean_val for x in salaries]
    sq_deviations = [d ** 2 for d in deviations]
    sum_sq = sum(sq_deviations)
    
    # Population metrics (N = 6)
    pop_variance = sum_sq / n
    pop_std_dev = math.sqrt(pop_variance)
    
    # Sample metrics (n - 1 = 5)
    sample_variance = sum_sq / (n - 1)
    sample_std_dev = math.sqrt(sample_variance)
    
    return {
        "salaries": salaries,
        "n": n,
        "mean": mean_val,
        "sum_sq": sum_sq,
        "pop_var": pop_variance,
        "pop_sd": pop_std_dev,
        "sample_var": sample_variance,
        "sample_sd": sample_std_dev
    }

if __name__ == "__main__":
    salaries = [28000, 29000, 27000, 60000, 26500, 27500]
    res = analyze_salaries(salaries)
    
    print("=" * 70)
    print(" Startup Employee Monthly Salary Spread Analysis")
    print("=" * 70)
    print(f"Salaries (Rs.)            : {res['salaries']}")
    print(f"Number of Employees (n)   : {res['n']}")
    print(f"Mean Salary (Rs.)         : Rs. {res['mean']:,.2f}")
    print(f"Sum of Squared Deviations : {res['sum_sq']:,.2f}")
    print("-" * 70)
    print("POPULATION METRICS (N = 6):")
    print(f"  Variance (sigma^2)      : {res['pop_var']:,.2f}")
    print(f"  Standard Deviation      : Rs. {res['pop_sd']:,.2f}")
    print("-" * 70)
    print("SAMPLE METRICS (n - 1 = 5):")
    print(f"  Variance (s^2)          : {res['sample_var']:,.2f}")
    print(f"  Standard Deviation (s)  : Rs. {res['sample_sd']:,.2f}")
    print("=" * 70)
    print("\nINTERPRETATION (2-3 lines):")
    print("=" * 70)
    interpretation = (
        "The exceptionally high variance and standard deviation (over Rs. 12,000 to 13,000) reveal\n"
        "severe compensation inequality within this startup team. While 5 out of 6 team members\n"
        "earn very similar salaries clustered tightly between Rs. 26,500 and Rs. 29,000, a single\n"
        "outlier of Rs. 60,000 (likely a founder or senior lead) creates an artificially high\n"
        "mean (Rs. 33,000) and produces a large spread across the team."
    )
    print(interpretation)
    print("=" * 70)
