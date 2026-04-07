import torch

def linear_regression_normal_equation(X, y) -> torch.Tensor:
    X_t = torch.as_tensor(X, dtype=torch.float)
    y_t = torch.as_tensor(y, dtype=torch.float).reshape(-1,1)

    X_transpose = X_t.T
    xtx = X_transpose @ X_t
    xtx_inv = torch.inverse(xtx)

    xty = X_transpose @ y_t

    theta = xtx_inv @ xty

    theta = theta.flatten()
    theta = torch.round(theta * 10000) / 10000
    return theta
