    #Trazendo os arquivos dos jogos
import forca
import adivinhacao

def escolhe_jogo():
    print('********************************')
    print('******* Escolha um Jogo: *******')
    print('********************************')
    print('')
    print('[1]-Adivinhação [2]-Forca')
    print('')

    jogo = int(input('Escolha seu Jogo:'))

    if (jogo == 1):
        print('Jogando Adivinhação !')
        print('')
        adivinhacao.jogar()
    elif(jogo == 2):
        print('Jogando Forca !')
        print('')
        forca.jogar() # ativa funcao jogar() do arquivo forca.py

#Tornando o arquivo atual Independente
if(__name__ == '__main__'):
    escolhe_jogo()

