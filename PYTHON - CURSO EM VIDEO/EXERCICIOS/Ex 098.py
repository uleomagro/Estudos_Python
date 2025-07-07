import time

print('Contagem de 1 até 10 de 1 em 1')
for contagem_positiva in range(1, 11):
    print(f'{contagem_positiva}', end=' ', flush=True)
    time.sleep(0.5)
print()

print('Contagem de 10 até 0 de 2 em 2')
for contagem_negativa in range(10, -1, -2):
    print(f'{contagem_negativa}', end=' ', flush=True)
    time.sleep(0.5)
print()

# Contagem personalizada
def contador():
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        passo = 1

    if inicio < fim and passo < 0:
        passo = -passo
    elif inicio > fim and passo > 0:
        passo = -passo    

    if passo > 0:
        fim += 1
    else:
        fim -= 1

    for contagem in range(inicio, fim, passo):
        print(f'{contagem}', end=' ', flush=True)
        time.sleep(0.5)
    print()

contador()