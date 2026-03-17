# Scalar Multiplication of a Matrix

## 📌 Problem Description

Write a Python function that multiplies a given matrix by a scalar value and returns the resulting matrix.

Scalar multiplication means multiplying every element of the matrix by a single number (scalar).

---

## 🧠 Example

### Input
```python
matrix = [[1, 2], [3, 4]]
scalar = 2
```

### Output
```python
[[2, 4], [6, 8]]
```

### Explanation

Each element in the matrix is multiplied by the scalar:

```
[1*2, 2*2] → [2, 4]
[3*2, 4*2] → [6, 8]
```

---

## 🚀 Solution

```python
def scalar_multiply(matrix, scalar):
    result = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result.append(new_row)

    return result
```

---

## ⚡ Alternative (Pythonic Way)

```python
def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]
```

---

## 🧪 Test

```python
matrix = [[1, 2], [3, 4]]
scalar = 2

print(scalar_multiply(matrix, scalar))
# Output: [[2, 4], [6, 8]]
```

---

## 📚 Key Concepts

- Matrix: List of lists in Python
- Scalar: A single number
- Nested loops / list comprehension

---

## 🎯 Complexity

- Time Complexity: O(n × m)  
- Space Complexity: O(n × m)  

(n = number of rows, m = number of columns)

---

## 🏁 Summary

Scalar multiplication is a fundamental linear algebra operation where every element of a matrix is multiplied by a constant value.
