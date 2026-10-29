"""
Session 10 - Task 4: Instagram Bot Account Detection via Bayes' Theorem
File: session-10/task4_instagram_bayes.py

Description:
Solves a real-world Bayes' Theorem problem generated via ChatGPT / Copilot:
Detecting whether a newly registered Instagram account is a 'Bot Account'
given that the account has a 'Default Profile Picture and Zero Posts'.
"""

from task1_bayes_posterior import bayes_posterior

def run_task4():
    # -------------------------------------------------------------
    # PROMPT SUBMITTED TO CHATGPT / COPILOT:
    # -------------------------------------------------------------
    chatgpt_prompt = """
    "Generate a realistic real-world Bayes' Theorem word problem related to Instagram.
    Specifically, set up a scenario where Instagram's Trust & Safety engineering team
    uses Bayes' Theorem to detect Bot/Spam accounts based on the profile feature:
    'Account has a Default Profile Picture and Zero Posts'.
    Provide realistic prior probabilities, likelihoods, numerical values, and explain
    the step-by-step Bayes' theorem solution with Python code."
    """

    print("=" * 72)
    print(" TASK 4: INSTAGRAM BOT ACCOUNT DETECTION (CHATGPT / COPILOT SCENARIO)")
    print("=" * 72)
    print("PROMPT SUBMITTED TO CHATGPT / COPILOT:")
    print(chatgpt_prompt.strip())
    print("-" * 72)

    # -------------------------------------------------------------
    # 1. Prior Probabilities
    # -------------------------------------------------------------
    # P(Bot): Prior probability that any newly registered account is a bot (15%)
    prior_bot = 0.15

    # P(Human): Prior probability that the account belongs to a legitimate human (85%)
    prior_human = 1.0 - prior_bot  # 0.85

    # -------------------------------------------------------------
    # 2. Likelihood Probabilities
    # Feature E = "Default Profile Picture & Zero Posts"
    # -------------------------------------------------------------
    # P(E | Bot): 75% of automated bots have a default avatar and 0 posts
    likelihood_feature_given_bot = 0.75

    # P(E | Human): Only 5% of legitimate humans have a default avatar and 0 posts
    likelihood_feature_given_human = 0.05

    # -------------------------------------------------------------
    # 3. Marginal Evidence via Law of Total Probability
    # P(E) = P(Bot) * P(E | Bot) + P(Human) * P(E | Human)
    # -------------------------------------------------------------
    prob_bot_and_feature = prior_bot * likelihood_feature_given_bot       # 0.15 * 0.75 = 0.1125
    prob_human_and_feature = prior_human * likelihood_feature_given_human # 0.85 * 0.05 = 0.0425

    evidence_feature = prob_bot_and_feature + prob_human_and_feature      # 0.1125 + 0.0425 = 0.1550

    # -------------------------------------------------------------
    # 4. Posterior Probability via Bayes' Theorem
    # P(Bot | E) = [P(Bot) * P(E | Bot)] / P(E)
    # -------------------------------------------------------------
    posterior_bot = bayes_posterior(
        prior=prior_bot,
        likelihood=likelihood_feature_given_bot,
        evidence=evidence_feature
    )

    posterior_human = 1.0 - posterior_bot

    # -------------------------------------------------------------
    # 5. Output & Analysis
    # -------------------------------------------------------------
    print("MODEL PARAMETERS:")
    print(f"1. Prior P(Bot)                           : {prior_bot:.4f} ({prior_bot*100:.1f}%)")
    print(f"2. Prior P(Human)                         : {prior_human:.4f} ({prior_human*100:.1f}%)")
    print(f"3. Likelihood P(Default & 0 Posts | Bot)  : {likelihood_feature_given_bot:.4f} ({likelihood_feature_given_bot*100:.1f}%)")
    print(f"4. Likelihood P(Default & 0 Posts | Human): {likelihood_feature_given_human:.4f} ({likelihood_feature_given_human*100:.1f}%)")
    print("-" * 72)
    print("LAW OF TOTAL PROBABILITY:")
    print(f"  P(Feature) = ({prior_bot:.2f} * {likelihood_feature_given_bot:.2f}) + ({prior_human:.2f} * {likelihood_feature_given_human:.2f})")
    print(f"             = {prob_bot_and_feature:.4f} + {prob_human_and_feature:.4f}")
    print(f"  Total Marginal Evidence P(Feature)      : {evidence_feature:.4f} ({evidence_feature*100:.2f}%)")
    print("-" * 72)
    print("BAYES' THEOREM POSTERIOR:")
    print(f"  P(Bot | Default & 0 Posts) = [{prior_bot:.2f} * {likelihood_feature_given_bot:.2f}] / {evidence_feature:.4f}")
    print(f"                             = {prob_bot_and_feature:.4f} / {evidence_feature:.4f}")
    print(f"  Posterior Probability (Decimal)         : {posterior_bot:.5f}")
    print(f"  Posterior Probability (Percentage)      : {posterior_bot * 100:.2f}%")
    print(f"  Posterior P(Human | Feature)            : {posterior_human * 100:.2f}%")
    print("=" * 72)

    # -------------------------------------------------------------
    # 6. Automated Trust & Safety Policy Action
    # -------------------------------------------------------------
    action_threshold = 0.70
    action = "TRIGGER CAPTCHA & PHONE VERIFICATION" if posterior_bot >= action_threshold else "ALLOW NORMAL BROWSING"

    print("\nINSTAGRAM TRUST & SAFETY SYSTEM ACTION:")
    print("-" * 72)
    print(f"Bot Probability Threshold : {action_threshold*100:.1f}%")
    print(f"Calculated Probability    : {posterior_bot*100:.2f}%")
    print(f"Automated Action          : {action}")
    print("Explanation: The 'Default Picture + 0 Posts' signal elevated the bot probability")
    print(f"             from a 15.0% baseline to {posterior_bot*100:.1f}%, exceeding the 70% risk threshold.")
    print("=" * 72)


if __name__ == "__main__":
    run_task4()

