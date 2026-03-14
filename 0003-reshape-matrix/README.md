# Reshape Matrix

## Difficulty

Easy

## Topic

Linear Algebra / Matrix Manipulation

## Problem

Write a Python function that reshapes a given matrix into a specified
shape.\
If the matrix **cannot be reshaped**, the function should return an
**empty list `[]`**.

Reshaping a matrix means rearranging the elements of the matrix into a
new dimension **without changing the order of the elements**.

The total number of elements **must remain the same**.

------------------------------------------------------------------------

## Example

### Input

    a = [[1,2,3,4],
         [5,6,7,8]]

    new_shape = (4,2)

### Output

    [[1,2],
     [3,4],
     [5,6],
     [7,8]]

------------------------------------------------------------------------

## Reasoning

The original matrix shape is:

    2 x 4

Total elements:

    2 * 4 = 8

The new requested shape is:

    4 x 2

Total elements:

    4 * 2 = 8

Since the number of elements is the same, reshaping is **valid**.

The matrix elements are first read **row by row**:

    [1,2,3,4,5,6,7,8]

Then they are placed into the new shape `(4,2)`:

    [[1,2],
     [3,4],
     [5,6],
     [7,8]]

------------------------------------------------------------------------

## Solution (PyTorch)

``` python
import torch

def reshape_matrix(a, new_shape):
    # check if reshape is possible
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return []

    tensor_matrix = torch.tensor(a)

    reshaped = tensor_matrix.reshape(new_shape)

    return reshaped.tolist()
```

------------------------------------------------------------------------

## Complexity

### Time Complexity

    O(n)

Where **n** is the number of elements in the matrix.

### Space Complexity

    O(n)

Because a new reshaped matrix is created.

------------------------------------------------------------------------

## Key Idea

A matrix can only be reshaped if:

    rows * columns = new_rows * new_columns

The reshape operation **does not change the data**, it only changes how
the data is **organized in rows and columns**.
