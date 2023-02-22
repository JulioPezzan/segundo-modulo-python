casa = float(input('Qual é o valor da casa ? : '))
salario = float(input('Qual é o seu salario atual ? : '))
tempo = int(input('Em quanto tempo vc pretende pagar ? : '))
mensal = casa / 12
print(f'{casa} {salario} {tempo} {mensal}')
if mensal > (30 * salario) / 100:
    print('Credito NÃO autorizado')
elif salario == 0:
    print('Credito NÃO Autorizado')
else:
    print('Credito Autorizado')
