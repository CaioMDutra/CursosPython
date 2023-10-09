from collections import Counter

'''
name = 'Caio de Macedo Dutra'

print(Counter(name.lower()))

'''

texto = '''Ash Ketchum foi mencionado pela primeira vez em um jogo eletrônico no diálogo de Pokémon Play It!
, e sua primeira aparição em um jogo foi em Pokémon Puzzle League. Satoshi Tajiri, o criador de Pokémon, 
com quem Ash compartilha seu nome japonês, afirmou que Ash representa o 'aspecto humano' da série, 
e que Ash reflete como ele era quando criança.'''

texto = texto.upper()

texto = texto.split()

res = Counter(texto)

#print(Counter(res))

print(res.most_common(5))