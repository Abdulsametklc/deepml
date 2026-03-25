import torch

def svd_2x2_singular_values(A: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:

    ATA = A.T @ A

    a = ATA[0, 0].item()
    b = ATA[0, 1].item()
    d = ATA[1, 1].item()

    if b != 0:
        theta = 0.5 * torch.atan2(2 * torch.tensor(b), torch.tensor(a - d))
        c = torch.cos(theta)
        s = torch.sin(theta)
    else:
        c = torch.tensor(1.0)
        s = torch.tensor(0.0)

    V = torch.stack([
        torch.stack([c, -s]),
        torch.stack([s,  c])
    ])

    ATA_diag = V.T @ ATA @ V

    sigma1 = torch.sqrt(ATA_diag[0, 0])
    sigma2 = torch.sqrt(ATA_diag[1, 1])

    S = torch.stack([sigma1, sigma2])
    S, idx = torch.sort(S, descending=True)
    V = V[:, idx]

    Sigma_inv = torch.diag(1 / S)
    U = A @ V @ Sigma_inv

    Vt = V.T

    return U, S, Vt
