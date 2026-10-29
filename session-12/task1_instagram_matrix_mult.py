"""
Session 12 - Task 1: Instagram Post Engagement Matrix Multiplication
File: session-12/task1_instagram_matrix_mult.py

Description:
Given two 2x2 matrices representing likes and comments for two Instagram
posts over two days, performs matrix multiplication and displays the
resulting matrix along with step-by-step dot product arithmetic.
"""

import numpy as np

def run_task1():
    print("=" * 70)
    print(" TASK 1: INSTAGRAM POST ENGAGEMENT MATRIX MULTIPLICATION")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1. Define Two 2x2 Matrices
    # Matrix A: Post Engagement on Day 1 [Likes, Comments]
    # Rows: Post 1, Post 2
    # Columns: Likes, Comments
    # -------------------------------------------------------------
    A = np.array([
        [120, 15],   # Post 1: 120 likes, 15 comments
        [80,  25]    # Post 2: 80 likes,  25 comments
    ])

    # Matrix B: Interaction weight / Day 2 rate matrix
    # Rows: Weight for Likes, Weight for Comments
    # Columns: Reach Score Factor, Engagement Value Factor
    B = np.array([
        [2, 1],      # Like weights: Reach factor = 2, Engagement factor = 1
        [3, 4]       # Comment weights: Reach factor = 3, Engagement factor = 4
    ])

    print("Matrix A (Instagram Posts: Likes & Comments):")
    print("           [Likes  Comments]")
    print(f"Post 1:    {A[0]}")
    print(f"Post 2:    {A[1]}")
    print("\nMatrix B (Engagement Multipliers / Weights):")
    print("           [Factor 1  Factor 2]")
    print(f"Row 1:     {B[0]}")
    print(f"Row 2:     {B[1]}")
    print("-" * 70)

    # -------------------------------------------------------------
    # 2. Step-by-Step Manual Dot Product Arithmetic
    # C[i, j] = Row i of A . Column j of B
    # -------------------------------------------------------------
    c00 = A[0, 0] * B[0, 0] + A[0, 1] * B[1, 0]  # 120*2 + 15*3 = 240 + 45 = 285
    c01 = A[0, 0] * B[0, 1] + A[0, 1] * B[1, 1]  # 120*1 + 15*4 = 120 + 60 = 180
    c10 = A[1, 0] * B[0, 0] + A[1, 1] * B[1, 0]  # 80*2 + 25*3  = 160 + 75 = 235
    c11 = A[1, 0] * B[0, 1] + A[1, 1] * B[1, 1]  # 80*1 + 25*4  = 80 + 100 = 180

    print("STEP-BY-STEP CALCULATION:")
    print(f"- C[0, 0] = (120 * 2) + (15 * 3) = 240 + 45  = {c00}")
    print(f"- C[0, 1] = (120 * 1) + (15 * 4) = 120 + 60  = {c01}")
    print(f"- C[1, 0] = (80 * 2)  + (25 * 3) = 160 + 75  = {c10}")
    print(f"- C[1, 1] = (80 * 1)  + (25 * 4) = 80 + 100  = {c11}")
    print("-" * 70)

    # -------------------------------------------------------------
    # 3. Matrix Multiplication via NumPy (A @ B or np.matmul)
    # -------------------------------------------------------------
    C = np.matmul(A, B)

    print("RESULTING MULTIPLIED MATRIX (C = A x B):")
    print(C)
    print("-" * 70)
    print(f"Post 1 Composite Metrics: {C[0]}")
    print(f"Post 2 Composite Metrics: {C[1]}")
    print("=" * 70)

if __name__ == "__main__":
    run_task1()

