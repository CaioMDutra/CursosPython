'''
Entendendo o **kwargs
'''

df = {'nome' : ['caio', 'cassio', 'rodolfo', 'gabriel'],
      'idade' : ['33', '31', '30', '21' ],
      'CPF' : [39122944885, 9122944800, 6722944899, 19322944885],
      'sobrenome' : ['Dutra', 'Pilon', 'Gabriel', 'Gomes'],
      }

def retorna_dados(**kwargs):
    return f"{kwargs['nome']},{kwargs['idade']},{kwargs['CPF']},{kwargs['sobrenome']}"

print(retorna_dados(**df))