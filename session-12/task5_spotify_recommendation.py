"""
Session 12 - Task 5: Matrix Multiplication in Spotify's Recommendation System
File: session-12/task5_spotify_recommendation.py

Description:
Presents the ChatGPT inquiry regarding how matrix multiplication trains machine
learning models like Spotify's song recommendation engine, followed by a concise,
in-depth 3-4 sentence summary in our own words.
"""

def get_chatgpt_query_and_summary():
    query = "How does matrix multiplication help in training a machine learning model like Spotify's song recommendation system?"
    
    summary = (
        "In Spotify's recommendation engine, matrix multiplication is the core computational engine "
        "behind Matrix Factorization and Collaborative Filtering, where high-dimensional User-Song "
        "interaction matrices are decomposed into compact user preference and song feature embedding matrices. "
        "During model training, multiplying these user and song latent matrices allows the system to efficiently "
        "compute predicted affinity scores for hundreds of millions of user-track pairs simultaneously via parallel GPU processing. "
        "The model rapidly updates these embedding weights by multiplying error gradients against feature vectors during each training epoch. "
        "Ultimately, when Spotify generates personalized playlists like 'Discover Weekly', a single matrix multiplication between a user's "
        "taste vector and the global song matrix instantly scores and ranks thousands of recommended songs in milliseconds."
    )
    
    return query, summary


def run_task5():
    query, summary = get_chatgpt_query_and_summary()

    print("=" * 72)
    print(" TASK 5: MATRIX MULTIPLICATION IN SPOTIFY'S RECOMMENDATION SYSTEM")
    print("=" * 72)
    print("CHATGPT PROMPT SUBMITTED:")
    print(f"'{query}'")
    print("-" * 72)
    print("SUMMARY IN OUR OWN WORDS (3-4 SENTENCES):")
    print(summary)
    print("=" * 72)

    # Conceptual mathematical breakdown
    print("\nMATHEMATICAL WORKFLOW SUMMARY:")
    print("-" * 72)
    print("1. Matrix Factorization : R (Users x Songs) approx U (Users x k) x V^T (k x Songs)")
    print("2. Dot Product Matching : Predicted Rating = u_i . v_j")
    print("3. Batch Training Speed : Matrix multiplication enables full-matrix parallel")
    print("                          gradient updates on modern GPU accelerators.")
    print("=" * 72)


if __name__ == "__main__":
    run_task5()
