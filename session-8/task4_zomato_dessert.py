"""
Session 8 - Task 4: Zomato Food and Dessert Orders Probability
File: session-8/task4_zomato_dessert.py


"""

def prob_ordered_both(food_users: list, dessert_users: list) -> dict:
    """
    Calculates the probability that a randomly chosen unique user ordered
    both food and dessert (Intersection over Union).

    Args:
        food_users (list): Collection of user IDs who ordered food.
        dessert_users (list): Collection of user IDs who ordered dessert.

    Returns:
        dict: Detailed breakdown containing set counts and computed probability.
    """
    # Convert to sets to eliminate duplicates and allow set operations
    set_food = set(food_users)
    set_dessert = set(dessert_users)

    # 1. Total unique users who placed an order (Union: Food ∪ Dessert)
    union_users = set_food.union(set_dessert)
    total_unique_count = len(union_users)

    if total_unique_count == 0:
        raise ValueError("Both user lists are empty; total unique users cannot be zero.")

    # 2. Users who ordered BOTH food and dessert (Intersection: Food ∩ Dessert)
    intersection_users = set_food.intersection(set_dessert)
    both_count = len(intersection_users)

    # 3. Probability: Intersection / Total Unique Users
    probability = both_count / total_unique_count

    # Additional segment breakdowns
    food_only = set_food - set_dessert
    dessert_only = set_dessert - set_food

    return {
        "food_users_count": len(set_food),
        "dessert_users_count": len(set_dessert),
        "both_users": sorted(list(intersection_users)),
        "both_count": both_count,
        "total_unique_users": sorted(list(union_users)),
        "total_unique_count": total_unique_count,
        "probability": probability,
        "percentage": probability * 100.0,
        "food_only_count": len(food_only),
        "dessert_only_count": len(dessert_only)
    }


def run_task4():
    # -------------------------------------------------------------
    # 1. Sample Zomato Customer Dataset
    # -------------------------------------------------------------
    food_orders = [
        "user_101", "user_102", "user_103", "user_104", 
        "user_105", "user_106", "user_107", "user_108"
    ]
    
    dessert_orders = [
        "user_103", "user_104", "user_107", "user_109", "user_110"
    ]

    result = prob_ordered_both(food_orders, dessert_orders)

    print("=" * 70)
    print(" TASK 4: ZOMATO FOOD & DESSERT SET PROBABILITY")
    print("=" * 70)
    print(f"Users who ordered Food (A)             : {len(food_orders)} users")
    print(f"Users who ordered Dessert (B)          : {len(dessert_orders)} users")
    print("-" * 70)
    print(f"Users who ordered BOTH (A INTERSECT B) : {result['both_users']}")
    print(f"Count of users who ordered BOTH        : {result['both_count']}")
    print("-" * 70)
    print(f"Total Unique Users (A UNION B)         : {result['total_unique_users']}")
    print(f"Count of Total Unique Users            : {result['total_unique_count']}")
    print("-" * 70)
    print(f"Formula                                : P(Both) = |Food INTERSECT Dessert| / |Food UNION Dessert|")
    print(f"Calculation                            : {result['both_count']} / {result['total_unique_count']}")
    print(f"Probability of ordering both (Decimal) : {result['probability']:.4f}")
    print(f"Probability of ordering both (Percent) : {result['percentage']:.2f}%")
    print("=" * 70)

    # Breakdown of entire user universe
    print("\nCOMPLETE SEGMENTATION BREAKDOWN:")
    print("-" * 70)
    print(f"1. Food Only Users    : {result['food_only_count']} users ({result['food_only_count']/result['total_unique_count']*100:.1f}%)")
    print(f"2. Dessert Only Users : {result['dessert_only_count']} users ({result['dessert_only_count']/result['total_unique_count']*100:.1f}%)")
    print(f"3. BOTH Food & Dessert: {result['both_count']} users ({result['probability']*100:.1f}%)")
    print("-" * 70)
    print(f"   Sum of Segments    : {result['total_unique_count']} users (100.0%)")
    print("=" * 70)


if __name__ == "__main__":
    run_task4()
