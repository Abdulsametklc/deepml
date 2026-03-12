# Matrix--Vector Dot Product (Python)

This project implements a Python function that computes the **dot
product of a matrix and a vector**.

The function verifies whether the matrix and vector dimensions are
compatible before performing the operation. If the dimensions do not
match, the function returns **-1**.

------------------------------------------------------------------------

## Problem Description

Write a Python function that computes the dot product of a **matrix**
and a **vector**.

-   A **matrix** is represented as a list of lists.
-   A **vector** is represented as a list.

The operation is valid **only if the number of columns in the matrix
equals the length of the vector**.

If the dimensions are incompatible, the function should return **-1**.

------------------------------------------------------------------------

## Example

### Input

``` python
a = [[1, 2], [2, 4]]
b = [1, 2]
```

### Output

    [5, 10]

### Explanation

Row 1 calculation:

    (1 * 1) + (2 * 2) = 1 + 4 = 5

Row 2 calculation:

    (2 * 1) + (4 * 2) = 2 + 8 = 10

Resulting vector:

    [5, 10]

------------------------------------------------------------------------

## Python Implementation

``` python
def matrix_dot_vector(a, b):
    if len(a[0]) != len(b):
        return -1

    result = []

    for row in a:
        dot_product = 0
        for i in range(len(b)):
            dot_product += row[i] * b[i]
        result.append(dot_product)

    return result
```

------------------------------------------------------------------------

## How It Works

1.  Check whether the **number of columns in the matrix equals the
    vector length**.
2.  If not, return **-1**.
3.  For each row in the matrix:
    -   Multiply each element with the corresponding vector element.
    -   Sum the results.
4.  Store the sum as part of the resulting vector.

------------------------------------------------------------------------

## Complexity

**Time Complexity**

    O(n × m)

-   `n` = number of rows in the matrix\
-   `m` = number of columns

**Space Complexity**

    O(n)

because the output vector contains one result for each row.
