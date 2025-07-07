from time import sleep

ARQUIVO = 'ULTIMO_EX_115/pessoas.txt'

def menu_prin():
    print('-'*40 + '\n' + 'MENU PRINCIPAL'.center(40) + '\n' + '-'*40)
    print('1  -  Ver Pessoas Cadastradas'
           + '\n' + '2  -  Cadastrar nova Pessoa'
           + '\n' + '3  -  Sair do Sistema' + '\n' + '-'*40)
    sleep(1)


def consulta():
    print('='*40 + '\n' + 'Pessoas Cadastradas'.center(40) + '\n' + '='*40)
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma pessoa cadastrada ainda.')
            else:
                for linha in linhas:
                    nome, idade = linha.strip().split(';')
                    print(f'{nome:<20}{idade:>15} anos')

    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada ainda.')
    
    print('='*40)
    sleep(1)


def cadastro():
    print('='*40 + '\n' + 'NOVO CADASTRO'.center(40) + '\n' + '='*40)
    nome = str(input('Nome: '))
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Idade invalida! Digite um número inteiro.')
            sleep(1)

    try:
        with open(ARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado')
    except Exception as e:
        print(f'Erro a cadastrar: {e}')
        sleep(1)

