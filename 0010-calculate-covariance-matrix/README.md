# Calculate Covariance Matrix

## Problem Description

Given a list of vectors, compute the covariance matrix.

Each inner list represents a feature and contains its observations.

## Key Idea

-   Each feature has a mean.
-   Covariance measures how two features vary together.
-   If they increase/decrease together → positive covariance.
-   If one increases while the other decreases → negative covariance.

## Important Notes

-   Input format: (features, samples)
-   Covariance matrix is always symmetric.
-   Diagonal values represent variance.

## Example

Input: \[\[1, 2, 3\], \[4, 5, 6\]\]

Output: \[\[1.0, 1.0\], \[1.0, 1.0\]\]

## Approach (Conceptual)

1.  Compute mean of each feature
2.  Subtract mean from each value (centering)
3.  Multiply deviations pairwise
4.  Average using (n - 1)

## Use Cases

-   Machine Learning
-   PCA (Principal Component Analysis)
-   Feature analysis
-   Statistics
