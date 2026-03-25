
# Singular Value Decomposition (SVD) of 2x2 Matrix

## Problem Description

The goal is to compute an **approximate Singular Value Decomposition (SVD)** of a real 2x2 matrix using **only one Jacobi rotation**.  

where:

- `U` is a 2x2 orthogonal matrix containing the **left singular vectors**.  
- `S` is a length-2 array containing the **singular values**.  
- `Vt` is the transpose of the right singular vector matrix `V`.

## Input

- `A`: a NumPy array of shape `(2, 2)`, containing real numbers.

## Output

- A tuple `(U, S, Vt)` representing the approximate SVD of the matrix.

The decomposition should **approximately satisfy**:

```
A ≈ U @ diag(S) @ Vt
```

## Rules and Constraints

- Only **basic NumPy operations** are allowed:
  - Matrix multiplication
  - Transpose
  - Element-wise arithmetic
  - Square roots, trigonometric functions, etc.
- Do **not** use:
  - `numpy.linalg.svd`
  - Any other high-level SVD routines
- Use **only one Jacobi rotation step** — no iterative refinements.
- This is an **approximate method**, so small numerical differences are acceptable.

## Example

**Input:**

```python
A = np.array([[2, 1],
              [1, 2]])
```

**Expected Approximate Output:**

```
U ≈ [[0.707, -0.707],
     [0.707,  0.707]]
S = [3.0, 1.0]
Vt ≈ [[0.707,  0.707],
      [-0.707, 0.707]]
```

**Reasoning:**

- The symmetric matrix `[[2, 1], [1, 2]]` has eigenvalues 3 and 1.  
- For symmetric matrices, the SVD simplifies: the singular values equal the **absolute eigenvalues**, and `U` and `V` are related to the eigenvectors.  
- The Jacobi rotation approximates the diagonalization of `A^T A` in a **single step**.

## Difficulty

- Understanding the connection between **eigenvalues** of `A^T A` and **singular values** of `A`.  
- Implementing a **single-step Jacobi rotation** to approximate the SVD.  
- Handling **ordering** of singular values and adjusting `U` and `V` accordingly.  
- Avoiding high-level linear algebra routines while maintaining an **orthogonal decomposition**.  

This problem requires both **linear algebra insight** and careful **numerical implementation**.
