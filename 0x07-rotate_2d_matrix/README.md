Rotate 2D Matrix
Description

This project is about implementing an algorithm that rotates a 2D matrix 90 degrees clockwise in-place using Python. The goal is to manipulate a given n x n 2D matrix directly without creating a copy, ensuring minimal space complexity.
Concepts
Matrix Representation

    The matrix is represented as a list of lists in Python. For example:

    csharp

    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

Matrix Transposition

    The first step is to transpose the matrix, which involves swapping rows with columns.

Reversing Rows

    After transposing the matrix, each row is reversed to complete the 90-degree clockwise rotation.

Requirements

    All files are interpreted on Ubuntu 20.04 LTS using Python 3.8.10.
    The solution should follow the pycodestyle style guide (version 2.8.0).
    The program should not return anything; the matrix is modified in place.
    You are not allowed to import any modules.

Task
0. Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    The matrix must be rotated in-place.
    The input matrix will always be 2-dimensional and non-empty.

Example

bash

$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Algorithm

The algorithm works in two steps:

    Transpose the matrix: Swap elements at (i, j) with elements at (j, i) for i < j.
    Reverse each row: Reverse every row in the matrix to complete the 90-degree clockwise rotation.

Files

    0-rotate_2d_matrix.py: Contains the implementation of the rotate_2d_matrix function.
    main_0.py: Test file to verify the solution.
