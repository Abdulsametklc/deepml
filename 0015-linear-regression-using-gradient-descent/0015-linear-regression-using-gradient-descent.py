import torch

def linear_regression_gradient_descent(X, y, alpha, iterations) -> torch.Tensor:
    X_t = torch.as_tensor(X, dtype = torch.float32)
    y_t = torch.as_tensor(y, dtype = torch.float32).reshape(-1,1)

    m, n = X_t.shape

    theta = torch.zeros((n, 1), dtype=torch.float32, requires_grad=True)

    for _ in range(iterations):
        y_pred = X_t @ theta
        loss = (1 / (2 * m)) * torch.sum((y_pred - y_t) ** 2)
        loss.backward()

        with torch.no_grad():
            theta -= alpha * theta.grad
        
        theta.grad.zero_()

    return theta.detach().flatten()
