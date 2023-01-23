from os import system
from Solo.dificuldades.facil import *
from Solo.dificuldades.dificil import *

# Um passo importante, onde o script irá direcionar o usuário para jogar entre a 
# dificuldade: facil e dificil
def VersusCpu():
    system("clear")
    print('--'*20)
    print('ESCOLHA A DIFICULDADE'.center(40))
    print('--'*20)
    print('1° Fácil'.center(40))
    print('2° Difícil'.center(40))
    print('--'*20)

    # Um input dentro de uma repetição infinita, até que o usuário escolha uma 
    # das dificuldades disponíveis
    while True:
        try:
            dificult = int(input('Dificuldade escolhida: '))
        except (ValueError, TypeError):
            print('Insira números inteiros')
        else:
            if dificult < 1 or dificult > 2:
                print('Insira um valor de dificuldade válido de 1 a 2')
            else:
                break
    
    # Direcionamento entre as dificuldades facil e dificil, sendo 1 para facil e 
    # 2 para dificil
    if dificult == 1:
        facil()
    else:
        dificil()
