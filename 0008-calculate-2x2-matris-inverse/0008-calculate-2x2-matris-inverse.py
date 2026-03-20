import torch

def inverse_2x2(matrix) -> torch.Tensor | None:
    m_t = torch.as_tensor(matrix, dtype = torch.float)

    a = m_t[0][0]
    b = m_t[0][1]
    c = m_t[1][0]
    d = m_t[1][1]

    det = a*d - b*c
    if det == 0:
        return None

    inv = torch.tensor([
      [d,-b],
      [-c,a]
    ], dtype = torch.float32)

    return inv * ( 1/det)
