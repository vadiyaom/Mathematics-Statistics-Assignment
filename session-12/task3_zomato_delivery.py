"""
Session 12 - Task 3: Zomato Delivery Time Prediction
File: session-12/task3_zomato_delivery.py

Description:
Uses the linear regression function from Task 2 to predict Zomato delivery
times based on delivery distance:
    y = 4x + 10
where:
    x = Distance in kilometers (km)
    m = 4 (Each km adds 4 minutes transit time)
    c = 10 (Base 10 minutes preparation and dispatch time)
    y = Predicted delivery time in minutes
Calculates predictions for distances: 2 km, 5 km, and 8 km.
"""

from task2_linear_regression import linear_regression_predict

def run_task3():
    print("=" * 70)
    print(" TASK 3: ZOMATO DELIVERY TIME PREDICTION (y = 4x + 10)")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1. Model Parameters
    # -------------------------------------------------------------
    # Equation: y = 4x + 10
    slope_m = 4.0        # Rate: 4 minutes per kilometer
    intercept_c = 10.0   # Base: 10 minutes kitchen prep & rider assignment

    # Distances to evaluate
    distances_km = [2, 5, 8]

    print("MODEL CONFIGURATION:")
    print(f"- Independent Variable (x) : Distance from restaurant (in km)")
    print(f"- Dependent Variable (y)   : Predicted delivery time (in minutes)")
    print(f"- Slope (m)                : 4.0 mins/km (Transit speed factor)")
    print(f"- Y-Intercept (c)          : 10.0 mins (Base kitchen cooking & dispatch)")
    print(f"- Regression Formula       : y = 4x + 10")
    print("-" * 70)

    # -------------------------------------------------------------
    # 2. Predict Delivery Time for Each Distance
    # -------------------------------------------------------------
    print(f"{'Distance (km)':<15} | {'Calculation (y = 4x + 10)':<28} | {'Predicted Time (mins)':<22}")
    print("-" * 70)

    for dist in distances_km:
        pred_time = linear_regression_predict(x=dist, m=slope_m, c=intercept_c)
        calc_str = f"4 * ({dist}) + 10 = {slope_m * dist:.0f} + 10"
        print(f"{dist:<4} km         | {calc_str:<28} | {pred_time:<4.0f} minutes")

    print("=" * 70)

    # -------------------------------------------------------------
    # 3. Practical Domain Insights
    # -------------------------------------------------------------
    print("\nINTERPRETATION OF RESULTS:")
    print("-" * 70)
    print("1. At 2 km : Predicted time = 18 minutes (Quick local neighbourhood order).")
    print("2. At 5 km : Predicted time = 30 minutes (Standard medium-range order).")
    print("3. At 8 km : Predicted time = 42 minutes (Cross-town extended distance order).")
    print("4. Rate of Increase: Every additional 1 km consistently adds 4 minutes,")
    print("   and every order requires a non-negotiable 10-minute base prep time.")
    print("=" * 70)

if __name__ == "__main__":
    run_task3()

