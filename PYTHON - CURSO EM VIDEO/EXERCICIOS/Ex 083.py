print('-='*20)

abre = 0
fecha = 0

pergunta = str(input('Digite algo: '))

for i in pergunta:
    if '(' in i:
        abre += 1
for i in pergunta:
    if ')' in i:
        fecha += 1

if abre == fecha:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida')

print('='*25)