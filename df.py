import pandas as pd

df = {'nome' : ['caio', 'cassio', 'rodolfo', 'gabriel'],
      'idade' : ['33', '31', '30', '21' ],
      'CPF' : [39122944885, 9122944800, 6722944899, 19322944885],
      'sobrenome' : ['Dutra', 'Pilon', 'Gabriel', 'Gomes'],
      }

'''df = pd.DataFrame(df)

df['nome'] = df['nome'].str.title()

print(df)

df = df.rename(columns={'phone':'Telefone','nome':'Nome','cargo':'Cargo','empresa':'Empresa'})
#print(df)

df = df[['Nome', 'Cargo', 'Empresa', 'Telefone', 'CPF']]
#print(df)

df['CPF'] = df['CPF'].apply(lambda x: str(x).zfill(11))
#print(df)

df = df.drop_duplicates()
#print(df)

df.to_excel('dados.xlsx', index=False)'''

