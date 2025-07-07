print('=' * 80)

num = 0

#num = int(input('Gostaria de ver a tabuada de qual valor: '))

while num >= 0:
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
    num = int(input('Gostaria de ver a tabuada de qual valor: '))


print('FIM')
print('=' * 80)