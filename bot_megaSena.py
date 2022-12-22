import random




def gera_numero_sena(jogos):

    contador_jogo = 1
    contador = 0
    lista = []
    lista2 = []


    while True:

        numero = random.randint(1,60)

        if contador < 6: 
            if not numero in lista:
                lista.append(numero)
                contador +=1
            else:
                continue
        
        else:
            lista2.append(lista)
            print('JOGO'+ str(contador_jogo) + '--> ' + str(lista))
            contador_jogo += 1
            contador = 0
            lista = []

        if contador_jogo > jogos:
            break





if __name__ == '__main__':

    while True:

        print('\n\n\n')

        jogos = int(input('QUANTOS JOGOS DESEJA GERAR? ----- '))

        print('\n\n\n')

        gera_numero_sena(jogos)

        print('\n\n\n')

        continuar = input('DESEJA GERAR OUTRA SEQUENCIA? (S/N) ---- ')

        if continuar == 'S' or continuar =='s':
            continue

        else:
            print('\n\n\n')
            print(' BOA SORTE!!! ')
            break



