from os import system
from Solo.dificuldades.facil import *
from Solo.dificuldades.dificil import *

def VersusCpu():
    system("clear")
    print('--'*20)
    print(f'{"ESCOLHA A DIFICULDADE".center(40)}')
    print('--'*20)
    print('1° Fácil')
    print('2° Difícil')
    print('--'*20)
    while True:
        try:
            dificult = int(input('Dificuldade escolhida: '))
        except (ValueError, TypeError):
            print('Insira números inteiros')
        else:
            if dificult < 1 or dificult > 2:
                print('Insira um valor de dificuldade válido de 1 a 3')
            else:
                break
    if dificult == 1:
        facil()
    else:
        dificil()
