"""
Session 12 - Task 4: Slope and Intercept in Flipkart Price Prediction
File: session-12/task4_flipkart_price_prediction.py

Description:
Provides clear, domain-specific explanations in our own words of what the
'slope' and 'intercept' represent in the context of predicting a product's price
on Flipkart based on its customer rating (Price = m * Rating + c).
"""

def explain_slope_and_intercept():
    explanation = {
        "model_equation": "Predicted Price = (Slope * Product Rating) + Intercept",
        "slope_explanation": (
            "In Flipkart's product price prediction model, the slope represents the change in "
            "a product's estimated price for every 1-star increase in customer rating. "
            "A positive slope indicates that higher-rated products command a premium price because "
            "buyers associate superior quality, better materials, and reputable brand value with high ratings. "
            "Mathematically, it reflects the price sensitivity or premium per unit of user trust."
        ),
        "intercept_explanation": (
            "The intercept represents the baseline starting price of a product when its rating is zero. "
            "In practical e-commerce terms, it reflects the foundational floor price of a newly listed "
            "product on Flipkart before accumulating any customer reviews. "
            "This baseline covers fundamental manufacturing costs, packaging, and minimum platform listing fees "
            "that exist regardless of customer satisfaction."
        )
    }
    return explanation


def run_task4():
    exp = explain_slope_and_intercept()

    print("=" * 72)
    print(" TASK 4: SLOPE & INTERCEPT IN FLIPKART PRODUCT PRICE PREDICTION")
    print("=" * 72)
    print(f"Regression Equation : {exp['model_equation']}")
    print("-" * 72)
    print("1. SLOPE (m):")
    print(exp["slope_explanation"])
    print("-" * 72)
    print("2. INTERCEPT (c):")
    print(exp["intercept_explanation"])
    print("=" * 72)

    # Concrete numerical example for illustration:
    # Say: Price = 350 * Rating + 400
    m_sample, c_sample = 350, 400
    print("\nCONCRETE NUMERICAL ILLUSTRATION (Price = 350 * Rating + 400):")
    print("-" * 72)
    for rating in [3.0, 4.0, 4.5, 5.0]:
        price = m_sample * rating + c_sample
        print(f"- Rating {rating} stars : Price = (350 * {rating}) + 400 = Rs. {price:,.0f}")
    print("=" * 72)


if __name__ == "__main__":
    run_task4()

