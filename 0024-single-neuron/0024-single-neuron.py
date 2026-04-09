import torch
import torch.nn.functional as F
from typing import List, Tuple

def single_neuron_model(
    features: List[List[float]],
    labels: List[float],
    weights: List[float],
    bias: float
) -> Tuple[List[float], float]:
    X = torch.tensor(features, dtype = torch.float32)
    y = torch.tensor(labels, dtype = torch.float32)
    w = torch.tensor(weights, dtype = torch.float32)
    b = torch.tensor(bias, dtype = torch.float32)

    z = X @ w + b
    y_pred = torch.sigmoid(z)
    mse = F.mse_loss(y_pred, y)
    y_pred_list = [round (float(p),4) for p in y_pred]
    mse_val = round(float(mse),4)

    return y_pred_list, mse_val
