import torch
import torch.nn.functional as F

def softmax(scores: list[float]) -> list[float]:
    
  x = torch.tensor(scores, dtype = torch.float32)

  x_max = torch.max(x)
  x_stable = x - x_max

  exp_x = torch.exp(x_stable)
  softmax_x = exp_x / torch.sum(exp_x)

  return [float(torch.round(p * 10000) / 10000) for p in softmax_x]
