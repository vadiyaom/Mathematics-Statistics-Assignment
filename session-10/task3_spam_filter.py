"""
Session 10 - Task 3: Naive Bayes Email Spam Detection Simulation
File: session-10/task3_spam_filter.py

Description:
Simulates a basic Naive Bayes spam filter on a dataset of 20 email subjects.
Calculates:
1. Prior probabilities: P(Spam) and P(Ham)
2. Likelihoods: P('free' | Spam) and P('free' | Ham)
3. Total Evidence: P('free')
4. Posterior Probability: P(Spam | 'free') using Bayes' Theorem
"""

import re
from task1_bayes_posterior import bayes_posterior

def contains_word(text: str, word: str) -> bool:
    """Case-insensitive exact word boundary matcher."""
    pattern = r'\b' + re.escape(word.lower()) + r'\b'
    return bool(re.search(pattern, text.lower()))


def run_task3():
    # -------------------------------------------------------------
    # 1. Dataset: 20 Email Subjects (Labeled as Spam or Ham)
    # -------------------------------------------------------------
    emails = [
        # Spam Emails (8 emails)
        ("Win a free luxury cruise trip to Bahamas today!", True),
        ("Claim your free gift card worth Rs. 5000", True),
        ("Urgent: Free bitcoin bonus deposited in your wallet", True),
        ("Exclusive free trial access for VIP members", True),
        ("Get your free credit score report instantly", True),
        ("Free entry to the international lucky draw", True),
        ("Congratulations! You won 1,000,000 cash prize", True),      # Spam without 'free'
        ("Fast personal loans approved with zero collateral", True),  # Spam without 'free'

        # Ham / Non-Spam Emails (12 emails)
        ("Are you free for a quick sync call tomorrow afternoon?", False), # Ham with 'free'
        ("Feel free to review the attached project proposal", False),      # Ham with 'free'
        ("Quarterly financial budget and expense spreadsheet", False),
        ("Doctor appointment confirmation for Thursday at 4 PM", False),
        ("Notes and action items from the team retrospective", False),
        ("Flight ticket booking confirmation and boarding pass", False),
        ("Weekly Python data science assignment submission", False),
        ("Invoice for September cloud hosting services", False),
        ("Family dinner plans this coming Saturday evening", False),
        ("Gym membership monthly subscription renewal receipt", False),
        ("Campus interview schedule and candidate briefing", False),
        ("Software engineering sprint retrospective notes", False)
    ]

    total_emails = len(emails)
    target_keyword = "free"

    # -------------------------------------------------------------
    # 2. Extract Counts & Statistics from the 20 Emails
    # -------------------------------------------------------------
    spam_emails = [subj for subj, is_spam in emails if is_spam]
    ham_emails = [subj for subj, is_spam in emails if not is_spam]

    n_spam = len(spam_emails)
    n_ham = len(ham_emails)

    spam_with_free = sum(1 for s in spam_emails if contains_word(s, target_keyword))
    ham_with_free = sum(1 for s in ham_emails if contains_word(s, target_keyword))
    total_with_free = spam_with_free + ham_with_free

    # -------------------------------------------------------------
    # 3. Calculate Prior, Likelihoods, and Marginal Evidence
    # -------------------------------------------------------------
    # Priors
    prior_spam = n_spam / total_emails           # 8 / 20 = 0.40
    prior_ham = n_ham / total_emails             # 12 / 20 = 0.60

    # Likelihoods
    likelihood_free_given_spam = spam_with_free / n_spam   # 6 / 8 = 0.75
    likelihood_free_given_ham = ham_with_free / n_ham     # 2 / 12 = 0.1667

    # Evidence: P('free')
    evidence_free = total_with_free / total_emails        # 8 / 20 = 0.40

    # -------------------------------------------------------------
    # 4. Compute Posterior Probability P(Spam | 'free')
    # -------------------------------------------------------------
    posterior_spam_given_free = bayes_posterior(
        prior=prior_spam,
        likelihood=likelihood_free_given_spam,
        evidence=evidence_free
    )

    posterior_ham_given_free = 1.0 - posterior_spam_given_free

    # -------------------------------------------------------------
    # 5. Formatted Output
    # -------------------------------------------------------------
    print("=" * 72)
    print(" TASK 3: NAIVE BAYES SPAM DETECTION FILTER (20 EMAILS)")
    print("=" * 72)
    print(f"Total Emails in Training Corpus         : {total_emails}")
    print(f"Spam Emails Count                       : {n_spam} ({prior_spam*100:.1f}%)")
    print(f"Ham (Non-Spam) Emails Count             : {n_ham} ({prior_ham*100:.1f}%)")
    print("-" * 72)
    print(f"Spam emails containing '{target_keyword}'            : {spam_with_free} / {n_spam}")
    print(f"Ham emails containing '{target_keyword}'             : {ham_with_free} / {n_ham}")
    print(f"Total emails containing '{target_keyword}'           : {total_with_free} / {total_emails}")
    print("-" * 72)
    print("BAYES' THEOREM PARAMETERS:")
    print(f"1. Prior P(Spam)                        : {prior_spam:.4f} ({prior_spam*100:.1f}%)")
    print(f"2. Likelihood P('{target_keyword}' | Spam)           : {likelihood_free_given_spam:.4f} ({likelihood_free_given_spam*100:.1f}%)")
    print(f"3. Likelihood P('{target_keyword}' | Ham)            : {likelihood_free_given_ham:.4f} ({likelihood_free_given_ham*100:.2f}%)")
    print(f"4. Evidence P('{target_keyword}')                    : {evidence_free:.4f} ({evidence_free*100:.1f}%)")
    print("-" * 72)
    print("POSTERIOR PROBABILITY CALCULATION:")
    print(f"  P(Spam | '{target_keyword}') = [P(Spam) * P('{target_keyword}' | Spam)] / P('{target_keyword}')")
    print(f"                     = [{prior_spam:.2f} * {likelihood_free_given_spam:.2f}] / {evidence_free:.2f}")
    print(f"                     = {prior_spam * likelihood_free_given_spam:.4f} / {evidence_free:.4f}")
    print(f"  Posterior Probability: {posterior_spam_given_free:.4f} ({posterior_spam_given_free * 100:.2f}%)")
    print(f"  Complement P(Ham | '{target_keyword}'): {posterior_ham_given_free:.4f} ({posterior_ham_given_free * 100:.2f}%)")
    print("=" * 72)

    # -------------------------------------------------------------
    # 6. Classification Decision Rule
    # -------------------------------------------------------------
    threshold = 0.50
    classification = "SPAM (Move to Junk Folder)" if posterior_spam_given_free >= threshold else "HAM (Keep in Inbox)"
    print("\nSPAM FILTER CLASSIFIER DECISION:")
    print("-" * 72)
    print(f"Decision Threshold : {threshold * 100:.1f}%")
    print(f"Predicted Class    : {classification}")
    print(f"Confidence         : {posterior_spam_given_free * 100:.2f}%")
    print("=" * 72)


if __name__ == "__main__":
    run_task3()

