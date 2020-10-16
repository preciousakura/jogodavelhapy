def matriz(linhas, colunas, val_inic): #Criar matriz
    mat = [[val_inic] * colunas for _ in range(linhas)]
    return mat #retorna a matriz


def mostrar_tabuleiro(matriz): #mostra o tabuleiro atualizado
    jogada = 0
    print("\n------ TABULEIRO ------\n")
    print("  A   B   C")
    for linha in range(len(matriz)):
        print(linha+1, end='')
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] == -1:
                jogada = " "
            elif matriz[linha][coluna]:
                jogada = "X"
            else:
                jogada = "O"
                
            if coluna != 2: #if para não mostrar o | depois do valor ultima coluna
                print("{:^3}".format(jogada), end='|') 
            else:
                print("{:^3}".format(jogada), end='') 
                
        print(linha+1)
        if linha!=2: #if para não mostrar o " ---+---+---" depois da ultima linha
            print(" ---+---+---")
    print("  A   B   C")

def definir_jogadores(nomePlay1,nomePlay2): #define a peça que o jogo vai começar e a retorna
    peca = input("Escolha a peça, "+nomePlay1+" [X/O]: ").upper()

    while peca != "X" and peca != "O":
        peca = input("Peça inválida! Escolha a peça, jogador 1 [X/O]: ").upper()

    if peca == "X":
        jogador1 = True
        print("\n"+nomePlay1+": X\n"+nomePlay2+": O")
    else:
        jogador1 = False
        print("\n"+nomePlay1+": O\n"+nomePlay2+": X")

    return jogador1

def verificar_jogada(jogada, matriz): #verifica se a entrada do usuario está de acordo com os criterios pedidos
    validar = True
    while validar: #enquanto a entrada não estiver de acordo, será pedida uma nova
        virgula = 0
        entrada = []
        for x in jogada: 
            if x != " " and x!=",":
                entrada.append(x)
            if x == ",":
                virgula += 1   
        if len(entrada) != 2 or virgula > 1: #pede uma nova se a entrada tiver mais que 2 valores, no caso a letra(coluna) e o numero(linha)
            jogada = input("Jogada Inválida! Digite novamente [LETRA,NUMERO]: ").upper()
        else:
            coluna = entrada[0]
            linha = entrada[1]

            if coluna not in "ABC" or linha not in "123": #pede uma nova entrada se o usuario digitar valores inválidos
                jogada = input("Jogada Inválida! Digite novamente [LETRA,NUMERO]: ").upper()
            else:
                linha = int(linha)
                if coluna == "A":
                    coluna = 0
                elif coluna == "B":
                    coluna = 1
                else:
                    coluna = 2
                
                if matriz[linha-1][coluna] != -1: #pede uma nova entrada se o usuario jogar uma jogada já feita
                    jogada = input("Você já fez essa jogada! Digite outra [LETRA,NUMERO]: ").upper()
                else:
                    return linha-1, coluna
                    validar = False

def fazer_jogada(linha, coluna, peca_atual, matriz): #atualiza a matriz com a jogada
    matriz[linha][coluna] = peca_atual

def ganhar(matriz, linha, coluna, jogada_atual): #verifica se o usuario atual ganhou 
    l = 0
    c = 0
    diagonal = 0
    diagonal_secundaria = 0
    cont = 2

    for x in range(3):
        #checa linha
        if matriz[linha][x] == jogada_atual: 
            l += 1
        #checa coluna
        if matriz[x][coluna] == jogada_atual:
            c += 1
        #checa diagonal principal
        if matriz[x][x] == jogada_atual:
            diagonal += 1
        #chega diagonal secundária
        if matriz[cont][x] == jogada_atual:
            diagonal_secundaria += 1
        cont -= 1


    if l == 3 or c == 3 or diagonal == 3 or diagonal_secundaria == 3:
        return True
    return False

