"""
Task 2: Function to Calculate Standard Deviation of Exam Scores
File: calculate_standard_deviation.py
"""
import math

def calculate_standard_deviation(scores, is_sample=True):
    """
    Calculates the standard deviation of a list of exam scores,
    rounded to two decimal places.
    
    Parameters:
        scores (list of float or int): List of exam scores.
        is_sample (bool): If True (default), computes sample standard deviation (n-1).
                          If False, computes population standard deviation (N).
                          
    Returns:
        float: Standard deviation rounded to 2 decimal places.
        
    Raises:
        ValueError: If scores list is empty or has fewer than 2 elements for sample standard deviation.
    """
    n = len(scores)
    if n == 0:
        raise ValueError("The scores list cannot be empty.")
    if is_sample and n < 2:
        raise ValueError("Sample standard deviation requires at least 2 scores.")
        
    # 1. Calculate Mean
    mean = sum(scores) / n
    
    # 2. Calculate Sum of Squared Deviations
    sum_squared_deviations = sum((x - mean) ** 2 for x in scores)
    
    # 3. Calculate Variance
    divisor = (n - 1) if is_sample else n
    variance = sum_squared_deviations / divisor
    
    # 4. Standard Deviation is square root of variance
    std_dev = math.sqrt(variance)
    
    return round(std_dev, 2)


if __name__ == "__main__":
    # Test cases with representative exam score datasets
    exam_scores_1 = [85, 90, 78, 92, 88, 76, 95, 89]
    exam_scores_2 = [72, 68, 75, 70, 74, 69, 71]
    
    sample_sd1 = calculate_standard_deviation(exam_scores_1, is_sample=True)
    pop_sd1 = calculate_standard_deviation(exam_scores_1, is_sample=False)
    
    print("=" * 60)
    print(" Exam Scores Standard Deviation Calculator")
    print("=" * 60)
    print(f"Exam Scores Dataset 1       : {exam_scores_1}")
    print(f"Number of Students (n)      : {len(exam_scores_1)}")
    print(f"Mean Score (Average)        : {sum(exam_scores_1) / len(exam_scores_1):.2f}")
    print(f"Sample Standard Deviation   : {sample_sd1}")
    print(f"Population Standard Dev     : {pop_sd1}")
    print("-" * 60)
    print(f"Exam Scores Dataset 2       : {exam_scores_2}")
    print(f"Sample Standard Deviation   : {calculate_standard_deviation(exam_scores_2)}")
    print("=" * 60)
