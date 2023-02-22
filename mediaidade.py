soma = 0
for c in range(0, 2):
    nome = str(input('NOME : ')).strip()
    idade = int(input('IDADE : '))
    sexo = str(input('SEXO [M/F] : ')).strip()
    print(f'Seu  nome é {nome} , vc tem {idade} anos de idade e seu sexo é {sexo} ')
    soma = soma + idade
media = soma / 4
print(f'A média de idade do grupo é {media} anos de idade')
