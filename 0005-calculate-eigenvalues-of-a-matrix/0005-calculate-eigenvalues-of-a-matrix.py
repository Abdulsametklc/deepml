import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    a_t = torch.as_tensor(matrix, dtype = torch.float)

    a = a_t[0,0]
    b = a_t[0,1]
    c = a_t[1,0]
    d = a_t[1,1]

    trace = a + d
    det = a * d - b * c

    disc = trace**2 - 4*det

    lambda1 = (trace + torch.sqrt(disc)) / 2
    lambda2 = (trace - torch.sqrt(disc)) / 2

    result = torch.tensor([lamda1, lambda2])

    result, _ = torch.sort(result, descending = True)

    return result
