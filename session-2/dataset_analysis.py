"""
Task 5: Analyze Real-World Dataset (IPL Player Runs from Kaggle) using Pandas
File: dataset_analysis.py
"""
import pandas as pd
import os

def analyze_dataset():
    # Resolve CSV path relative to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "ipl_player_runs.csv")
    
    print("=" * 65)
    print(" Real-World Dataset Analysis: IPL Batting Records (Kaggle)")
    print("=" * 65)
    
    # 1. Load dataset using pandas
    df = pd.read_csv(csv_file)
    print(f"Dataset successfully loaded from: {os.path.basename(csv_file)}")
    print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
    print("\nDataset Preview (Top 5 rows):")
    print(df[['player_name', 'team', 'matches', 'runs', 'highest_score', 'strike_rate']].head().to_string(index=False))
    
    # 2. Select numeric column for analysis
    target_column = "runs"
    runs_series = df[target_column]
    
    # 3. Calculate Mean, Median, and Mode
    mean_val = runs_series.mean()
    median_val = runs_series.median()
    mode_series = runs_series.mode()
    mode_val = mode_series.tolist()
    
    # 4. Display statistical metrics
    print("\n" + "=" * 65)
    print(f" Statistical Summary for Numeric Column: '{target_column}'")
    print("=" * 65)
    print(f"Total Players Analyzed (n) : {runs_series.count()}")
    print(f"Mean (Average Runs)        : {mean_val:.2f}")
    print(f"Median (Middle Runs)       : {median_val:.2f}")
    print(f"Mode (Most Frequent Runs)  : {mode_val} (All values appear with equal frequency)")
    print(f"Minimum Runs               : {runs_series.min()} ({df.loc[runs_series.idxmin(), 'player_name']})")
    print(f"Maximum Runs               : {runs_series.max()} ({df.loc[runs_series.idxmax(), 'player_name']})")
    print(f"Standard Deviation         : {runs_series.std():.2f}")
    print("=" * 65)

    # Secondary column analysis for additional depth: Matches played
    matches_col = "matches"
    print(f"\n Bonus Analysis on Discrete Numeric Column: '{matches_col}'")
    print(f"Mean Matches Played        : {df[matches_col].mean():.2f}")
    print(f"Median Matches Played      : {df[matches_col].median():.1f}")
    print(f"Mode Matches Played        : {df[matches_col].mode().tolist()[0]} (Appears {sum(df[matches_col] == df[matches_col].mode()[0])} times)")
    print("=" * 65)

if __name__ == "__main__":
    analyze_dataset()
