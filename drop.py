import pandas as pd

# Criar um DataFrame de exemplo
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
print(type(data))
df = pd.DataFrame(data)
print(df)

# Remover a coluna 'B' usando o método drop()
df = df.drop('A', axis=1)

print(df)
