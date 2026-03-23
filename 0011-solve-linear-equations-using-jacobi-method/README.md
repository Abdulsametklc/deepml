# Solve Linear Equations using Jacobi Method

## Problem Description

Write a Python function that uses the Jacobi method to solve a system of linear equations given by:

[
Ax = b
]

The function should:

* Initialize the solution vector ( x ) with zeros
* Perform exactly ( n ) iterations
* Update each component of ( x ) using the Jacobi formula
* Round each intermediate value to **4 decimal places**
* Return the final approximate solution as a list

---

## Jacobi Formula

For each element:

[
x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j \right)
]

---

## Notes

* The method uses only values from the previous iteration
* Rounding is applied at each iteration step
* The solution is approximate and depends on the number of iterations
* The method may not converge for all matrices
