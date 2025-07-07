
try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    r = a / b

except ValueError as e:
    print(f'Erro de valor: {e}')  # Ex: tentar converter uma string não numérica em int
except TypeError as e:
    print(f'Erro de tipo: {e}')  # Ex: somar string com inteiro
except IndexError as e:
    print(f'Erro de índice: {e}')  # Ex: acessar um índice inexistente em uma lista
except KeyError as e:
    print(f'Erro de chave: {e}')  # Ex: acessar uma chave inexistente em um dicionário
except ZeroDivisionError as e:
    print(f'Erro de divisão por zero: {e}')  # Ex: dividir número por zero
except FileNotFoundError as e:
    print(f'Erro de arquivo não encontrado: {e}')  # Ex: abrir um arquivo inexistente
except PermissionError as e:
    print(f'Sem permissão para acessar o recurso: {e}')
except AttributeError as e:
    print(f'Erro de atributo: {e}')  # Ex: acessar método inexistente de um objeto
except ImportError as e:
    print(f'Erro ao importar módulo: {e}')
except NameError as e:
    print(f'Erro de nome (variável não definida): {e}')
except IndentationError as e:
    print(f'Erro de identação: {e}')  # normalmente identificado em tempo de compilação
except SyntaxError as e:
    print(f'Erro de sintaxe: {e}')  # idem acima
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')

else:
    print(f'Resultado = {r}')
finally:
    print('Volte Sempre!!')

#############################################################
# except (ValueError, TypeError) as erro:
#     print(f'Tivemos um erro com os dados digitados = {erro.__class__}')
# except ZeroDivisionError:
#     print('Não é possivel fazer divisao por zero')
# except KeyboardInterrupt:
#     print('Dados não digitados')
# else:
#     print(f'Resultado = {r}')
# finally:
#     print('Volte Sempre!!')