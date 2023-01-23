from random import randint, choice
from time import sleep
import os

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

def jogador(interface):
    print('Jogador')
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

def chanceDeVencer(interface, Jogada):
    
    # Essa atribuição é para o controle do bloco de condição, se por exemplo
    # a CPU ainda não jogou é por que ela não teve a chance de ganhar nessa 
    # rodada, sendo assim, iremos apenas impedir que o usuário venca
    Jogada = '.'
    aux = interface.copy()

    # verificar se podemos vencer em alguma coluna
    if Jogada == '.':
        interrupt = False
        for c in range(0, 3):
            coluna = [ interface[0][c], interface[1][c], interface[2][c]]
            if coluna.count('O') == 2:
                for i in range(0, 3):
                    if isinstance(coluna[i], int):
                        Jogada = coluna[i]
                        for z in range(0,3):
                            for x in range(0,3):
                                if interface[z][x] == Jogada:
                                    interface[z][x] = 'O'
                                    interrupt = True
                if interrupt:
                    break
    
    # verificar se podemos vencer em alguma linha
    if Jogada == '.':
        for c in range(0,3):
            if interface[1].count('O') == 2:
                if isinstance(interface[1][c], int):
                    Jogada = interface[1][c]
                    interface[1][c] = 'O'

    # verificar se podemos vencer em alguma diagonal
    if Jogada == '.':
        interrupt = False
        diagonal1 = [ interface[0][0], interface[1][1], interface[2][2] ]
        diagonal2 = [ interface[0][2], interface[1][1], interface[2][0] ]
        
        if diagonal2.count('O') == 2 and diagonal2.count('X') == 0 and Jogada == '.':

            for c in range(0, 3):
                # Laço para a diagonal2
                    if isinstance(diagonal2[c], int):
                        Jogada = diagonal2[c]
                        for z in range(0, 3):
                            for x in range(0 ,3):
                                if interface[z][x] == Jogada:
                                    interface[z][x] = 'O'
                                    interrupt = True
                    if interrupt:
                        break           

        if diagonal1.count('O') == 2  and diagonal1.count('X') == 0 and Jogada == '.':
            if Jogada == '.':
                # Laço para a diagonal1
                for i in range(0, 3):
                    if isinstance(diagonal1[i], int):
                        Jogada = diagonal1[i]
                        for z in range(0, 3):
                            for x in range(0 ,3):
                                if interface[z][x] == Jogada:
                                    interface[z][x] = 'O'
                                    interrupt = True
                    if interrupt:
                        break
    
    for c in range(0, 3):
        if aux[c] == interface[c]:
            Jogada = '.'

    return Jogada

def inicioCanto(interface, controladorDeJogadas):

    """Uma IA específica para quando o usuário iniciar o jogo posicionando um 'X'
    em qualquer canto possivel do jogo (1, 3, 7, 9), e assim iniciaremos um
    contra jogo a partir da melhor estratégia defensiva para esse começo de jogo.
    
    A maioria das estruturas estão focadas em contra atacar com essa estratégia,
    porém, essa estratégia exige que o usuário siga uma sequencia específica de 
    jogadas, mas caso isso ocorra, iremos impedir que o usuário tente vencer 
    com outras jogadas, ou se o próprio usuário fazer uma jogada aleatória,
    iremos fazer uma jogada aleatória.
    
    Em todo caso, se o usuário permitir nossa vitória com alguns erros no jogo
    iremos simplesmente vencer.
        
        Parâmetros:
        
        param 01: interface são as posições do jogo, nela iremos colocar nossos
        'O', e usaremos também verificar qualquer possibilidade de vencer;
        
        param 02: controladorDeJogadas são as jogadas efetuadas pelos jogadores,
        serve para controlar qual verificação de jogadas vamos usar e também
        ajuda a IA a saber quando o jogo empatou. """


    # Essa atribuição é para o controle do bloco de condição, se por exemplo
    # a CPU ainda não jogou é por que ela não teve a chance de ganhar nessa 
    # rodada, sendo assim, iremos apenas impedir que o usuário venca
    Jogada = '.'  


    # Colocaremos o 'O' no meio, pois é a melhor jogada no inicio
    if controladorDeJogadas == 1:
        Jogada = interface[1][1]
        interface[1][1] = 'O'
        
        # Concluído
    
    
    elif controladorDeJogadas == 3:
        
        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        for c in range(0,3):
            if interface[c].count('X') == 2:
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        Jogada = interface[c][i]
                        interface[c][i] = 'O'

        # Se o oponente jogar em cantos opostos
        if interface[0][0] == 'X' and interface[2][2] == 'X' or interface[0][2] == 'X' and interface[2][0] == 'X':
            while True:
                interrupt = False
                v = randint(1,9)
                if v % 2 == 0:
                    for c in range(0,3):
                        for i in range(0,3):
                            if interface[c][i] == v:
                                Jogada = interface[c][i]
                                interface[c][i] = 'O'
                                interrupt = True
                if interrupt:
                    break


        # Se jogar dois X na mesma coluna
        else:
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                  for x in range(0,3):
                                        if interface[z][x] == Jogada:
                                            interface[z][x] = 'O'
                                            interrupt = True
                if interrupt:
                    break
        
        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        # Concluído
    

    elif controladorDeJogadas == 5:
        
        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)

        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if Jogada == '.':
            for c in range(0, 3):
                if interface[c].count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(interface[c][i], int):
                            Jogada = interface[c][i]
                            interface[c][i] = 'O'
                            
        # Se o oponente tentar vencer em uma coluna
        if Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break

        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'

        # Concluído

    elif controladorDeJogadas == 7:  

        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)
        
        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if Jogada == '.':
            for c in range(0,3):
                if interface[c].count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(interface[c][i], int):
                            Jogada = interface[c][i]
                            interface[c][i] = 'O'
                            
        # Se o oponente tentar vencer em uma coluna
        if Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break
        
        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        # Concluído

    print('CPU')
    print(f'A CPU escolheu a posição {Jogada}')
    sleep(3.6)

    #  80% concluído