def possibilidades(matriz, jogada_atual): #função que comunica ao usuário que está na iminência de jogar que ele já perdeu a rodada
    possibilidades = 0
    checar = 0

    #checar linhas
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == jogada_atual:
                checar += 1
            elif matriz[i][j] != -1 and matriz[i][j] != jogada_atual:
                checar -= 1

        if checar>1:
            possibilidades += 1
        checar = 0
    
    #checar colunas
    for i in range(3):
        for j in range(3):
            if matriz[j][i] == jogada_atual:
                checar += 1
            elif matriz[j][i] != -1 and matriz[j][i] != jogada_atual:
                checar -= 1

        if checar>1:
            possibilidades += 1
        checar = 0

    #checar diagonal principal
    for i in range(3):
        if matriz[i][i] == jogada_atual:
            checar += 1
        elif matriz[i][i] != -1 and matriz[i][i] != jogada_atual:
            checar -= 1   

    if checar>1:
        possibilidades += 1 
    checar = 0

    #checar diagonal secundaria
    dg = 2
    for i in range(3):
        if matriz[i][dg] == jogada_atual:
            checar += 1
        elif matriz[i][dg] != -1 and matriz[i][dg] != jogada_atual:
            checar -= 1   
            dg -= 1 

    if checar>1:
        possibilidades += 1    

    if possibilidades > 1: 
        return True
    return False      

def rodar_jogo(): #roda o jogo
    partida = 0
    jogador1 = 0
    jogador2 = 0
    jogador = False
    opcao = "S"
    play1 = input("Digite o nome do jogador 1: ").upper()
    play2 = input("Digite o nome do jogador 2: ").upper()
    print("\n\n      "+play1+"   X   "+play2+"     ")

    while opcao == "S": 
        jogo = matriz(3,3,-1)
        print("\n+-----------------------+")
        print("|       PARTIDA",partida+1,"      |")
        print("+-----------------------+\n")

        jogada = definir_jogadores(play1,play2) 
        mostrar_tabuleiro(jogo)
        jogador_atual = play1

        velha = 0 #variavel para contar as posições preenchidas da matriz
        while True:
            print("\n-- VEZ DE",jogador_atual," --")
            linha, coluna = verificar_jogada(input("Digite as coordenadas [LETRA, NUMERO]: ").upper(), jogo)
            fazer_jogada(linha,coluna,jogada,jogo)

            if (ganhar(jogo,linha,coluna,jogada)):
                mostrar_tabuleiro(jogo)
                print("\n     PARABÉNS,",jogador_atual,"! VOCÊ VENCEU!     \n")
                partida += 1
                if jogador == 0:
                    jogador1 += 1
                else:
                    jogador2 += 1
                break
            
            elif velha == 8: #casos todas as posições sejam preenchidas sem haver um ganhador, a partida acaba 
                partida += 1
                print("°.......................°")
                print("|       DEU VELHA       |")
                print("°.......................°\n")
                break

            else:
                if jogador_atual == play1:
                    jogador_atual = play2
                else:
                    jogador_atual = play1
                velha += 1
                mostrar_tabuleiro(jogo)
                jogador = not(jogador)
                if possibilidades(jogo,jogada):
                    print("\nVocê já perdeu,",jogador_atual)
                jogada = not(jogada)
        print("+-----------------------+")
        print("|      PLACAR ATUAL     |")
        print("+-----------------------+\n")
        print(play1+":", jogador1, "\n"+
              play2+":", jogador2, "\n")
        opcao = input("Continuar? [S/N] ").upper() # continuar o jogo, se não, o jogo para
        while opcao not in "SN":
            opcao = input("Opção Inválida! Digite novamente [S/N]: ").upper()
    print("\n+-----------------------+")
    print("|      PLACAR FINAL     |")
    print("+-----------------------+\n")
    print(play1+":", jogador1, "\n"+
          play2+":", jogador2, "\n")
    print("Até mais! Saindo..")


rodar_jogo()
