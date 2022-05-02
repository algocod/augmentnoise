import pandas as pd

col_names = ["Target_Labels", "Pseudo_Labels"]
#df = pd.DataFrame(columns= col_names)
#
# df2 = {'Target_Labels': 'trgt2', 'Pseudo_Labels': 'psed2'}
# df3 = {'Target_Labels': 'trgt3', 'Pseudo_Labels': 'psed3'}
# df4 = {'Target_Labels': 'trgt4', 'Pseudo_Labels': 'psed4'}
# df = df.append(df2, ignore_index = True)
# df = df.append(df3, ignore_index = True)
# df = df.append(df4, ignore_index = True)

L = []
P = []
L.append("trgt1")
L.append("trgt2")
P.append("Psedo1")
P.append("Psedo2")
df = pd.DataFrame()


df["Target_Labels"] = L
df["Pseudo_Labels"] = P

df.to_csv('C:\\Users\\hk_le\\devwork\\CS7643\\output\\pseudoLabels\\exp1.csv', encoding='utf-8', index=False)