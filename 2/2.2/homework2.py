import os
import pandas as pd
import torch

data_file = os.path.join('..', 'data', 'homework.csv')
data = pd.read_csv(data_file)
# 将处理后的数据集转换为张量格式
input,output = data.iloc[:, 0:1], data.iloc[:, -1]
x = torch.tensor(input.values, dtype=torch.float32)
y = torch.tensor(output.values, dtype=torch.float32)
print(x)
print(y)