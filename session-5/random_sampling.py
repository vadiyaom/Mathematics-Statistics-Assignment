"""
Task 2: Simulate Random Sampling of 50 Users from 1,000 Fake Users
File: random_sampling.py
"""
import random

def simulate_random_sampling(population_size=1000, sample_size=50, seed=42):
    """
    Simulates simple random sampling (without replacement) from a population of users.
    
    Parameters:
        population_size (int): Total number of fake user IDs in the population.
        sample_size (int): Number of users to randomly select for the survey sample.
        seed (int, optional): Random seed for reproducible results.
        
    Returns:
        list: The randomly selected sample of user IDs.
    """
    if seed is not None:
        random.seed(seed)
        
    # 1. Generate a population of 1000 fake user IDs (e.g., user1 to user1000)
    population = [f"user{i}" for i in range(1, population_size + 1)]
    
    # 2. Select 50 random users without replacement using random.sample()
    sample = random.sample(population, sample_size)
    
    return population, sample


if __name__ == "__main__":
    pop_size = 1000
    samp_size = 50
    
    population, selected_sample = simulate_random_sampling(pop_size, samp_size, seed=42)
    
    print("=" * 70)
    print(" Python Random Sampling Simulation (Survey Sample)")
    print("=" * 70)
    print(f"Total Population Size (N) : {len(population)} users ({population[0]} to {population[-1]})")
    print(f"Sample Size Selected (n)  : {len(selected_sample)} users")
    print(f"Sampling Ratio (n / N)    : {len(selected_sample) / len(population) * 100:.1f}%")
    print("-" * 70)
    print("Selected 50 Random User IDs for the Survey:")
    print("-" * 70)
    
    # Print the 50 selected user IDs in neat rows of 5
    for i in range(0, len(selected_sample), 5):
        row = selected_sample[i:i+5]
        formatted_row = "  ".join(f"{uid:<10}" for uid in row)
        print(f"  [{i+1:02d}-{min(i+5, len(selected_sample)):02d}]: {formatted_row}")
        
    print("=" * 70)
