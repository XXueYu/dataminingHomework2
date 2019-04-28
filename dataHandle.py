import numpy
import pandas as pd

# 数据准备
data=pd.read_csv('cbg_patterns.csv')

# 取表中的一列的前一万项作为数据源，挖掘各种品牌店铺的相关性
brands=data['related_same_month_brand'][0:100]

for count in brands.index:
    brands[count] = brands[count][2:-2].split('","')

list=[]
for count in brands.index:
    list.append(brands[count])

data=pd.DataFrame(list)
data.to_csv('data_copy(for test).csv', sep=",")
