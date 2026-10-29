"""
Task 1: Calculate Mean Daily Spotify Song Plays
File: playlist_stats.py
"""

def calculate_mean(play_counts):
    """
    Calculates the mean (average) number of plays from a list of play counts.
    
    Formula: Mean = sum(x) / n
    where:
      sum(x) = total sum of all daily play counts
      n      = number of days observed
    """
    if not play_counts:
        raise ValueError("The list of play counts cannot be empty.")
    
    total_plays = sum(play_counts)
    total_days = len(play_counts)
    mean_plays = total_plays / total_days
    return mean_plays


if __name__ == "__main__":
    # Sample daily play counts for a Spotify song over a week
    sample_play_counts = [120, 135, 150, 200, 120, 90, 200]
    
    mean_result = calculate_mean(sample_play_counts)
    
    print("=" * 55)
    print(" Spotify Playlist Daily Play Count Statistics")
    print("=" * 55)
    print(f"Daily Play Counts : {sample_play_counts}")
    print(f"Total Days (n)    : {len(sample_play_counts)}")
    print(f"Total Plays (sum) : {sum(sample_play_counts)}")
    print(f"Mean Daily Plays  : {mean_result:.2f}")
    print("=" * 55)
