import torch

def transform_matrix(A, T, S) -> torch.tensor:
    A_t = torch.tensor(A, dtype = torch.float)
    T_t = torch.tensor(T, dtype = torch.float)
    S_t = torch.tensor(S, dtype = torch.float)

    T_t = torch.inverse(T_t)
    return torch.matmul(torch.matmul(T_t, A_t), S_t)
