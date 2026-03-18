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

## 💡 Explanation

1. Check if **T** and **S** are invertible
2. Compute **T⁻¹**
3. Multiply matrices in order:

   ```
   T⁻¹ × A × S
   ```

---

## 🛠️ Implementation (PyTorch)

```python
import torch

def matrix_transformation(A, T, S):
    A = torch.tensor(A, dtype=torch.float32)
    T = torch.tensor(T, dtype=torch.float32)
    S = torch.tensor(S, dtype=torch.float32)

    # Check if T and S are invertible
    if torch.det(T) == 0 or torch.det(S) == 0:
        return -1

    # Compute transformation
    T_inv = torch.inverse(T)
    result = T_inv @ A @ S

    return result.tolist()
```

---

## 🚀 Key Points

* Use `torch.inverse()` to compute inverse
* Use `@` for matrix multiplication (NOT `*`)
* Matrix multiplication order matters
* Determinant must be non-zero for invertibility

---

## 🧪 Test

```python
print(matrix_transformation(
    [[1, 2], [3, 4]],
    [[2, 0], [0, 2]],
    [[1, 1], [0, 1]]
))
```

---

## ✅ Expected Output

```
[[0.5, 1.5], [1.5, 3.5]]
```
