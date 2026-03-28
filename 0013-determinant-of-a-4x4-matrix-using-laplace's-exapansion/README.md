# Determinant of a 4x4 Matrix using Laplace's Expansion

## 📌 Problem Description

Write a Python function that calculates the determinant of a **4x4 matrix** using **Laplace's Expansion method**.

The function should:

* Take a single argument: a 4x4 matrix (list of lists)
* Return the determinant as a float or integer
* Use **recursion** to compute determinants of smaller matrices (3x3 → 2x2)

---

## 🧠 Concept: Laplace Expansion

Laplace Expansion calculates the determinant by expanding along a row (commonly the first row):

* Each element is multiplied by its **cofactor**
* Cofactor includes:

  * A **sign**: (-1)^(row + column)
  * The **determinant of the minor matrix**

The process continues recursively until reaching a **2x2 matrix**, which is directly solvable.

---

## 🔢 Base Case

For a 2x2 matrix:

```
|a  b|
|c  d|
```

Determinant = (a * d) - (b * c)

---

## 🧩 Example

### Input

```
a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]
```

### Output

```
0
```

### Reasoning

This matrix has linearly dependent rows, so its determinant is **0**.
