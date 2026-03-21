import torch

def matrixmul(a,b) -> torch.Tensor:
    A_t = torch.as_tensor(a, dtype = torch.float)
    B_t = torch.as_tensor(b, dtype = torch.float)

    if A_t.shape[1] != B_t.shape[0]:
        return torch.tensor(-1)

    return torch.matmul(A_t, B_t)
