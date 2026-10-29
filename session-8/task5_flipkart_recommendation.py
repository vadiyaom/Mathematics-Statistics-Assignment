"""
Session 8 - Task 5: Flipkart Recommendation Engine via Conditional Probability
File: session-8/task5_flipkart_recommendation.py

"""

def calculate_conditional_probability(both_count: int, given_item_count: int) -> float:
    """
    Calculates P(B|A) = count(A and B) / count(A).
    """
    if given_item_count <= 0:
        raise ValueError("The count of users who bought item A must be > 0.")
    return both_count / given_item_count


def run_task5():
    # -------------------------------------------------------------
    # 1. E-Commerce Transaction Data (Flipkart Scenario)
    # Total Users Sampled: 1,000 customers
    # -------------------------------------------------------------
    total_customers = 1000

    # Number of customers who bought a Phone (Event A)
    phone_buyers = 400

    # Joint purchases: Users who bought a Phone AND a secondary item
    accessory_joint_purchases = {
        "Screen Protector"  : 340,  # 340 bought Phone AND Screen Protector
        "Phone Case / Cover": 320,  # 320 bought Phone AND Phone Case
        "Wireless Headphones": 260, # 260 bought Phone AND Wireless Headphones
        "Power Bank"        : 120,  # 120 bought Phone AND Power Bank
        "Smart Watch"       : 90,   # 90 bought Phone AND Smart Watch
        "Microwave Oven"    : 10    # 10 bought Phone AND Microwave Oven
    }

    # Baseline site-wide purchases (regardless of buying a phone)
    site_wide_purchases = {
        "Screen Protector"  : 360,
        "Phone Case / Cover": 350,
        "Wireless Headphones": 280,
        "Power Bank"        : 180,
        "Smart Watch"       : 150,
        "Microwave Oven"    : 120
    }

    print("=" * 72)
    print(" TASK 5: CONDITIONAL PROBABILITY IN FLIPKART RECOMMENDATIONS")
    print("=" * 72)
    print(f"Total Platform Customers Sampled           : {total_customers}")
    print(f"Customers Who Bought a Smartphone [Event A]: {phone_buyers} ({phone_buyers/total_customers*100:.1f}%)")
    print("-" * 72)

    # -------------------------------------------------------------
    # 2. Compute Conditional Probabilities & Rank Recommendations
    # -------------------------------------------------------------
    recommendations = []
    for item, both_cnt in accessory_joint_purchases.items():
        cond_prob = calculate_conditional_probability(both_cnt, phone_buyers)
        prior_prob = site_wide_purchases[item] / total_customers
        lift = cond_prob / prior_prob if prior_prob > 0 else 0

        recommendations.append({
            "item": item,
            "both_count": both_cnt,
            "cond_prob": cond_prob,
            "prior_prob": prior_prob,
            "lift": lift
        })

    # Sort items by conditional probability descending
    recommendations.sort(key=lambda x: x["cond_prob"], reverse=True)

    print(f"{'Rank':<5} | {'Recommended Item (B)':<22} | {'Both Count':<10} | {'P(B | Phone)':<14} | {'Lift Factor':<12}")
    print("-" * 72)
    for idx, rec in enumerate(recommendations, 1):
        print(f" #{idx:<3} | {rec['item']:<22} | {rec['both_count']:<10} | {rec['cond_prob']*100:<6.2f}% ({rec['cond_prob']:.2f}) | {rec['lift']:<6.2f}x higher")
    print("=" * 72)

    # -------------------------------------------------------------
    # 3. Focus on the Specific Question: P(Headphones | Phone)
    # -------------------------------------------------------------
    hp_both = accessory_joint_purchases["Wireless Headphones"]
    p_hp_given_phone = hp_both / phone_buyers
    p_hp_general = site_wide_purchases["Wireless Headphones"] / total_customers

    print("\nDEEP DIVE: PROBABILITY OF BUYING HEADPHONES GIVEN PHONE:")
    print("-" * 72)
    print(f"1. Total users who bought a phone, n(Phone)                 = {phone_buyers}")
    print(f"2. Users who bought BOTH Phone & Headphones, n(Both)        = {hp_both}")
    print(f"3. Formula: P(Headphones | Phone) = n(Phone & Headphones) / n(Phone)")
    print(f"4. Calculation: {hp_both} / {phone_buyers}                  = {p_hp_given_phone:.4f} ({p_hp_given_phone * 100:.2f}%)")
    print(f"5. General probability of buying headphones P(Headphones)   = {p_hp_general:.4f} ({p_hp_general * 100:.2f}%)")
    print(f"6. Recommendation Lift: {p_hp_given_phone / p_hp_general:.2f}x increase in likelihood!")
    print("=" * 72)

    # -------------------------------------------------------------
    # 4. Business Explanation
    # -------------------------------------------------------------
    print("\nHOW FLIPKART USES THIS TO IMPROVE RECOMMENDATIONS:")
    print("-" * 72)
    print("A. Personalized Context: A user who purchased a phone is NOT a generic")
    print("   visitor. Recommending headphones yields a 65.0% purchase probability,")
    print("   whereas a generic shopper only has a 28.0% probability.")
    print("B. Dynamic 'Frequently Bought Together': Flipkart automatically surfaces")
    print("   the top 3 highest conditional probability items on the product page:")
    print(f"   1. {recommendations[0]['item']} ({recommendations[0]['cond_prob']*100:.1f}%)")
    print(f"   2. {recommendations[1]['item']} ({recommendations[1]['cond_prob']*100:.1f}%)")
    print(f"   3. {recommendations[2]['item']} ({recommendations[2]['cond_prob']*100:.1f}%)")
    print("C. Avoid Irrelevant Recommendations: While microwaves are popular overall,")
    print("   P(Microwave | Phone) is only 2.5%, so Flipkart suppresses it from")
    print("   the phone accessory drawer.")
    print("=" * 72)


if __name__ == "__main__":
    run_task5()