def inicioCentro(interface, controladorDeJogadas):

    """Uma IA específica para quando o usuário iniciar o jogo posicionando um 'X'
    no centro (5), e assim iniciaremos um contra jogo a partir da melhor estratégia 
    defensiva para esse começo de jogo.
    
    A maioria das estruturas estão focadas em contra atacar com essa estratégia,
    porém, essa estratégia exige que o usuário siga uma sequencia específica de 
    jogadas, mas caso isso ocorra, iremos impedir que o usuário tente vencer 
    com outras jogadas, ou se o próprio usuário fazer uma jogada aleatória,
    iremos fazer uma jogada aleatória.
    
    Em todo caso, se o usuário permitir nossa vitória com alguns erros no jogo
    iremos simplesmente vencer.
        Parâmetros:
        
        param 01: interface são as posições do jogo, nela iremos colocar nossos
        'O', e usaremos também verificar qualquer possibilidade de vencer;
        
        param 02: controladorDeJogadas são as jogadas efetuadas pelos jogadores,
        serve para controlar qual verificação de jogadas vamos usar e também
        ajuda a IA a saber quando o jogo empatou. """


    
    # Essa atribuição é para o controle do bloco de condição, se por exemplo
    # a CPU ainda não jogou é por que ela não teve a chance de ganhar nessa 
    # rodada, sendo assim, iremos apenas impedir que o usuário venca
    Jogada = '.'  
    
    
    # Iniciaremos em um canto e a partir disto, iremos impedir que o usuário vença
    if controladorDeJogadas == 1:
        cantos = [1, 3, 7, 9]
        Jogada = choice(cantos)
        for c in range(0, 3):
            for i in range(0, 3):
                if interface[c][i] == Jogada:
                    interface[c][i] = 'O'
        
        # Concluído
    

    elif controladorDeJogadas == 3:
        
        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if interface[1].count('X') == 2:
            for i in range(0, 3):
                if isinstance(interface[1][i], int):
                    Jogada = interface[1][i]
                    interface[1][i] = 'O'
        
        # Verificando se ele inseriu um 'X' em diagonais, e impediremos de pontuar
        if interface[0][0] == 'X':
            if isinstance(interface[2][2], int):
                Jogada = interface[2][2]
                interface[2][2] = 'O'
        elif interface[0][2] == 'X':
            if isinstance(interface[2][0], int):
                Jogada = interface[2][0]
                interface[2][0] = 'O'
        elif interface[2][0] == 'X':
            if isinstance(interface[0][2], int):
                Jogada = interface[0][2]
                interface[0][2] = 'O'
        elif interface[2][2] == 'X':
            if isinstance(interface[0][0], int):
                Jogada = interface[0][0]
                interface[0][0] = 'O'

        # Verificando se ele inseriu um 'X' em uma borda
        else:
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True

        # Caso não exista chance de vitoria para nenhum dos lados, mas é preciso 
        # jogar para o jogo acabar
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'        
        
        
        # Concluído

    
    elif controladorDeJogadas == 5:

        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)

        # Verificando se ele inseriu um 'X' em diagonais, se sim, impediremos de pontuar
        if interface[0][0] == 'X':
            if isinstance(interface[2][2], int):
                Jogada = interface[2][2]
                interface[2][2] = 'O'
        elif interface[0][2] == 'X':
            if isinstance(interface[2][0], int):
                Jogada = interface[2][0]
                interface[2][0] = 'O'
        elif interface[2][0] == 'X':
            if isinstance(interface[0][2], int):
                Jogada = interface[0][2]
                interface[0][2] = 'O'
        elif interface[2][2] == 'X':
            if isinstance(interface[0][0], int):
                Jogada = interface[0][0]
                interface[0][0] = 'O'

        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if Jogada == '.':
            for c in range(0,3):
                if interface[c].count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(interface[c][i], int):
                            Jogada = interface[c][i]
                            interface[c][i] = 'O'
                            
        # Se o oponente tentar vencer em uma coluna
        if Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break
        
        # Caso não exista chance de vitoria para nenhum dos lados, mas é preciso 
        # jogar para o jogo acabar
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        # Concluído


    elif controladorDeJogadas == 7:  

        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)
        
        # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if Jogada == '.':
            for c in range(0,3):
                if interface[c].count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(interface[c][i], int):
                            Jogada = interface[c][i]
                            interface[c][i] = 'O'
                            
        # Se o oponente tentar vencer em uma coluna
        if Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break
        
        # Caso não exista chance de vitoria para nenhum dos lados, mas é preciso 
        # jogar para o jogo acabar
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        # Concluído

    print('CPU')
    print(f'A CPU escolheu a posição {Jogada}')
    sleep(3.6)

    # 80% cocluído


