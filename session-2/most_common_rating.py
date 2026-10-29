"""
Task 3: Find Mode (Most Common Rating) for Flipkart Products
File: most_common_rating.py
"""
from collections import Counter
import statistics

def most_common_rating(ratings):
    """
    Takes a list of ratings and returns the mode (most frequent rating).
    
    Parameters:
        ratings (list): List of numeric or categorical rating values.
        
    Returns:
        The rating value that appears with the highest frequency.
    """
    if not ratings:
        raise ValueError("Ratings list cannot be empty.")
    
    # Count frequency of each rating
    frequency_counts = Counter(ratings)
    
    # most_common(1) returns [(value, count)]
    mode_value, highest_count = frequency_counts.most_common(1)[0]
    
    return mode_value


if __name__ == "__main__":
    # Sample Flipkart product ratings
    sample_ratings = [5, 4, 4, 3, 5, 4, 2, 4]
    
    mode_rating = most_common_rating(sample_ratings)
    counts = Counter(sample_ratings)
    stats_mode = statistics.mode(sample_ratings)
    
    print("=" * 55)
    print(" Flipkart Product Ratings - Mode Calculation")
    print("=" * 55)
    print(f"Product Ratings List : {sample_ratings}")
    print(f"Rating Frequencies   : {dict(counts)}")
    print(f"Most Frequent Rating : {mode_rating} (appeared {counts[mode_rating]} times)")
    print(f"Verification (stats) : {stats_mode}")
    print("=" * 55)
