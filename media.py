n1 = float(input('Digite uma nota  : '))
n2 = float(input('Digite mais uma nota : '))
media = (n1 + n2) / 2
print(f'Sua MEDIA FINAL é {media}')
if media == 10:
    print('APROVADO COM NOTA MAXIMA !!! O maluco é BRABO haha')
elif media >= 7:
    print('APROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
