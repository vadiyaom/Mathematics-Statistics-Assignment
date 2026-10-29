"""
Session 8 - Task 3: Spotify Recent Songs Genre Probability
File: session-8/task3_spotify_genres.py


"""

from collections import Counter
import random

def calculate_genre_probability(genres_list: list, target_genre: str) -> dict:
    """
    Calculates the probability of selecting a target genre from a list of genres.

    Args:
        genres_list (list): List of genre strings.
        target_genre (str): The genre to find probability for (case-insensitive).

    Returns:
        dict: Detailed dictionary containing total count, target count, and probability.
    """
    if not genres_list:
        raise ValueError("The genres list cannot be empty.")

    # Standardize to lowercase for robust matching
    normalized_list = [g.strip().lower() for g in genres_list]
    target = target_genre.strip().lower()

    total_songs = len(normalized_list)
    target_count = normalized_list.count(target)
    probability = target_count / total_songs

    return {
        "total_songs": total_songs,
        "target_genre": target_genre,
        "target_count": target_count,
        "probability": probability,
        "percentage": probability * 100.0,
        "genre_counts": Counter(normalized_list)
    }


def run_task3():
    # -------------------------------------------------------------
    # 1. Dataset: Genres of Last 20 Played Spotify Songs
    # -------------------------------------------------------------
    spotify_genres = [
        'pop',  'rock',   'pop',    'hiphop', 'pop', 
        'indie', 'jazz',   'pop',    'rock',   'pop', 
        'classical', 'edm', 'hiphop', 'pop',  'rock', 
        'pop',  'r&b',    'pop',    'edm',    'pop'
    ]

    target = "pop"
    res = calculate_genre_probability(spotify_genres, target)

    print("=" * 68)
    print(" TASK 3: SPOTIFY RECENT HISTORY GENRE PROBABILITY")
    print("=" * 68)
    print(f"Total Songs in Recent History (n) : {res['total_songs']}")
    print(f"Target Genre                      : '{target}'")
    print(f"Occurrences of '{target}' in History : {res['target_count']}")
    print("-" * 68)
    print(f"Formula: P('{target}') = count('{target}') / total_songs")
    print(f"Calculation: P('{target}') = {res['target_count']} / {res['total_songs']}")
    print(f"Theoretical Probability: {res['probability']:.4f} ({res['percentage']:.2f}%)")
    print("=" * 68)

    # -------------------------------------------------------------
    # 2. Complete Distribution of All Genres
    # -------------------------------------------------------------
    print("\nCOMPLETE GENRE BREAKDOWN IN LAST 20 SONGS:")
    print("-" * 68)
    print(f"{'Genre':<14} | {'Song Count':<12} | {'Probability':<14} | {'Percentage':<12}")
    print("-" * 68)
    # Sort genres by count descending
    for genre, count in res['genre_counts'].most_common():
        p = count / res['total_songs']
        is_target = " <-- (Target)" if genre == target.lower() else ""
        print(f"{genre.capitalize():<14} | {count:<12} | {p:<14.4f} | {p*100:<10.1f}%{is_target}")
    print("-" * 68)
    print(f"{'Total':<14} | {res['total_songs']:<12} | {1.0:<14.4f} | 100.0%")
    print("=" * 68)

    # -------------------------------------------------------------
    # 3. Monte Carlo Verification (Random Pick Simulation)
    # -------------------------------------------------------------
    trials = 100000
    random.seed(42)
    pop_picks = sum(1 for _ in range(trials) if random.choice(spotify_genres) == target)
    simulated_prob = pop_picks / trials

    print("\nMONTE CARLO EMPIRICAL VERIFICATION (100,000 Random Picks):")
    print("-" * 68)
    print(f"Simulated Picks of '{target}' : {pop_picks} / {trials}")
    print(f"Empirical Pick Probability    : {simulated_prob:.4f} ({simulated_prob * 100:.2f}%)")
    print(f"Theoretical Probability       : {res['probability']:.4f} ({res['percentage']:.2f}%)")
    print(f"Difference                    : {abs(simulated_prob - res['probability']):.5f}")
    print("=" * 68)


if __name__ == "__main__":
    run_task3()

