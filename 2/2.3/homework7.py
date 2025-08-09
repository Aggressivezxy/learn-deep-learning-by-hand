import torch

x = torch.arange(24).reshape(2,3,4)
sum_axis0 = x.sum(axis=0)
sum_axis1 = x.sum(axis=1)
sum_axis2 = x.sum(axis=2)
print("X:", x)
print("Sum along axis 0:", sum_axis0)
print("Sum along axis 1:", sum_axis1)
print("Sum along axis 2:", sum_axis2)