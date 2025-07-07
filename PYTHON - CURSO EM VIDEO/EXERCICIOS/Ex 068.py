import random

print('='*40, end='')
print('PAR OU IMPAR', end='')
print('='*40)

jogador = 0
pc = 0
vitorias = 0

while True:
    escolha = input('Escolha Par(P) ou Impar(I): ').strip().upper()
    while escolha not in ('P', 'I'): #ReCHAT
        escolha = input('Opção inválida. Escolha Par(P) ou Impar(I): ').upper().strip()
    jogador = int(input('Digite seu valor: '))
    print('A maquina escolheu um numero....')
    pc = random.randint(0, 10)
    soma = (jogador+pc)
    print(f'A soma dos dois números é igual a: {soma}')
    if escolha == 'P' and soma % 2 == 0:
        print('VITORIA, vamos denovo...')
        vitorias += 1
    elif escolha == 'I' and soma % 2 == 1:
        print('VITORIA, vamos denovo...')       
        vitorias += 1
    else:
        print('O jogador perdeu...')
        break

print(f'O Jogador teve {vitorias} vitória(s) consecutiva(s).')
print('FIM')
print('=' * 80)