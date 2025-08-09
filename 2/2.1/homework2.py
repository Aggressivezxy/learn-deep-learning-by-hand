import torch
a = torch.arange(6).reshape((3, 1, 2))
b = torch.arange(2).reshape((1, 2, 1))
print(a)
print(b)
print(a + b)
