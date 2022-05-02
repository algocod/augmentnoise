import pandas as pd

data = ['Loss']
data.append(2.333)
data.append(4.66)

dft = pd.DataFrame(data)
dft.to_csv('C:\\Users\\hk_le\\devwork\\CS7643\\output\\trainloss_test.csv',sep='\t', encoding='utf-8', index=False)