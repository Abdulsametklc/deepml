import torch

def det(m):
    n = m.shape[0]

    if n == 2:
        return (m[0,0]*m[1,1] - m[0,1]*m[1,0]).item()

    total = 0
    for c in range(n):
        minor = torch.cat((m[1:, :c], m[1:, c+1:]), dim=1)
        total += ((-1)**c) * m[0,c].item() * det(minor)

    return total


def determinant_4x4(matrix):
    m = torch.as_tensor(matrix, dtype=torch.float)
    return det(m)
