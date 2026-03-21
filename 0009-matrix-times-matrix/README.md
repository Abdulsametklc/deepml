# Matrix Times Matrix

## 📌 Problem

Write a function that multiplies two matrices.

Given two matrices **A** and **B**, compute:

C = A · B

------------------------------------------------------------------------

## ✅ Rules

-   Matrix multiplication is valid only if:

    number of columns in A = number of rows in B

-   If shapes are not aligned, return **-1**

------------------------------------------------------------------------

## 🧠 Example 1

**Input:** A = \[\[1, 2\], \[2, 4\]\]\
B = \[\[2, 1\], \[3, 4\]\]

**Output:** \[\[8, 9\], \[16, 18\]\]

**Explanation:** - (1×2 + 2×3) = 8\
- (1×1 + 2×4) = 9\
- (2×2 + 4×3) = 16\
- (2×1 + 4×4) = 18

------------------------------------------------------------------------

## ❌ Example 2

**Input:** A = \[\[1, 2\], \[2, 4\]\]\
B = \[\[2, 1\], \[3, 4\], \[4, 5\]\]

**Output:** -1

**Explanation:** Matrix shapes are not compatible for multiplication.
