from Multiplayer.PvP import *
from Solo.PvC import *
from os import system

# O jogo inteiro começa aqui, portanto, neste ponto inicial é escolhido 
# o importante Modo de Jogo

# começo da tela
system("clear")
print('--'*20)
print('MENU JOGO DA VELHA'.center(40))
print('--'*20)
print('Modos de Jogo:'.center(40))
modosDeJogo = ['Player vs Player', 'Player vs CPU', 'Sair do Jogo']

# irá escrever os modos de jogo 
for c in range(0, 3):

    # possui uma formatação especifica para melheor interface no console
    print(f'{c+1}° {modosDeJogo[c]}')
print('--'*20)

# Um input do modo escolhido dentro de uma estrutura de tratemento de exceções e 
# eventuais erros de digitação do usuário
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

# irá direcionar o modo de jogo, sendo 1 PlayerVsPlayer, 2 PlayerVsCpu e 
# o modo  "3" é apenas para não jogar nada e sair do script
if modoEscolhido == 1:
    VersusPlayer()
elif modoEscolhido == 2:
    VersusCpu()

# é importante ressaltar que o modo 3 está em condicional, pois nos módulos do 
# jogo já exite uma tela final de "VITÓRIA", "DERROTA" e "EMPATE"
else:
    print('=='*20)
    print('SAINDO DO JOGO'.center(40))
    print('=='*20)