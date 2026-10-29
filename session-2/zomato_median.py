"""
Task 2: Find Median Delivery Time for Zomato Orders
File: zomato_median.py
"""
import statistics

def find_median(data):
    """
    Finds the median value of a numerical dataset.
    
    Algorithm:
    1. Sort the list in ascending order.
    2. If length (n) is odd:
          median = sorted_data[n // 2]
       If length (n) is even:
          median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    """
    if not data:
        raise ValueError("Data list cannot be empty.")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 1:
        # Odd number of observations: middle element
        median_value = sorted_data[mid]
    else:
        # Even number of observations: average of the two middle elements
        median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        
    return median_value, sorted_data


if __name__ == "__main__":
    # Given array of delivery times (in minutes) for Zomato orders
    delivery_times = [30, 25, 40, 35, 30, 45, 30]
    
    median_val, sorted_times = find_median(delivery_times)
    stats_median = statistics.median(delivery_times)
    
    print("=" * 55)
    print(" Zomato Order Delivery Time - Median Calculation")
    print("=" * 55)
    print(f"Original Delivery Times (mins) : {delivery_times}")
    print(f"Sorted Delivery Times (mins)   : {sorted_times}")
    print(f"Total Observations (n)         : {len(delivery_times)} (Odd)")
    print(f"Middle Position Index          : index {len(delivery_times) // 2} (4th element)")
    print(f"Calculated Median Delivery Time: {median_val} minutes")
    print(f"Verification via statistics pkg: {stats_median} minutes")
    print("=" * 55)
