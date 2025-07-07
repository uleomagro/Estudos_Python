print('=-'*20)
print(f"{'APROVADO / REPROVADO':-^40}")
print('=-'*20)

aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Qual a média de {aluno['nome']}: '))

print(f'O nome é {aluno["nome"]}')
print(f'A media é {aluno["media"]}')

if aluno['media'] > 6:
    print(f'Situação: APROVADO(A)')
else:
    print(f'Situação: REPROVADO(A)')

print('=-'*20)
print(f"{'APROVADO / REPROVADO':-^40}")
print('=-'*20)