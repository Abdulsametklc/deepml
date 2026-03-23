import torch

def solve_jacobi(A, b, n) -> torch.Tensor:
    A_t = torch.as_tensor(A, dtype = torch.float)
    b_t = torch.as_tensor(b, dtype = torch.float)
  
    x = torch.zeros_like(b_t)
    D = torch.diag(A_t)
    R = A_t - torch.diag_embed(D)
  
    for _ in range(n):
        x = (b_t - torch.matmul(R, x)) / D
    return x
