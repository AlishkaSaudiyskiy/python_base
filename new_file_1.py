sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}



distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris


print(distances)
