"""
Session 8 - Task 1: Basic Probability Calculation & Coin Toss
File: session-8/task1_coin_toss.py


"""

def calculate_probability(event_count: int, total_outcomes: int) -> float:
    """
    Calculates the probability of an event occurring in an equally likely sample space.

    Formula:
        P(E) = favorable_outcomes / total_possible_outcomes

    Args:
        event_count (int): Number of favorable outcomes for the event.
        total_outcomes (int): Total number of possible outcomes in the sample space.

    Returns:
        float: Probability value between 0.0 and 1.0.

    Raises:
        ValueError: If total_outcomes is <= 0 or event_count < 0 or event_count > total_outcomes.
    """
    if total_outcomes <= 0:
        raise ValueError("Total outcomes must be strictly greater than zero.")
    if event_count < 0:
        raise ValueError("Event count cannot be negative.")
    if event_count > total_outcomes:
        raise ValueError("Event count cannot exceed total possible outcomes.")

    return event_count / total_outcomes


def run_task1():
    print("=" * 65)
    print(" TASK 1: BASIC PROBABILITY CALCULATION (COIN TOSS)")
    print("=" * 65)

    # Sample space for tossing a fair coin:
    # S = {'Heads', 'Tails'}
    sample_space = ['Heads', 'Tails']
    total_outcomes = len(sample_space)

    # Event E = Getting 'Heads'
    # Favorable outcomes = {'Heads'}
    event_outcomes = ['Heads']
    event_count = len(event_outcomes)

    # Calculate probability
    prob_heads = calculate_probability(event_count, total_outcomes)
    prob_tails = calculate_probability(total_outcomes - event_count, total_outcomes)

    print(f"Sample Space (S)             : {sample_space}")
    print(f"Total Possible Outcomes (n)  : {total_outcomes}")
    print(f"Target Event (E)             : Getting 'Heads'")
    print(f"Favorable Outcomes Count (k) : {event_count}")
    print("-" * 65)
    print(f"Formula                      : P(E) = k / n")
    print(f"Calculation                  : P('Heads') = {event_count} / {total_outcomes}")
    print(f"Probability (Decimal)        : {prob_heads:.4f}")
    print(f"Probability (Percentage)     : {prob_heads * 100:.2f}%")
    print(f"Probability (Fraction)       : 1/2")
    print("-" * 65)
    print(f"Complement Event P('Tails')  : {prob_tails:.4f} ({prob_tails * 100:.1f}%)")
    print(f"Sum of Probabilities         : {prob_heads + prob_tails:.1f} (Axiom of Probability)")
    print("=" * 65)


if __name__ == "__main__":
    run_task1()

