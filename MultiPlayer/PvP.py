import os
os.system("clear")

def vencedor(interface,  controladorDeJogadas):
    '''Verificara se há um vencedor no jogo, será verificado na seguinte sequência:
          Horizontais de cima pra baixo, denominadas como horizontal1, 2 e 3
          Verticais da esquerda para a direita< denominadas como vertical 1, 2 e 3 
          Diagonais em \(1) e /(2) 
       Usando a variável de escopo global "interface" 
       
       OBS: ESSA FUNÇÃO APENAS VERIFICA SE HÁ UM VENCEDOR, A VERIFICAÇÃO DE QUEM É 
       O VENCEDOR ESTARÁ NO FINAL DO CÓDIGO'''

    # Para facilitar a visualixação da verificação
    
    # interface = [
    #   [1,2,3], 
    #   [4,5,6] , 
    #   [7,8,9] ]
     
    # Horizontal 1
    if interface[0][0] == interface[0][1] == interface[0][2]:
        return True
    
    # Horizontal 2
    elif interface[1][0] == interface[1][1] == interface [1][2]:
        return True

    # Horizontal 3
    elif interface[2][0] == interface[2][1] == interface[2][2]:
        return True
    
    # Horixontais já verificadas
    
    # Agora é a vez das verticais

    # Vertical 1 
    elif interface[0][0] == interface[1][0] == interface[2][0]:
        return True
    
    # Vertical 2  
    elif interface[0][1] == interface[1][1] == interface[2][1]:
        return True
    
    # Vertical 3 
    elif interface[0][2] == interface[1][2] == interface[2][2]:
        return True

    # Verticais verificadas 
    
    # Agora é a vez das duas diagonais
    
    # Diaonal 1
    elif interface[0][0] == interface[1][1] == interface[2][2]:
        return True
    
    # Diagonal 2
    elif interface[0][2] == interface [1][1] == interface[2][0]:
        return True

    elif controladorDeJogadas == 9:
        return True

def jogador1(interface):  # X
    print('Jogador 1')
    while True:
        try:
            jogada = int(input('Colocar X na posição: '))
        except (ValueError, TypeError):
            print('Erro! Por Favor digite um valor válido.')
        except KeyboardInterrupt:
            print('Jogo encerrado.')
        else:
            for c in range(0,3):
                for i in range(0,3):
                    if jogada == interface[c][i]:
                        interface[c][i] = 'X'
            break

def jogador2(interface):  # O
    print('Jogador 2')
    while True:
        try:
            jogada = int(input('Colocar O na posição: '))
        except (ValueError, TypeError):
            print('Erro! Por Favor digite um valor válido.')

        except KeyboardInterrupt:
            print('Jogo encerrado.')
        else:
            for c in range(0,3):
                for i in range(0,3):
                    if jogada == interface[c][i]:
                        interface[c][i] = 'O'
            break

def interfaceDoJogo(interface):
    # Interface inicial do jogo
    os.system("clear")
    print('--'*20)
    for c in range(0,3):
        for i in range(0,3):
            print(f'| {interface[c][i]} |',end='')
        print()
        print('-'*15)
    print('--'*20)


def VersusPlayer():

    # Variável com os números das posições do jogo
    interface = [ [1,2,3], [4,5,6] , [7,8,9] ]

    # Repetição para alternar os turnos dos jogadores sendo jogador1 numeros pares e 
    # jogador2 números ímpares
    controladorDeJogadas = 0 
    while True:
        if vencedor(interface, controladorDeJogadas):
            break
        if controladorDeJogadas % 2 == 0:
            interfaceDoJogo(interface)
            jogador1(interface)
        else:
            interfaceDoJogo(interface)
            jogador2(interface)
        controladorDeJogadas += 1


    # Varialvel que retornará uma mensagem de empate caso empate
    draw = False
    if controladorDeJogadas == 10:
        draw = True

    interfaceDoJogo(interface)
    # Verificador do vencedor
    if draw :
        print('=='*21)
        print('EMPATE!!')
        print('=='*21)
    elif controladorDeJogadas % 2 == 0:
        print('=='*21)
        print('O JOGADOR 2 VENCEU!!')
        print('=='*21)
    elif controladorDeJogadas % 2 != 0:
        print('=='*21)
        print('O JOGADOR 1 VENCEU!!')
        print('=='*21)