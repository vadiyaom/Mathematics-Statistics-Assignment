import numpy as np

# 3 Friends (Rows: Rohan, Priya, Amit) x 3 Dishes (Cols: Biryani, Butter Chicken, Garlic Naan)
ratings = [
    [5, 4, 3],  # Friend 1 (Rohan)
    [4, 5, 2],  # Friend 2 (Priya)
    [3, 4, 5]   # Friend 3 (Amit)
]

ratings_matrix = np.array(ratings)

print("3x3 Swiggy Ratings Matrix:")
print(ratings_matrix)

# Display ratings for the SECOND food item (Butter Chicken, Column Index 1)
friends = ["Friend 1 (Rohan)", "Friend 2 (Priya)", "Friend 3 (Amit)"]
second_item_index = 1  # 0-indexed: Column 1 is the 2nd item

print("\nRatings Given to the Second Food Item (Butter Chicken):")
for i, friend in enumerate(friends):
    print(f"- {friend}: {ratings_matrix[i, second_item_index]} / 5 stars")

second_item_ratings = ratings_matrix[:, second_item_index]
print(f"\nExtracted Column Vector: {list(second_item_ratings)}")
print(f"Average Rating for Second Item: {np.mean(second_item_ratings):.2f} / 5.0")