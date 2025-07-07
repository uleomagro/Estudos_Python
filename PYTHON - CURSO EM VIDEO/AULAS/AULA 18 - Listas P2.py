#teste = []
#teste.append('Leonardo')
#teste.append(25)
#galera = []
#galera.append(teste[:])
#teste[0] = 'Vitoria'
#teste[1] = 21
#galera.append(teste[:])
#print(galera)

#galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][0])

#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')

galera = []
dado = []
totmai = totmen = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(galera)
