"""
Session 7: Complete Task Runner
File: session-7/run_all_tasks.py

Executes all python tasks in session-7 sequentially and generates all plots:
1. task1_instagram.py       -> instagram_scatter_plot.png
2. task2_zomato_swiggy.py   -> zomato_swiggy_scatter_plot.png
3. task4_spotify_marks.py   -> spotify_vs_marks_scatter.png
"""

import sys
import os

from task1_instagram import run_task1
from task2_zomato_swiggy import run_task2
from task4_spotify_marks import run_task4

def main():
    print("#" * 75)
    print("  SESSION 7: CORRELATION ANALYSIS & SCATTER PLOTS (ALL TASKS)")
    print("#" * 75)
    
    print("\n>>> RUNNING TASK 1...")
    run_task1()
    
    print("\n>>> RUNNING TASK 2...")
    run_task2()
    
    print("\n>>> RUNNING TASK 4...")
    run_task4()
    
    print("\n" + "#" * 75)
    print("  ALL SESSION 7 TASKS COMPLETED SUCCESSFULLY!")
    print("  Artifacts Generated:")
    print("  - instagram_scatter_plot.png")
    print("  - zomato_swiggy_scatter_plot.png")
    print("  - spotify_vs_marks_scatter.png")
    print("  - Task-1.txt, Task-2.txt, Task-3.txt, Task-4.txt")
    print("#" * 75)

if __name__ == "__main__":
    main()

