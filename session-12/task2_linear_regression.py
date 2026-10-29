"""
Session 12 - Task 2: Linear Regression Prediction Function
File: session-12/task2_linear_regression.py

Description:
Defines the prediction function:
    linear_regression_predict(x, m, c)
which implements the univariate linear regression equation:
    y = m * x + c
Supports single numerical values as well as lists and NumPy arrays.
"""

from typing import Union, List
import numpy as np

def linear_regression_predict(
    x: Union[float, int, List[Union[float, int]], np.ndarray],
    m: float,
    c: float
) -> Union[float, np.ndarray]:
    """
    Predicts the output value(s) y using the linear regression model: y = mx + c.

    Args:
        x (float, int, list, or np.ndarray): Input feature value or collection of values.
        m (float): Slope of the regression line (rate of change of y with respect to x).
        c (float): Y-intercept of the regression line (expected value of y when x = 0).

    Returns:
        float or np.ndarray: Predicted target value(s) y.
    """
    if isinstance(x, (list, tuple)):
        x_arr = np.array(x, dtype=float)
        return m * x_arr + c
    elif isinstance(x, np.ndarray):
        return m * x + c
    else:
        return float(m * x + c)


def run_task2():
    print("=" * 68)
    print(" TASK 2: LINEAR REGRESSION PREDICTION FUNCTION (y = mx + c)")
    print("=" * 68)
    print("Function Signature: linear_regression_predict(x, m, c)")
    print("-" * 68)

    # Test Case 1: Scalar prediction
    # Given: x = 10, m = 2.5, c = 5.0 ==> y = 2.5 * 10 + 5.0 = 30.0
    x_test1 = 10
    m_test1 = 2.5
    c_test1 = 5.0
    y_pred1 = linear_regression_predict(x_test1, m_test1, c_test1)

    print("Test Case 1 (Scalar Value):")
    print(f"  Input (x)     : {x_test1}")
    print(f"  Slope (m)     : {m_test1}")
    print(f"  Intercept (c) : {c_test1}")
    print(f"  Equation      : y = {m_test1} * {x_test1} + {c_test1}")
    print(f"  Predicted (y) : {y_pred1}")
    print("-" * 68)

    # Test Case 2: Vector / List prediction
    x_test2 = [1, 2, 3, 4]
    m_test2 = 3.0
    c_test2 = 1.0
    y_pred2 = linear_regression_predict(x_test2, m_test2, c_test2)

    print("Test Case 2 (Multiple Inputs):")
    print(f"  Inputs (x)    : {x_test2}")
    print(f"  Equation      : y = {m_test2}x + {c_test2}")
    print(f"  Predicted (y) : {[float(v) for v in y_pred2]}")
    print("=" * 68)
    print("\n[+] linear_regression_predict() implemented and verified successfully.")


if __name__ == "__main__":
    run_task2()
