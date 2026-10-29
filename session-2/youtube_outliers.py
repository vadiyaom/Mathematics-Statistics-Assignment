"""
Task 4: Compare Mean, Median, and Mode of YouTube Video Views Across Channels
File: youtube_outliers.py
"""
import statistics
from collections import Counter

def get_mode(data):
    """Returns the mode or first modal value."""
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def analyze_channel(name, views):
    """Calculates Mean, Median, Mode, and Outlier Sensitivity metric."""
    mean_val = statistics.mean(views)
    median_val = statistics.median(views)
    mode_val = get_mode(views)
    
    # Absolute difference between Mean and Median highlights outlier pull
    diff = abs(mean_val - median_val)
    pct_distortion = (diff / median_val) * 100 if median_val != 0 else 0
    
    return {
        "name": name,
        "views": views,
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "diff": diff,
        "pct_distortion": pct_distortion
    }

if __name__ == "__main__":
    # Three YouTube channels with distinct view distributions
    channels = {
        "Channel 1 (Tech Tutorials - Consistent)": [1200, 1250, 1200, 1300, 1280, 1220, 1200],
        "Channel 2 (Daily Vlogs - Moderate Variance)": [800, 950, 850, 900, 850, 1100, 920],
        "Channel 3 (Viral Clips - High Outlier)": [100, 120, 110, 105, 120, 5000]
    }
    
    results = [analyze_channel(name, views) for name, views in channels.items()]
    
    print("=" * 80)
    print(f"{'Channel Name':<42} | {'Mean':>10} | {'Median':>8} | {'Mode':>8} | {'|Mean-Median|':>12}")
    print("=" * 80)
    for res in results:
        mode_str = str(res['mode'])
        print(f"{res['name']:<42} | {res['mean']:>10.2f} | {res['median']:>8.1f} | {mode_str:>8} | {res['diff']:>12.2f}")
    print("=" * 80)
    
    # Identify the channel most affected by outliers
    most_affected = max(results, key=lambda x: x['diff'])
    
    print("\n" + "=" * 80)
    print(f"CONCLUSION: {most_affected['name']} is the MOST affected by outliers.")
    print("=" * 80)
    print(f"- Normal Typical Views: ~100 to 120 views")
    print(f"- Viral Outlier: 5000 views")
    print(f"- Effect on Mean: The single outlier pulled the mean up to {most_affected['mean']:.2f},")
    print(f"  which is misleading because 5 out of 6 videos received fewer than 125 views.")
    print(f"- Effect on Median: The median remained stable at {most_affected['median']:.1f}, accurately")
    print(f"  representing typical channel performance.")
    print(f"- Why? The arithmetic mean incorporates every data point into its sum, making it highly")
    print(f"  sensitive to extreme values, whereas the median is a robust statistic based solely on")
    print(f"  middle ranking position.")
    print("=" * 80)
