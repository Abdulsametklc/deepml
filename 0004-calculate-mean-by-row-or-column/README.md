# Calculate Mean by Row or Column

**Difficulty:** Easy\
**Topic:** Linear Algebra

## Problem Description

Write a Python function that calculates the **mean of a matrix** either
**by row** or **by column**, based on a given mode.

The function should:

-   Take a **matrix (list of lists)** as input
-   Take a **mode** parameter which can be:
    -   `'row'`
    -   `'column'`
-   Return a **list containing the means** calculated according to the
    specified mode.

------------------------------------------------------------------------

## Function Signature

``` python
def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
```

------------------------------------------------------------------------

## Example

### Input

``` python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

mode = 'column'
```

### Output

``` python
[4.0, 5.0, 6.0]
```

### Explanation

Column means are calculated as:

    (1 + 4 + 7) / 3 = 4
    (2 + 5 + 8) / 3 = 5
    (3 + 6 + 9) / 3 = 6

Result:

    [4.0, 5.0, 6.0]

------------------------------------------------------------------------

## Solution Using PyTorch

``` python
import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:

    tensor = torch.tensor(matrix, dtype=torch.float)

    if mode == "row":
        return tensor.mean(dim=1)
    
    if mode == "column":
        return tensor.mean(dim=0)
```

------------------------------------------------------------------------

## Example Usage

``` python
import torch

print(
    calculate_matrix_mean(
        [[1.0,2.0,3.0],[4.0,5.0,6.0]],
        'row'
    ).numpy().tolist()
)
```

Output

    [2.0, 5.0]

------------------------------------------------------------------------

## Key Concept

PyTorch dimension behavior:

  Operation     Code
  ------------- ---------------
  Row mean      `mean(dim=1)`
  Column mean   `mean(dim=0)`

-   **dim=0 → column operation**
-   **dim=1 → row operation**

------------------------------------------------------------------------

## Time Complexity

    O(n × m)

Where:

-   `n` = number of rows
-   `m` = number of columns

------------------------------------------------------------------------

## Tags

-   Matrix
-   Linear Algebra
-   PyTorch
-   Mean
