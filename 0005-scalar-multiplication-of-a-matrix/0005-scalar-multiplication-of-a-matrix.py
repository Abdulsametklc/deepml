import torch

def scalar_multiply(matrix, scalar) -> torch.Tensor:
  m_t = torch.as_tensor(matrix, dtype = torch.float)
  m_t = m_t * scalar
  return m_t
