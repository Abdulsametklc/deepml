import torch

def calculate_covariance_matrix(vectors) -> torch.Tensor:
    v_t = torch.as_tensor(vectors, dtype = torch.float)
    return torch.cov(v_t)
