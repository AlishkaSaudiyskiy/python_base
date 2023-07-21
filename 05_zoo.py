zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

print(('Клетка в которой сидит лев -'), zoo.index('lion'), ('Клетка в которой сидит жаворонок -'), zoo.index('lark'))
