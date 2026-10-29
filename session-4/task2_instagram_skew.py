"""
Task 2: Instagram Influencer Follower Counts Skewness
File: task2_instagram_skew.py
"""
import statistics

def analyze_instagram_followers():
    followers = [5, 7, 8, 8, 9, 10, 12, 15, 95]
    n = len(followers)
    
    mean_val = statistics.mean(followers)
    median_val = statistics.median(followers)
    mode_val = statistics.mode(followers)
    
    print("=" * 60)
    print(" Instagram Influencer Follower Counts (in thousands)")
    print("=" * 60)
    print(f"Data Points (in '000s) : {followers}")
    print(f"Total Influencers (n)  : {n}")
    print(f"Mean Follower Count    : {mean_val:.2f}k (18,778 followers)")
    print(f"Median Follower Count  : {median_val:.2f}k (9,000 followers)")
    print(f"Mode Follower Count    : {mode_val:.2f}k (8,000 followers)")
    print("-" * 60)
    
    if mean_val > median_val:
        print("Comparison: The MEAN is higher than the MEDIAN (18.78 > 9.00).")
        print("Conclusion: The data is RIGHT-SKEWED (Positively Skewed).")
        print("Reasoning : The extreme outlier (95k) pulls the mean far to the right,")
        print("            even though most influencers have 15k or fewer followers.")
    elif mean_val < median_val:
        print("Comparison: The MEAN is lower than the MEDIAN.")
        print("Conclusion: The data is LEFT-SKEWED (Negatively Skewed).")
    else:
        print("Comparison: Mean equals Median.")
        print("Conclusion: The data is SYMMETRICAL.")
    print("=" * 60)

if __name__ == "__main__":
    analyze_instagram_followers()
