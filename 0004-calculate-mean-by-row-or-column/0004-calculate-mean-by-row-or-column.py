import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
  a_t = torch.as_tensor(matrix, dtype = torch.float)
  if mode == "column":
      a_t = a_t.mean(dim = 0)
  else:
      a_t = a_t.mean(dim = 1)
  return a_t
