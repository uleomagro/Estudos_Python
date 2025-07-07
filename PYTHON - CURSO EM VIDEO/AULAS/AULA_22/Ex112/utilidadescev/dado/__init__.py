def leiaDinheiro(msg):
    valido = False
    while valido == False:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" nao e um numero.\033[m')          
        else:
            valido = True
            return float(entrada)
            
