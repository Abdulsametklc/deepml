# Calculate 2x2 Matrix Inverse

## 📌 Problem Description

Write a Python function that calculates the inverse of a 2x2 matrix.

The inverse of a matrix **A** is another matrix **A⁻¹** such that:

A × A⁻¹ = I (identity matrix)

For a 2x2 matrix:

    [[a, b],
     [c, d]]

The inverse exists only if the determinant is non-zero:

    det = ad - bc

If `det = 0`, the matrix is **not invertible**, and the function should
return `None`.

------------------------------------------------------------------------

## 🧮 Formula

    A⁻¹ = (1 / (ad - bc)) × [[ d, -b],
                             [-c,  a]]

------------------------------------------------------------------------

## 🧠 Example

**Input:**

    matrix = [[4, 7], [2, 6]]

**Steps:** - det = 4×6 - 7×2 = 24 - 14 = 10 - Since det ≠ 0 → invertible

**Output:**

    [[0.6, -0.7],
     [-0.2, 0.4]]

------------------------------------------------------------------------

## 💻 Python Solution (PyTorch)

``` python
import torch

def inverse_2x2(matrix):
    m = torch.tensor(matrix, dtype=torch.float32)

    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]

    det = a * d - b * c

    if det == 0:
        return None

    inv = torch.tensor([
        [d, -b],
        [-c, a]
    ], dtype=torch.float32)

    return inv / det
```

------------------------------------------------------------------------

## 🚀 Notes

-   Time Complexity: **O(1)**

-   Works only for **2x2 matrices**

-   For larger matrices, use:

    ``` python
    torch.inverse(matrix)
    ```

------------------------------------------------------------------------

## 🎯 Key Takeaways

-   Determinant decides invertibility
-   Simple formula for 2x2 inverse
-   Useful for interviews and fundamentals
