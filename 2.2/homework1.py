import os
import pandas as pd


os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'homework.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,HOST,Price\n')  # 列名
    f.write('NA,Pave,ALEX,127500\n') 
    f.write('2,NA,PETE,106000\n')
    f.write('4,NA,JOHN,178100\n')
    f.write('NA,NA,MIKE,140000\n')
    f.write('3,NA,ALICE,123000\n')
    f.write('5,Pave,BOB,150000\n')

# 删除缺失值最多的一列
data = pd.read_csv(data_file)
na_count = data.isna().sum()  # 计算每列的缺失值数量
max_na_col = na_count.idxmax()  # 找到缺失值最多的列
data = data.drop(columns=[max_na_col])  # 删除该列
data.to_csv(data_file, index=False)  # 保存修改后的数据