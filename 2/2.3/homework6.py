import torch

A = torch.arange(20).reshape(5, 4)
print(A/A.sum(axis=1))
# ������״��ƥ�䣬���¹㲥��broadcasting��ʧ��