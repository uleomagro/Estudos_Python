def maior(*parametros):
    print('-='*20)
    print('Analisando os valores passados...')
    if not parametros:
        print(f'Nenhum valor informado.')
        print(f'FINALIZANDO')
        print('-='*20)
    else:
        for num in parametros:
            print(num, end=' ')
        print(f'Foram informados {len(parametros)} valores ao todo.')
        print(f'O maior valor informado foi {max(parametros)}')
        

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
