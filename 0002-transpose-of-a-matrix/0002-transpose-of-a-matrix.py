import torch

def transpose_matrix(a) -> torch.Tensor:
  a_t = torch.as_tensor(a)
  a_t = a_t.T
  return a_t
