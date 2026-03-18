# Calculate Eigenvalues of a 2x2 Matrix

## 🧠 Problem
Write a Python function that calculates the eigenvalues of a 2x2 matrix.  
Return the eigenvalues sorted from **highest to lowest**.

---

## 📌 Example

**Input:**
```python
matrix = [[2, 1], [1, 2]]
```

**Output:**
```python
[3.0, 1.0]
```

---

## 🔑 Explanation

For a 2x2 matrix:

```
[a  b]
[c  d]
```

We compute:

- **Trace:**  
```
trace = a + d
```

- **Determinant:**  
```
det = a*d - b*c
```

- **Characteristic Equation:**
```
λ² - trace(A)λ + det(A) = 0
```

Solve using quadratic formula:
```
λ = (trace ± √(trace² - 4*det)) / 2
```

---

## 🧪 Implementation (PyTorch)

```python
import torch

def calculate_eigenvalues(matrix):
    A = torch.tensor(matrix, dtype=torch.float32)

    a, b = A[0, 0], A[0, 1]
    c, d = A[1, 0], A[1, 1]

    trace = a + d
    det = a * d - b * c

    disc = trace**2 - 4 * det

    lambda1 = (trace + torch.sqrt(disc)) / 2
    lambda2 = (trace - torch.sqrt(disc)) / 2

    result = torch.tensor([lambda1, lambda2])
    result, _ = torch.sort(result, descending=True)

    return result.tolist()
```

---

## 🚀 Notes

- If `disc < 0`, eigenvalues become complex.
- PyTorch also provides a built-in method:
```python
torch.linalg.eigvals(A)
```
But implementing manually helps understand the math.

---

## ✅ Complexity

- Time: **O(1)**  
- Space: **O(1)**

---

## 🎯 Summary

- Use trace and determinant  
- Solve quadratic equation  
- Sort results  

---

Happy Coding 🚀
