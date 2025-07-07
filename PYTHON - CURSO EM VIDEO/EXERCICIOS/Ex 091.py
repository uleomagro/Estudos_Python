import random
import time
import operator

players = {}
players['Jogador 1'] = random.randint(1, 6)
players['Jogador 2'] = random.randint(1, 6)
players['Jogador 3'] = random.randint(1, 6)
players['Jogador 4'] = random.randint(1, 6)

print(f"{'DADOS SENDO ROLADOS':-^40}")

for k, v in players.items():
    print(f'  -  O {k} tirou: {v}')
    time.sleep(1)

print(f"{'RANKING':-^40}")
ranking = []
ranking = sorted(players.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  -  O {i+1}° foi o {v[0]} que tirou {v[1]}'),
    time.sleep(1)
 


print('-='*20)

