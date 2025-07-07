# Funçao
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print('\r\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número Real valido.\033[m')
        except (KeyboardInterrupt):
            print('\r\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n

# Programa Principal
numero_int = leiaInt('Digite um número Inteiro: ')
numero_real = leiaReal('Digite um número Real: ')
print(f'O valor inteiro foi {numero_int} e o real foi {numero_real}')
