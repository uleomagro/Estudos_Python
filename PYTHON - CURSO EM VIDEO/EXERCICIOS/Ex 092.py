from datetime import datetime

print('-='*40)
cont_min = 35
ano_atual = datetime.now().year
pessoa = {} # Pessoa se aposenta com 35 anos de contribuição

pessoa['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = ano_atual - ano_nasc
pessoa['CTPS'] = int(input('Número da CTPS (Carteira de Trabalho e Previdência Social),' \
' digite 0 caso não tenha: '))
if pessoa['CTPS'] == 0:
    print('-='*10)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')
    
else:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))

    anos_trabalhados = ano_atual - pessoa['Contratação']
    pessoa['Aposentadoria'] = pessoa['Idade'] + (cont_min - anos_trabalhados)

    print('-='*10)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')



print('-='*10)