print('-='*20)
filme = {'titulo':'Star Wars',
         'ano':1997,
         'diretor':'George Lucas'}

print(filme.values()) # Valores
print(filme.keys()) # Chaves
print(filme.items()) # Ambos

for k, v in filme.items():
    print(f'O {k} é {v}')
print('-='*20)

pessoas = {'nome': 'Leonardo', 'sexo': 'M', 'idade': 25}
print(pessoas)
print(f'{pessoas['nome']:^20}')
print(f'{pessoas['sexo']:^20}')
print(f'{pessoas['idade']:^20}')
print('-='*20)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print('-='*20)
pessoas['nome'] = 'Teste'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*20)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

print('-='*20)