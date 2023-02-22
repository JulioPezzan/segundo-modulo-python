n1 = int(input('Digite um número : '))
n2 = int(input('Digite mais um número : '))
print('[1]SOMAR')
print('[2]MULTIPLICAR')
print('[3]MAIOR')
print('[4]NOVOS NÚMEROS')
print('[5]SAIR DO PROGRAMA')
print(f'Digite a função que vc gostaria de realizar no número {n1} e {n2} : ')
d = float(input('Digite a função : '))
if d == 1:
    s = n1 + n2
    print(f'A soma é {s}')
elif d == 2:
    m = n1 * n2
    print(f'A multiplicação entre os números é {m}')
elif d == 3:
    if n1 > n2:
        print(f'O maior valor é {n1} ')
    else:
        print(f'O maior valor é {n2} ')
elif d == 4:
    n1 = int(input('Digite um número : '))
    n2 = int(input('Digite mais um número : '))
    print('[1]SOMAR')
    print('[2]MULTIPLICAR')
    print('[3]MAIOR')
    print('[4]NOVOS NÚMEROS')
    print('[5]SAIR DO PROGRAMA')
    print(f'Digite a função que vc gostaria de realizar no número {n1} e {n2} : ')
    d = float(input('Digite a função : '))
elif d == 5:
    print('TCHAU')
