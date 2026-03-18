# Matrix Transformation

## 📌 Problem Description

Write a Python function that transforms a given matrix **A** using the operation:

[
T^{-1} A S
]

where **T** and **S** are invertible matrices.

---

## ⚙️ Requirements

* Validate whether matrices **T** and **S** are invertible.
* If either matrix is not invertible, return:

  ```
  -1
  ```
* If both are invertible:

  * Compute the inverse of **T**
  * Perform matrix multiplication in order:

    ```
    T⁻¹ × A × S
    ```

---

## 📥 Input

* `A`: 2D list (matrix)
* `T`: 2D list (invertible matrix)
* `S`: 2D list (invertible matrix)

---

## 📤 Output

* Transformed matrix as a 2D list
* OR `-1` if no solution exists

---

## 🧠 Example

### Input

```python
A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]
```

### Output

```python
[[0.5, 1.5], [1.5, 3.5]]
```

---
