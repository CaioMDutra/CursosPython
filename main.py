import csv
import pandas as pd

tabela = pd.read_csv('perfil.csv')

profile = {'name':'N/A',
    'fone':'N/A',
    'email':'N/A'
}

user_input = {
    'name': input('Qual seu nome? '),
    'email': input('Qual seu email? '),
    'fone': int(input('Qual seu telefone? '))

}

profile |= user_input

profile.update(user_input)

# Especificar o nome do arquivo CSV
arquivo_csv = 'perfil.csv'

# Abrir o arquivo CSV em modo de escrita
with open(arquivo_csv, 'a', newline='') as arquivo_csv:

    # Criar um objeto escritor CSV
    escritor_csv = csv.writer(arquivo_csv)
       
    # Escrever os dados do perfil no arquivo
    escritor_csv.writerow(profile.values())

print('Dados salvos com sucesso!.')

tabela = pd.read_csv('perfil.csv')

print(tabela)