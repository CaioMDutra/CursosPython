'''paises = {'br' : 'Brasil', 'eua': 'Estados Unidos', 'py' : 'Paraguai'}

paises |= {'ko':'Coreia'}

pais = paises.get('ko')

print(paises.get('br'))
print(pais)

paises.update({'br': 'Brazil'})

print(paises)

paises.pop('py')

print(paises)

del paises['eua']

print(paises)'''

paises = {'br' : 'Brasil', 'eua': 'Estados Unidos', 'py' : 'Paraguai'}

print(paises.get('br', 'chave não encontrada'))