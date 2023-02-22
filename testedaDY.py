from time import sleep

cora = 'sim'
while cora and 'sim':
    cora = str(input('Dy vc me AMA ? : ')).upper()
    print(cora)

    if cora == 'NÃO':
        print('DY???Acho que vc digitou errado... ,tenta de novo depois do tempo')
        for cont in range(10, -1, -1):
            print(cont)
            sleep(1.5)
        print('Agora digita certo,Pra de graça ksksksk')

    elif cora == 'SIM':
        print('Também te AMO meu amor!!!Minha Linda,Obrigado por me apresentar PROGRAMAÇÃO')
        break
