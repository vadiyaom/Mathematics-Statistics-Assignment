"""
Session 8: Complete Task Runner
File: session-8/run_all_tasks.py

Executes all python tasks in session-8 sequentially:
1. task1_coin_toss.py              -> Basic probability formula & coin toss
2. task2_dice_simulation.py        -> 100 dice rolls simulation & bar chart
3. task3_spotify_genres.py         -> Recent 20 Spotify tracks genre probability
4. task4_zomato_dessert.py         -> Zomato food and dessert set intersection
5. task5_flipkart_recommendation.py-> Conditional probability in recommendations
"""

from task1_coin_toss import run_task1
from task2_dice_simulation import run_task2
from task3_spotify_genres import run_task3
from task4_zomato_dessert import run_task4
from task5_flipkart_recommendation import run_task5

def main():
    print("#" * 75)
    print("      SESSION 8: PROBABILITY & APPLICATIONS (TASKS 1 TO 5)")
    print("#" * 75)
    
    print("\n>>> RUNNING TASK 1...")
    run_task1()
    
    print("\n>>> RUNNING TASK 2...")
    run_task2()
    
    print("\n>>> RUNNING TASK 3...")
    run_task3()
    
    print("\n>>> RUNNING TASK 4...")
    run_task4()
    
    print("\n>>> RUNNING TASK 5...")
    run_task5()
    
    print("\n" + "#" * 75)
    print("  ALL 5 SESSION 8 TASKS COMPLETED SUCCESSFULLY!")
    print("  Deliverables:")
    print("  - task1_coin_toss.py & Task-1.txt")
    print("  - task2_dice_simulation.py, dice_simulation_plot.png & Task-2.txt")
    print("  - task3_spotify_genres.py & Task-3.txt")
    print("  - task4_zomato_dessert.py & Task-4.txt")
    print("  - task5_flipkart_recommendation.py & Task-5.txt")
    print("#" * 75)

if __name__ == "__main__":
    main()

