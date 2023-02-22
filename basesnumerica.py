num = int(input('Digite um número : '))
print(''' Escolha algumas das bases para coversão : 
 [1] BINÁRIO
 [2] OCTAL
 [3] HEXADECIMAL ''')
op = int(input('Sua Opção : '))
if op == 1:
    print('{} Convertido para BINÁRIO fica {} '.format(num, bin(num)))
elif op == 2:
    print('{} Convertido para OCTAL fica {}'.format(num, oct(num)))
elif op == 3:
    print('{} Convertido para HEXADECIMAL fica {} '.format(num, hex(num)))
else:
    print('Opção invalida , tente novamente!')
