print('=-='*25)

lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    # Continuar?
    while True:
        cont = input('Deseja continuar [S/N]: ').upper().strip()
        if cont in ('S', 'N'):
            break
        print('Resposta inválida. Digite apenas S ou N.')

    if cont == 'N':
        break
            
# A
quantidade = len(lista)
print(f'Foram digitados {quantidade} valores')

# B
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')

# C
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi digitado')

print('-=-'*25)