def inicioBorda(interface, controladorDeJogadas):

    """Uma IA específica para quando o usuário iniciar o jogo posicionando um 'X'
    em qualquer borda possivel do jogo (2, 4, 6, 9), e assim iniciaremos um
    contra jogo a partir da melhor estratégia defensiva para esse começo de jogo.
    
    A maioria das estruturas estão focadas em contra atacar com essa estratégia,
    porém, essa estratégia exige que o usuário siga uma sequencia específica de 
    jogadas, mas caso isso ocorra, iremos impedir que o usuário tente vencer 
    com outras jogadas, ou se o próprio usuário fazer uma jogada aleatória,
    iremos fazer uma jogada aleatória.
    
    Em todo caso, se o usuário permitir nossa vitória com alguns erros no jogo
    iremos simplesmente vencer.
        Parâmetros:
        
        param 01: interface são as posições do jogo, nela iremos colocar nossos
        'O', e usaremos também verificar qualquer possibilidade de vencer;
        
        param 02: controladorDeJogadas são as jogadas efetuadas pelos jogadores,
        serve para controlar qual verificação de jogadas vamos usar e também
        ajuda a IA a saber quando o jogo empatou. """


    # Essa atribuição é para o controle do bloco de condição, se por exemplo
    # a CPU ainda não jogou é por que ela não teve a chance de ganhar nessa 
    # rodada, sendo assim, iremos apenas impedir que o usuário venca
    Jogada = '.'


    # iniciaremos jogando no centro
    if controladorDeJogadas == 1:
        Jogada = interface[1][1]
        interface[1][1] = 'O'
     
        # Concluído


    elif controladorDeJogadas == 3:
        
        # Se o oponente fazer uma lina 'X-O-X' no centro ou em uma coluna,
        # iremos jogar um 'O' em um canto aleatório
        
        if interface[1].count('X') == 2:
            cantos = [ 1, 3, 7, 9 ]
            Jogada = choice(cantos)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        elif Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break
        
        # Se ocorrer de o oponente jogar em 2 adjacentes para tentar vencer
        if Jogada == '.':
            bordas = [interface[0][1], interface[1][0], interface[1][2], interface[2][0]]
            if bordas[0]=='X' and bordas[1] =='X':
                Jogada = interface[0][0]
                interface[0][0] = 'O'
            elif bordas[2] == 'X' and bordas[3] == 'X':
                Jogada = interface[2][2]
                interface[2][2] = 'O'
        
        if Jogada == '.':
            defesa_1 = [ interface[0][1], interface[2][0], interface[2][2] ]
            defesa_2 = [ interface[1][0], interface[0][2], interface[2][2] ]
            defesa_3 = [ interface[1][2], interface[0][0], interface[2][0] ]
            defesa_4 = [ interface[2][1], interface[0][0], interface[0][2] ]

            if defesa_1[1] == 'X':
                Jogada = interface[0][0]
                interface[0][0] = 'O'
            elif defesa_1[2] == 'X':
                Jogada = interface[0][2]
                interface[0][2] = 'O'
            
            elif defesa_2[1] == 'X':
                Jogada = interface[0][0]
                interface[0][0] = 'O'
            elif defesa_2[2] == 'X':
                Jogada = interface[2][0]
            
            elif defesa_3[1] == 'X':
                Jogada = interface[0][2]
                interface[0][2] = 'O'
            elif defesa_3[2] == 'X':
                Jogada = interface[2][2]
                interface[2][2] = 'O'
            
            elif defesa_4[1] == 'X':
                Jogada = interface[2][0]
                interface[2][0] = 'O'
            elif defesa_4[2] == 'X':
                Jogada = interface[2][2]
                interface[2][2] = 'O'

        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        
        # Estratégia Concluída


    elif controladorDeJogadas == 5:

        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)

         # Se o oponente tentar fazer uma linha na horizontal, impediremos
        if Jogada == '.':
            for c in range(0, 3):
                if interface[c].count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(interface[c][i], int):
                            Jogada = interface[c][i]
                            interface[c][i] = 'O'
                            
        # Se o oponente tentar vencer em uma coluna
        if Jogada == '.':
            interrupt = False
            for c in range(0, 3):
                coluna = [ interface[0][c], interface[1][c], interface[2][c]]
                if coluna.count('X') == 2:
                    for i in range(0, 3):
                        if isinstance(coluna[i], int):
                            Jogada = coluna[i]
                            for z in range(0,3):
                                for x in range(0,3):
                                    if interface[z][x] == Jogada:
                                        interface[z][x] = 'O'
                                        interrupt = True
                if interrupt:
                    break

        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'

        # Estratégia Concluída


    elif controladorDeJogadas == 7:

        # Se tivermos chance de vencer 
        Jogada = chanceDeVencer(interface, Jogada)

        # Se não ocorrer nenhuma das opções anteriores
        if Jogada == '.':
            lacunas = []
            for c in range(0, 3):
                for i in range(0, 3):
                    if isinstance(interface[c][i], int):
                        lacunas.append(interface[c][i])
            Jogada = choice(lacunas)
            for c in range(0, 3):
                for i in range(0, 3):
                    if interface[c][i] == Jogada:
                        interface[c][i] = 'O'
        

    print('CPU')
    print(f'A CPU escoleu a posição {Jogada}')
    sleep(3.6)

    # 80% concluído


