# Trabalho Prático – Jogo da Velha
# Disciplina Fundamentos de Programação – Semestre 2020.1
# Isabel Cristina de Oliveira Lopes
# Matrícula: 493948
def matriz(linhas, colunas, val_inic): #Criar matriz
    mat = [[val_inic] * colunas for _ in range(linhas)]
    return mat

def menu():
    game = 0
    playA = 0
    playB = 0
    keep = True
    rodada = True
    while keep: 
        jogo = matriz(3,3,-1) #Criação da matriz principal do jogo da velha 
        continuar = input("0. Sair \n"+
                              "1. Jogar \n") 
                              
        while(continuar != '0' and continuar != '1'):
            continuar = input("Opção Inválida! Digite novamente: ")
                        
        if continuar != "0":
            jogar = input("Escolha sua peça, Jogador 1 [X/O]: ").lower()
            while jogar != 'x' and jogar!='o':
                jogar = input("Peça inválida, digite outra: ").lower()        
            if jogar[0] == "x":
                rodada = True            
            elif jogar[0]=="o":
                rodada = False
                    
            print()
            print("PLACAR:")       
            print("Jogador 1:", playA)
            print("Jogador 2:", playB)
            print()  
            print("PARTIDA:", game+1)
            partida = 0   
            if fazer_jogada(jogo, rodada, partida) == 1:
                playA += 1
            else:
                playB += 1      
            game+=1       
        else:
            print("Saindo...")
            keep = False                     

def mostrar_jogo(jogo_atual): #Mostra a matriz do jogo da velha com as jogadas atualizadas
    print("  {:<4}{:<4}{:<1}".format("A","B","C")) #Printa as colunas no inicio
    for i in range(len(jogo_atual)): #For para as linhas
        print("{}".format(i+1), end='') #Printa o número da linha no lado esquerdo
        for j in range(len(jogo_atual[0])): #For para as colunas
            if jogo_atual[i][j] == True: #Mostra os X's
                if j != 2: # Essa condição faz com que o | seja printado somente na primeira e na segunda coluna, ou seja, valores de j < 2
                    print("{:^3}{}".format("X", "|"), end='')
                else:
                    print("{:^3}".format("X"), end='')
            elif jogo_atual[i][j] == False: #Mostra os O's
                if j != 2:
                    print("{:^3}{}".format("O", "|"), end='')
                else:
                    print("{:^3}".format("O"), end='')
            elif jogo_atual[i][j] == -1: # -1 é o valor vazio da matriz do jogo da velha, mostra espaço em branco
                if j != 2:
                    print("{:^3}{}".format(" ", "|"), end='')
                else:
                    print("{:^3}".format(" "), end='')
           
        print("{}".format(i+1), end='') #Printa o número da linha no lado direito
        print()
        if i != 2: #Essa condição faz com que a linha de separação não seja printada na ultima linha
            print(" ---+---+---")
    print("  {:<4}{:<4}{:<1}".format("A","B","C")) #Printa as colunas no final

def verifica_jogada(peca, matriz): 
    jogada = True 
    while jogada: #Condição para o while rodar
        entrada = []
        virgula = 0
        for x in peca:
            if x != " " and x != ",":
                entrada.append(x)  
            if x == ",":
                virgula += 1
            
            
        if len(entrada) != 2 or virgula > 1:
            peca = input("Coordenadas inválidas! Digite novamente [LETRA,NUMERO]: ").lower()
        else:       
            coluna = entrada[0]
            linha = entrada[1]
            
            if coluna not in "abc" or linha not in "123":
                peca = input("Coordenadas inválidas! Digite novamente [LETRA,NUMERO]: ").lower()
                
            else:
                linha = int(entrada[1])
                if (coluna=='a' or coluna=='b' or coluna=='c') and (linha <= 3 and linha>= 0):         
                    if coluna == 'a': #converte de letra para número para ser usado na matriz
                        coluna = int(0)
                    elif coluna == 'b':
                        coluna = int(1)
                    elif coluna == 'c':
                        coluna = int(2)
                        
                    if matriz[linha-1][coluna] != -1: #verifica se a jogada já foi feita
                        peca = input("Você já fez essa jogada! Digite outra [LETRA,NUMERO]: ").lower()
                    
                    else:
                        return linha-1, coluna #retorna a linha e a coluna convertida
                        jogada = False #para o while                   
                else: 
                    peca = input("Coordenadas inválidas! Digite novamente [LETRA,NUMERO]: ").lower()
        
def fazer_jogada(matriz, rodada, partida): 
    ganhar = True
    while(ganhar):
        print()
        print()
        partida += 1
        print("-"*10, end=' ')
        print("RODADA", partida, end=' ')
        print("-"*10)
        print()
        print()
        mostrar_jogo(matriz)
        print()
        print()
        if partida%2 == 0:
            jogar = 2
        else:
            jogar = 1
            
        print("VEZ DO JOGADOR ",jogar)   
        linha, coluna = verifica_jogada(input("Digite sua jogada [LETRA,NUMERO]: ").lower(), matriz)
        l = 0
        c = 0
        d = 0
        ds = 0
        cont = 2
        matriz[linha][coluna] = rodada
        for x in range(3):
            #checando linhas
            if matriz[linha][x] == rodada:
                l += 1
            #checando colunas
            if matriz[x][coluna] == rodada:
                c += 1
             #checando diagonal primária      
            if matriz[x][x] == rodada:
                d += 1 
            #checando diagonal secundária
            if matriz[cont][x] == rodada:
                ds += 1
            cont -= 1
                    
        rodada = not(rodada)
        
        if l == 3 or c == 3 or d == 3 or ds == 3:
            print()
            print()
            print("-"*10, end=' ')
            print("O JOGADOR", jogar, "GANHOU! PARABÉNS!!!!!", end=' ')
            print("-"*10)
            print()
            print()
            mostrar_jogo(matriz)
            print()
            print()
            return jogar
            ganhar = False
            
        elif(partida > 8):
            print()
            print()
            print("-"*10, end=' ')
            print("DEU VELHA, NINGUÉM GANHOU HAHAHHA", end=' ')
            print("-"*10)
            print()
            print()
            mostrar_jogo(matriz)
            print()
            print()
            ganhar = False
  
  

menu() 