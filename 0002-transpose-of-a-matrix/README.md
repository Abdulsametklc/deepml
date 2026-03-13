# Transpose of a Matrix

**Difficulty:** Easy\
**Topic:** Linear Algebra

## Problem

Write a Python function that computes the **transpose of a given 2D
matrix**.

The transpose of a matrix is formed by **turning its rows into columns
and its columns into rows**.

If the original matrix has dimensions **m × n**, the transposed matrix
will have dimensions **n × m**.

------------------------------------------------------------------------

## Example

**Input**

    a = [[1, 2, 3], [4, 5, 6]]

**Output**

    [[1, 4], [2, 5], [3, 6]]

------------------------------------------------------------------------

## Reasoning

The input matrix has **2 rows and 3 columns (2×3)**.

    1  2  3
    4  5  6

When we take the transpose:

-   Rows become columns
-   Columns become rows

Resulting matrix:

    1  4
    2  5
    3  6

Which corresponds to:

    [[1, 4], [2, 5], [3, 6]]
