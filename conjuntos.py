classic_car = {'Voyage', 'Opala', 'Chevette', 'fusca', 'Marverick', 'Camaro', 'Mustang'}

news_car = {'Voyage', 'Polo', 'Argo', 'Cross', 'HB-20', 'Camaro', 'Mustang'}

uniq_cars = classic_car | news_car #tbm pode ser feito da maneira baixo
#uniq_cars = classic_car.union(news_car)
print(f'Aqui não repete os carros: {uniq_cars}')

remake_cars = classic_car & news_car #tbm pode ser feito da maneira baixo
#remake_cars = classic_car.intersection(news_car)
print(f'Aqui mostra os carros iguais: {remake_cars}')

classic_car_only = classic_car.difference(news_car)
print(f'Aqui mostra somente os carros classicos e unicos: {classic_car_only}')

news_car_only = news_car.difference(classic_car)
print(f'Aqui mosta somente os novos carros e unicos: {news_car_only}')