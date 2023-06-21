import pandas as pd

atendimentos_df = pd.read_csv('contcontract.csv')
print(atendimentos_df.describe())
