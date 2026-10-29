"""
Session 10 - Task 2: Swiggy Premium Restaurant Discount - Bayes' Theorem
File: session-10/task2_swiggy_bayes.py

Description:
Solves the Swiggy restaurant classification problem:
- 10% of restaurants are 'premium', 90% are 'regular'.
- 80% of premium restaurants offer a discount.
- 20% of regular restaurants offer a discount.
Given that a discount is observed, calculates the posterior probability
that the restaurant is 'premium' using Bayes' Theorem.
"""

from task1_bayes_posterior import bayes_posterior

def run_task2():
    print("=" * 70)
    print(" TASK 2: SWIGGY PREMIUM RESTAURANT PROBABILITY GIVEN A DISCOUNT")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1. Define Prior Probabilities
    # -------------------------------------------------------------
    # P(Premium): Prior probability that any random restaurant is premium (10%)
    prior_premium = 0.10

    # P(Regular): Prior probability that a restaurant is regular (non-premium) (90%)
    prior_regular = 1.0 - prior_premium  # 0.90

    # -------------------------------------------------------------
    # 2. Define Likelihoods
    # -------------------------------------------------------------
    # P(Discount | Premium): Probability a premium restaurant offers a discount (80%)
    likelihood_discount_given_premium = 0.80

    # P(Discount | Regular): Probability a regular restaurant offers a discount (20%)
    likelihood_discount_given_regular = 0.20

    # -------------------------------------------------------------
    # 3. Calculate Total Marginal Evidence via Law of Total Probability
    # -------------------------------------------------------------
    # P(Discount) = P(Premium) * P(Discount|Premium) + P(Regular) * P(Discount|Regular)
    prob_premium_and_discount = prior_premium * likelihood_discount_given_premium  # 0.10 * 0.80 = 0.08
    prob_regular_and_discount = prior_regular * likelihood_discount_given_regular  # 0.90 * 0.20 = 0.18

    evidence_discount = prob_premium_and_discount + prob_regular_and_discount     # 0.08 + 0.18 = 0.26

    # -------------------------------------------------------------
    # 4. Calculate Posterior Probability using Bayes' Theorem
    # -------------------------------------------------------------
    # P(Premium | Discount) = (P(Premium) * P(Discount | Premium)) / P(Discount)
    posterior_premium = bayes_posterior(
        prior=prior_premium,
        likelihood=likelihood_discount_given_premium,
        evidence=evidence_discount
    )

    posterior_regular = 1.0 - posterior_premium

    # -------------------------------------------------------------
    # 5. Formatted Output & Analysis
    # -------------------------------------------------------------
    print("PROBLEM PARAMETERS & FORMULAS:")
    print("-" * 70)
    print(f"1. Prior P(Premium)                    : {prior_premium:.2f} (10.0%)")
    print(f"2. Prior P(Regular)                    : {prior_regular:.2f} (90.0%)")
    print(f"3. Likelihood P(Discount | Premium)    : {likelihood_discount_given_premium:.2f} (80.0%)")
    print(f"4. Likelihood P(Discount | Regular)    : {likelihood_discount_given_regular:.2f} (20.0%)")
    print("-" * 70)
    print("LAW OF TOTAL PROBABILITY (EVIDENCE):")
    print("  P(Discount) = [P(Prem) * P(Disc|Prem)] + [P(Reg) * P(Disc|Reg)]")
    print(f"              = [{prior_premium:.2f} * {likelihood_discount_given_premium:.2f}] + [{prior_regular:.2f} * {likelihood_discount_given_regular:.2f}]")
    print(f"              = {prob_premium_and_discount:.4f} + {prob_regular_and_discount:.4f}")
    print(f"  Total Evidence P(Discount)           : {evidence_discount:.4f} (26.0%)")
    print("-" * 70)
    print("BAYES' THEOREM POSTERIOR CALCULATION:")
    print("  P(Premium | Discount) = [Prior * Likelihood] / Evidence")
    print(f"                        = [{prior_premium:.2f} * {likelihood_discount_given_premium:.2f}] / {evidence_discount:.2f}")
    print(f"                        = {prob_premium_and_discount:.4f} / {evidence_discount:.4f}")
    print(f"                        = 4 / 13")
    print(f"  Posterior Probability (Decimal)      : {posterior_premium:.5f}")
    print(f"  Posterior Probability (Percentage)   : {posterior_premium * 100:.2f}%")
    print("=" * 70)

    print("\nINTERPRETATION & BASE-RATE INSIGHT:")
    print("=" * 70)
    print(f"- Prior belief before seeing a discount   : 10.00%")
    print(f"- Posterior belief after seeing a discount : {posterior_premium * 100:.2f}% (over 3x increase!)")
    print(f"- Why is it not higher (e.g. 80%)?")
    print("  Because regular restaurants make up 90% of the platform. In a sample")
    print("  of 100 restaurants:")
    print("    * 10 are Premium  -> 8 offer discounts  (10 * 80%)")
    print("    * 90 are Regular  -> 18 offer discounts (90 * 20%)")
    print("  Out of the 26 total discounted restaurants, only 8 are premium:")
    print(f"    8 / 26 = 4 / 13 = {posterior_premium*100:.2f}%.")
    print("=" * 70)

if __name__ == "__main__":
    run_task2()

