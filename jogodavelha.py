# Trabalho Prático – Jogo da Velha
# Disciplina Fundamentos de Programação – Semestre 2020.1
# Isabel Cristina de Oliveira Lopes
# Matrícula: 493948

jogar = input("Escolha sua peça, Jogador 1 [X/O]: ").lower()
while jogar not in "xo":
    jogar = input("Peça inválida, Jogador 1, digite outra: ").lower()
    
if jogar[0] == "x":
    rodada = True
    
elif jogar[0]=="o":
    rodada = False

partida = 0
 
def matriz(linhas, colunas, val_inic): #Criar matriz
    mat = [[val_inic] * colunas for _ in range(linhas)]
    return mat
    
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
        if len(peca) == 3 and peca: #se digitarem mais de 3 caracteres, pedirei outra jogada
            if not(peca[0] not in "aAbBcC") and (peca[1] == ",") and not(peca[2] not in '123'): #se não tiver o formato [letra,numero] pedirei outra jogada
                coluna, linha = peca.split(",") #fatia a jogada em letra e numero
                linha = int(linha) #tranforma o valor da coluna em inteiro
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
        
        if rodada:
            matriz[linha][coluna] = True
            for x in range(3):
                if matriz[linha][x] == True:
                    l += 1
            
                if matriz[x][coluna] == True:
                    c += 1
                    
            for i in range(len(matriz)): 
                for j in range(len(matriz[0])): 
                    if i==j:
                        if matriz[i][j] == True:
                            d += 1
            
            rodada = False
        
        elif not(rodada):
            matriz[linha][coluna] = False
            for x in range(3):
                if matriz[linha][x] == False:
                    l += 1
            
                if matriz[x][coluna] == False:
                    c += 1
                    
            for i in range(len(matriz)): 
                for j in range(len(matriz[0])): 
                    if i==j:
                        if matriz[i][j] == False:
                            d += 1
            
            rodada = True
        
        if l == 3 or c == 3 or d == 3:
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
        
    


        
    
                
        
         

jogo = matriz(3,3,-1) #Criação da matriz principal do jogo da velha  
fazer_jogada(jogo, rodada, partida) 





