from time import sleep
import minhas_func as F

while True:
    F.menu_prin()
    opc = int(input('Sua opção: '))
    if opc == 1:
        F.consulta()
    elif opc == 2:
        F.cadastro()
    elif opc == 3:
        print('-'*40 + '\n' + 'FINALIZANDO...'.center(40) + '\n' + '-'*40)
        break
    else:
        print('ERRO! Digite uma opção válida.', flush=True)
        sleep(1)