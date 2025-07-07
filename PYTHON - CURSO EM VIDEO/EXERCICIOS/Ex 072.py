print('='*80)

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
        'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
          'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  escolha = int(input('Digite um número de 0 a 20: '))
  while escolha < 0 or escolha > 20:
      escolha = int(input('Número invalido, favor escolher um número entre 0 a 20: '))

  print(f'Você digitou: {num[escolha]}')

  while True:
     continuar = input('Deseja continuar? S/N: ').upper().strip()
     if continuar in ('S', 'N'):
        break
     else:
        print('Resposta invalida, digite somente S ou N')

  if continuar == 'N':
     print('FIM')
     break      

