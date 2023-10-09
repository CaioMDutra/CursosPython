dict = {1 : 'Botafogo',
        2: 'Palmeiras',
        3: 'Gremio',
        4: 'Flamengo',
        5: 'Fluminense',
        6: 'Bragantino',
        7: 'Athletico',
        8: 'Fortaleza',
        9: 'Atletico-MG',
        10: 'Cuiaba'}

'''
print(dict.get(2, 'Não encontrado')) #quando usar o get() necessário o uso dos parenteses! e definir o padrão para não encontrados.
print(dict.get(11, 'Não encontrado')) # se a chave não estiver no dicionario, ele retorna o segindo parametro.
print(dict[1]) #quando usar somente a posição usar os [conchetes], se não encontrado retorna KeyErros.

'''
input = {11: 'Vasco',
         12: 'Internacional',
         13: 'Cruzeiro',
         14: 'São Paulo',
         15: 'Goias',
         16: 'Bahia',
         17: 'Santos',
         18: 'Coritiba',
         19: 'Corinthians',
         20: 'America-MG'}

dict |= input

for chave, valor in dict.items():
    print(f'Posição {chave}: {valor}')





