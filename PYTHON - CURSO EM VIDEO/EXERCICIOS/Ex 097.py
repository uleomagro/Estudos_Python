# Metodo 1
#def escreva(*txt):
    #print('~' * tamanho_linha)
    #print(texto.center(tamanho_linha))
    #print('~' * tamanho_linha)

#texto = str(input('Digite uma frase: '))
#tamanho_linha = len(texto) + 2
#escrev(texto)


# Metodo 2
def escreva(txt):
    tamanho_linha = len(txt) + 4
    print('~' * tamanho_linha)
    print(txt.center(tamanho_linha))  # Os dois dao certo
    print(f'  {txt}')                 # Os dois dao certo
    print('~' * tamanho_linha)

escreva('OUDRICANDELARAI')
escreva('CURSO DE PYTHON NO YOUTUBE')
escreva('CeV')