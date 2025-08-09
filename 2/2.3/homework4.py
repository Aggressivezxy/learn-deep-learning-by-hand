import torch

x = torch.arange(24).reshape(2,3,4)
print(len(x))

# len(张量) 等价于 张量.shape[0]