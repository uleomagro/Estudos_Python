boletim = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    while True:
        continuar = input("Quer continuar? [S/N] ").upper()
        if continuar == 'S':
            break # Sai apenas do loop de validação
        elif continuar == 'N':
            break
        else:
            print('Entrada invalida')
    if continuar == 'N':
        break

print("\nBoletim:")
print(f"{'No.':<4} {'Nome':<10} {'Média':>6}")
for i, aluno in enumerate(boletim):
    print(f"{i:<4} {aluno[0]:<10} {aluno[2]:>6.1f}")

# Consulta de notas individuais
while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para sair): "))
    if opcao == 999:
        break
    if 0 <= opcao < len(boletim):
        print(f"Notas de {boletim[opcao][0]}: {boletim[opcao][1]}")
