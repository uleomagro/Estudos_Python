from colorama import Fore, Back, Style

while True:
    # Título principal
    frase1 = '  SISTEMA DE AJUDA PyHELP  '
    linha1 = '~' * len(frase1)
    print(f'{Back.GREEN}{linha1}{Style.RESET_ALL}')
    print(f'{Back.GREEN}{frase1}{Style.RESET_ALL}')
    print(f'{Back.GREEN}{linha1}{Style.RESET_ALL}')

    # Entrada do usuário
    comando = input('Função ou Biblioteca: ')
    print()
    if comando == 'exit':
        break

    # Cabeçalho do comando
    frase2 = f'  Acessando o manual do comando "{comando}"  '
    linha2 = '~' * len(frase2)
    print(f'{Back.CYAN}{linha2}{Style.RESET_ALL}')
    print(f'{Back.CYAN}{frase2}{Style.RESET_ALL}')
    print(f'{Back.CYAN}{linha2}{Style.RESET_ALL}')

    # Mostrar ajuda
    print(f'{Back.WHITE}{Fore.BLACK}')
    help(comando)
    print(Style.RESET_ALL)

frase3 = '  ENCERRANDO A CONSULTA  '
linha3 = '~' * len(frase3)
print(f'{Back.RED}{linha3}{Style.RESET_ALL}')
print(f'{Back.RED}{frase3}{Style.RESET_ALL}')
print(f'{Back.RED}{linha3}{Style.RESET_ALL}')