def interfaceDoJogo(interface):

    """Uma função simples, serve apenas para a ilustração do jogo
        Parâmetros:
        param 01: interface é uma lista composta por 3 listas, cada uma dessas
        pequenas listas é uma linha do jogo, é uma várivel que possui os dados
        do jogo"""


    # Interface inicial do jogo
    os.system("clear")
    print('--'*20)
    for c in range(0,3):
        for i in range(0,3):
            print(f'| {interface[c][i]} |'.center(40),end='')
        print()
        print('-'*15)
    print('--'*20)


def dificil():

    """Como se fosse o programa principal, essa função chama todas as outras
    funções, é uma espécie de 'Gerenciador' do jogo em si.
        Não recebe parametro, afinal, é dessa função que o jogo se inicia."""

    # Variável com os números das posições do jogo
    interface = [ [1,2,3], [4,5,6] , [7,8,9] ]

    # Repetição para alternar os turnos dos jogadores sendo jogador1 numeros pares e 
    # jogador2 números ímpares
    controladorDeJogadas = 0 
    estrategia = ''
    while True:
        if vencedor(interface, controladorDeJogadas):
            break
        if controladorDeJogadas % 2 == 0:
            interfaceDoJogo(interface)
            jogador(interface)
        else:
            interfaceDoJogo(interface)
            if controladorDeJogadas == 1:
                if interface[0][0] == 'X' or interface[0][2] == 'X' or interface[2][0] == 'X' or interface[2][2] == 'X':
                    estrategia = 'Canto'
                elif interface[1][1] == 'X':
                    estrategia = 'Centro'
                else:
                    estrategia = 'Borda'
            if estrategia == 'Canto':
                inicioCanto(interface, controladorDeJogadas)
            elif estrategia == 'Centro':
                inicioCentro(interface, controladorDeJogadas)
            elif estrategia == 'Borda':
                inicioBorda(interface, controladorDeJogadas)
        controladorDeJogadas += 1
    
    # Varialvel que retornará uma mensagem de empate caso empate
    draw = False
    if controladorDeJogadas == 9:
        draw = True

    interfaceDoJogo(interface)
    # Verificador do vencedor
    if draw :
        print('=='*21)
        print('EMPATE!!'.center(40))
        print('=='*21)
    elif controladorDeJogadas % 2 == 0:
        print('=='*21)
        print('DERROTA'.center(40))
        print('=='*21)
    elif controladorDeJogadas % 2 != 0:
        print('=='*21)
        print('VITÓRIA!!'.center(40))
        print('=='*21)
