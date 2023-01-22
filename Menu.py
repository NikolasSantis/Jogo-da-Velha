from Multiplayer.PvP import *
from Solo.PvC import *
from os import system

system("clear")
print('--'*20)
print(f'{"MENU JOGO DA VELHA".center(40)}')
print('--'*20)
print(f'{"Modos de Jogo:".center(40)}')
modosDeJogo = ['Player vs Player', 'Player vs CPU', 'Sair do Jogo']
for c in range(0, 3):
    print(f'{c+1}° {modosDeJogo[c]}')
print('--'*20)
while True:
    try:
        modoEscolhido = int(input('Modo de jogo escolhido: '))
    except (ValueError, TypeError):
        print('Erro! Digite um número inteiro')
    else:
        if modoEscolhido < 1 or modoEscolhido > 3:
            print('Erro! Insira números de 1 a 3')
        else:
            break
if modoEscolhido == 1:
    VersusPlayer()
elif modoEscolhido == 2:
    VersusCpu()
print('=='*20)
print(f'{"SAINDO DO JOGO".center(40)}')
print('=='*20)