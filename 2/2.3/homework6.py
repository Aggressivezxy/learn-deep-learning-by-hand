import torch

A = torch.arange(20).reshape(5, 4)
print(A/A.sum(axis=1))
# 张量形状不匹配，导致广播（broadcasting）失败