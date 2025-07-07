# Funçao
def leiaInt(merda):
    valor = 0
    while True:
        numero_dentro = str(input(merda))
        if numero_dentro.isnumeric():
            valor = numero_dentro
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
    return valor


# Programa Principal
numero_fora = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero_fora}')
