"""
Session 10 - Task 1: Bayes' Theorem Posterior Probability Calculator
File: session-10/task1_bayes_posterior.py

Description:
Defines the core mathematical function:
    bayes_posterior(prior, likelihood, evidence)
which calculates and returns the posterior probability using Bayes' Theorem:
    Posterior = (Prior * Likelihood) / Evidence
Includes comprehensive parameter validation and test verification cases.
"""

def bayes_posterior(prior: float, likelihood: float, evidence: float) -> float:
    """
    Calculates the posterior probability P(H | E) using Bayes' Theorem.

    Formula:
                    P(H) * P(E | H)      Prior * Likelihood
        P(H | E) = ----------------- = ----------------------
                         P(E)                 Evidence

    Args:
        prior (float): P(H) - Prior probability of hypothesis H before observing evidence (0.0 to 1.0).
        likelihood (float): P(E | H) - Probability of observing evidence E given hypothesis H is true (0.0 to 1.0).
        evidence (float): P(E) - Total marginal probability of observing evidence E (0.0 < evidence <= 1.0).

    Returns:
        float: Posterior probability P(H | E) between 0.0 and 1.0.

    Raises:
        ValueError: If any input probability is out of the valid range [0, 1],
                    or if evidence is <= 0.0, or if resulting posterior > 1.0.
    """
    if not (0.0 <= prior <= 1.0):
        raise ValueError(f"Prior probability must be between 0.0 and 1.0. Received: {prior}")
    if not (0.0 <= likelihood <= 1.0):
        raise ValueError(f"Likelihood probability must be between 0.0 and 1.0. Received: {likelihood}")
    if not (0.0 < evidence <= 1.0):
        raise ValueError(f"Evidence probability must be strictly > 0.0 and <= 1.0. Received: {evidence}")

    posterior = (prior * likelihood) / evidence

    if posterior > 1.0000000001:  # Allow for tiny floating point rounding
        raise ValueError(f"Calculated posterior exceeds 1.0 ({posterior}). Please verify input probabilities.")

    return min(posterior, 1.0)


def run_task1():
    print("=" * 68)
    print(" TASK 1: BAYES' THEOREM POSTERIOR PROBABILITY FUNCTION")
    print("=" * 68)
    print("Formula: P(Hypothesis | Evidence) = (Prior * Likelihood) / Evidence")
    print("-" * 68)

    # Test Case 1: Standard Verification Example
    # e.g., Prior = 0.01 (1% disease prevalence), Likelihood = 0.95 (95% sensitivity), Evidence = 0.05
    p1, l1, e1 = 0.01, 0.95, 0.057
    post1 = bayes_posterior(p1, l1, e1)
    print("Test Case 1 (Diagnostic Screening):")
    print(f"  - Prior P(H)        : {p1:.4f} ({p1*100:.1f}%)")
    print(f"  - Likelihood P(E|H) : {l1:.4f} ({l1*100:.1f}%)")
    print(f"  - Evidence P(E)     : {e1:.4f} ({e1*100:.1f}%)")
    print(f"  - Posterior P(H|E)  : {post1:.4f} ({post1*100:.2f}%)")
    print("-" * 68)

    # Test Case 2: Coin Bias Test
    # Fair coin vs Biased coin: Prior = 0.50, Likelihood of 3 Heads = 0.875, Evidence = 0.50
    p2, l2, e2 = 0.50, 0.875, 0.5625
    post2 = bayes_posterior(p2, l2, e2)
    print("Test Case 2 (Coin Bias Verification):")
    print(f"  - Prior P(H)        : {p2:.4f} ({p2*100:.1f}%)")
    print(f"  - Likelihood P(E|H) : {l2:.4f} ({l2*100:.1f}%)")
    print(f"  - Evidence P(E)     : {e2:.4f} ({e2*100:.1f}%)")
    print(f"  - Posterior P(H|E)  : {post2:.4f} ({post2*100:.2f}%)")
    print("=" * 68)

    print("\n[+] bayes_posterior() function verified successfully.")


if __name__ == "__main__":
    run_task1()

