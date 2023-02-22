resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    soma = soma + num
    quant = quant + 1

    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Vc digitou {quant} números e a média foi {media} ')
