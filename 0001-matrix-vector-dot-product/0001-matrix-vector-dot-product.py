import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)

    if a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)

    result = torch.matmul(a_t, b_t)

    return result
