"""
Session 11 - Task 1: Spotify Playlist Duration Calculation
File: session-11/task1_playlist_duration.py

Description:
Creates a Python list representing a playlist of 5 song durations in seconds.
Calculates and prints the total duration in both raw seconds and formatted
minutes and seconds (MM:SS).
"""

def calculate_playlist_duration(durations: list) -> dict:
    """
    Calculates total and average duration for a list of song durations in seconds.

    Args:
        durations (list): List of integer song durations in seconds.

    Returns:
        dict: Summary statistics including total seconds, formatted time, and song count.
    """
    if not durations:
        raise ValueError("Durations list cannot be empty.")

    total_seconds = sum(durations)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    avg_seconds = total_seconds / len(durations)

    return {
        "song_count": len(durations),
        "durations": durations,
        "total_seconds": total_seconds,
        "minutes": minutes,
        "remaining_seconds": seconds,
        "formatted_duration": f"{minutes}m {seconds:02d}s",
        "average_seconds": avg_seconds
    }


def run_task1():
    # -------------------------------------------------------------
    # 1. Dataset: 5 Song Durations in Seconds
    # -------------------------------------------------------------
    song_durations = [210, 180, 245, 200, 175]
    song_titles = [
        "Song 1: Starboy - The Weeknd",
        "Song 2: Levitating - Dua Lipa",
        "Song 3: Bohemian Rhapsody - Queen",
        "Song 4: Blinding Lights - The Weeknd",
        "Song 5: Shape of You - Ed Sheeran"
    ]

    result = calculate_playlist_duration(song_durations)

    print("=" * 65)
    print(" TASK 1: PLAYLIST DURATION CALCULATION (5 SONGS)")
    print("=" * 65)
    print(f"{'#':<3} | {'Track Title':<38} | {'Duration (sec)':<14}")
    print("-" * 65)
    for idx, (title, dur) in enumerate(zip(song_titles, song_durations), 1):
        m, s = divmod(dur, 60)
        print(f"{idx:<3} | {title:<38} | {dur:<4}s ({m}:{s:02d})")
    print("-" * 65)
    print(f"Total Songs in Playlist      : {result['song_count']}")
    print(f"List of Durations (seconds)  : {song_durations}")
    print(f"Total Playlist Duration      : {result['total_seconds']} seconds")
    print(f"Formatted Playlist Duration  : {result['formatted_duration']} ({result['minutes']} minutes, {result['remaining_seconds']} seconds)")
    print(f"Average Song Duration        : {result['average_seconds']:.1f} seconds")
    print("=" * 65)


if __name__ == "__main__":
    run_task1()

