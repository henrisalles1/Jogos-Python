def jogar():
    import random
    
    print('********************************')
    print('Bem vindo ao Jogo de Adivinhacao')
    print('********************************')
    
    print('')
    print('Defina um nivel de dificuldade:')
    print('[1]-Facil [2]-Medio [3]-Dificil')
    print('')
    
    nivel = int(input('Defina o nivel:'))
    
    if (nivel == 1):
        total_de_tentativas = 15
        pontos = 500
    elif (nivel == 2):
        total_de_tentativas = 10
        pontos = 1000
    elif (nivel == 3):
        total_de_tentativas = 5
        pontos = 2000
    
    numero_secreto = round(random.randrange(1, 101))
    pontos_perdidos = 50
    
    for tentativas in range(0, total_de_tentativas):
        print('')
        print('tentativa {} de {}'.format(tentativas, total_de_tentativas))
        print('')
        chute = input("Digite um numero entre 1 e 100: ")
        numero = int(chute)
    
        if (numero < 1 or numero > 100):
            print('')
            print('Voce deve digitar um numero entre 1 e 100!')
            continue
    
        print('')
        print('Voce digitou ', numero)
        print('')
    
        acertou = numero == numero_secreto
        menor = numero < numero_secreto
        maior = numero > numero_secreto
    
        if (acertou):
            print('')
            print('**************')
            print('Voce acertou!!')
            print('**************')
            print('')
            print('SCORE: ', pontos)
            break
        
        else:
            pontos -= pontos_perdidos
        if (menor):
            print('Dica: O numero e maior!')
        elif (maior):
            print('Dica: O numero e menor!')
    
    print('')
    print('___________FIM_DE_JOGO__________')

if(__name__ == '__main__'):
    jogar()
