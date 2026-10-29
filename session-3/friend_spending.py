"""
Task 3: Compare Spending Consistency of Two Friends on Zomato
File: friend_spending.py
"""
import math
import statistics

def compute_stats(spending_list, name):
    n = len(spending_list)
    mean_val = sum(spending_list) / n
    sq_diffs = [(x - mean_val) ** 2 for x in spending_list]
    
    # Sample standard deviation (n-1)
    sample_var = sum(sq_diffs) / (n - 1)
    sample_std = math.sqrt(sample_var)
    
    # Population standard deviation (N)
    pop_var = sum(sq_diffs) / n
    pop_std = math.sqrt(pop_var)
    
    return {
        "name": name,
        "data": spending_list,
        "mean": mean_val,
        "sample_std": round(sample_std, 2),
        "pop_std": round(pop_std, 2)
    }

if __name__ == "__main__":
    friend_a = [200, 200, 200, 200, 200]
    friend_b = [100, 300, 150, 400, 50]
    
    stats_a = compute_stats(friend_a, "Friend A")
    stats_b = compute_stats(friend_b, "Friend B")
    
    print("=" * 65)
    print(" Zomato 5-Day Daily Spending Comparison")
    print("=" * 65)
    for s in [stats_a, stats_b]:
        print(f"Friend                  : {s['name']}")
        print(f"Daily Spending (Rs.)    : {s['data']}")
        print(f"Mean Spending (Rs.)     : Rs. {s['mean']:.2f}")
        print(f"Sample Std Deviation    : Rs. {s['sample_std']:.2f}")
        print(f"Population Std Deviation: Rs. {s['pop_std']:.2f}")
        print("-" * 65)
        
    print("\n" + "=" * 65)
    print("CONSISTENCY EXPLANATION (2-3 lines):")
    print("=" * 65)
    explanation = (
        "Friend A has significantly more consistent spending because their standard deviation\n"
        "is Rs. 0.00, meaning their spending never deviates from the average of Rs. 200 every day.\n"
        "In contrast, Friend B has high variability (standard deviation of Rs. 145.77), fluctuating\n"
        "widely between Rs. 50 and Rs. 400 despite maintaining the exact same Rs. 200 daily average."
    )
    print(explanation)
    print("=" * 65)
