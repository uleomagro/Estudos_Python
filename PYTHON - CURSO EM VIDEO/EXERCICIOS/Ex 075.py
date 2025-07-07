print('='*80)

tp = ()

for c in range(4):      
    n1 = int(input('Digite um valor: '))
    tp += (n1,)

print(f'Os valores digitados foram: {tp}')

nove = tp.count(9)
print(f'O numero 9 aparece {nove} vezes.') #PARTE A

if 3 in tp:  #PARTE B
    tres = tp.index(3) + 1
    print(f'O primeiro valor 3 foi digitado na posicao: {tres}')
else:
    print(f'Nao foi digitado o valor 3 em nenhum momento.')

lista = ()
for numeros in tp:   #PARTE C
    if numeros % 2 == 0:
        lista += (numeros,)
        
if not lista:
    print('Nenhum numero par digitado')
else: 
    print(f'Os numeros pares sao: {lista}')

print('FIM')