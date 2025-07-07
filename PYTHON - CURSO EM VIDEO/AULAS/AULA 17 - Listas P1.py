lista = ['lanche', 'Suco', 'Pizza', 'Pudim']

lista.append('cokkie')
lista.insert(0, 'cahorro quente')

#del lista[3]
#lista.pop[3] #Normalmente usado para o ultimo elemento
if 'Pizza' in lista:
    lista.remove('Pizza') #Remove pelo nome
lista.pop()

print(lista)
print('='*80)

valores = list(range(4, 11))

valores.sort()
print(valores)

valores.sort(reverse=True)
print(valores)

print(len(valores))