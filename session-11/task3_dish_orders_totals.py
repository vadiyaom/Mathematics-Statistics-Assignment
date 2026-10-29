"""
Session 11 - Task 3: Dish Orders Totals Across Days (Matrix Column Sums)
File: session-11/task3_dish_orders_totals.py

Description:
Given a 3x4 matrix representing order counts for 4 different dishes across
3 consecutive days (rows = days, columns = dishes):
1. Calculates total orders for each dish (column sum / axis 0).
2. Displays the matrix with headers and summary totals.
"""

import numpy as np

def calculate_dish_totals(matrix: list) -> list:
    """
    Calculates the sum of orders for each dish (column sum) across all days.

    Args:
        matrix (list of list): 2D matrix where rows=days, columns=dishes.

    Returns:
        list: Total orders for each dish.
    """
    num_days = len(matrix)
    num_dishes = len(matrix[0])

    dish_totals = []
    for col in range(num_dishes):
        col_sum = sum(matrix[row][col] for row in range(num_days))
        dish_totals.append(col_sum)

    return dish_totals


def run_task3():
    # -------------------------------------------------------------
    # 1. Dataset: 3 Days x 4 Dishes Matrix
    # Rows: Day 1, Day 2, Day 3
    # Columns: Dish 1, Dish 2, Dish 3, Dish 4
    # -------------------------------------------------------------
    days = ["Day 1 (Friday)", "Day 2 (Saturday)", "Day 3 (Sunday)"]
    dishes = ["Dish 1 (Pizza)", "Dish 2 (Burger)", "Dish 3 (Pasta)", "Dish 4 (Tacos)"]

    # 3x4 Matrix of Orders
    orders_matrix = [
        [25, 40, 15, 30],  # Day 1
        [30, 45, 20, 35],  # Day 2
        [20, 35, 25, 40]   # Day 3
    ]

    # Calculate dish totals (column sums) using pure Python
    dish_totals_py = calculate_dish_totals(orders_matrix)

    # Convert to NumPy array for matrix axis operations
    np_orders = np.array(orders_matrix)
    dish_totals_np = np.sum(np_orders, axis=0)  # Sum down columns (axis=0)
    day_totals_np = np.sum(np_orders, axis=1)   # Sum across rows (axis=1)

    print("=" * 72)
    print(" TASK 3: RESTAURANT DISH ORDERS MATRIX (3 DAYS x 4 DISHES)")
    print("=" * 72)
    print(f"{'Day (Row)':<18} | {'Pizza':<10} | {'Burger':<10} | {'Pasta':<10} | {'Tacos':<10} | {'Daily Total':<11}")
    print("-" * 72)
    for day_name, row, day_tot in zip(days, orders_matrix, day_totals_np):
        print(f"{day_name:<18} | {row[0]:<10} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {day_tot:<11}")
    print("=" * 72)

    # -------------------------------------------------------------
    # 2. Total Orders for Each Dish
    # -------------------------------------------------------------
    print(f"{'TOTAL ORDERS':<18} | {dish_totals_np[0]:<10} | {dish_totals_np[1]:<10} | {dish_totals_np[2]:<10} | {dish_totals_np[3]:<10} | {np.sum(np_orders):<11}")
    print("=" * 72)

    print("\nDETAILED TOTAL ORDERS PER DISH:")
    print("-" * 72)
    for i, (dish_name, total) in enumerate(zip(dishes, dish_totals_np), 1):
        daily_breakdown = f"({orders_matrix[0][i-1]} + {orders_matrix[1][i-1]} + {orders_matrix[2][i-1]})"
        print(f"{dish_name:<20} : {total} total orders  {daily_breakdown}")

    print("-" * 72)
    print(f"Total Restaurant Orders Across All Dishes: {int(np.sum(np_orders))} orders")
    print("=" * 72)


if __name__ == "__main__":
    run_task3()

