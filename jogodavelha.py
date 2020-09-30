# Trabalho Prático – Jogo da Velha
# Disciplina Fundamentos de Programação – Semestre 2020.1
# Isabel Cristina de Oliveira Lopes
# Matrícula: 493948

rodadas = 0
 
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
                linha, coluna = peca.split(",") #fatia a jogada em letra e numero
                coluna = int(coluna) #tranforma o valor da coluna em inteiro
                if linha == 'a': #converte de letra para número para ser usado na matriz
                    linha = int(0)
                elif linha == 'b':
                    linha = int(1)
                elif linha == 'c':
                    linha = int(2)
                    
                if matriz[linha][coluna-1] != -1: #verifica se a jogada já foi feita
                    peca = input("Você já fez essa jogada! Digite outra: ").lower()
                    
                else:
                    return linha, coluna-1 #retorna a linha e a coluna convertida
                    jogada = False #para o while
        peca = input("Coordenadas inválidas! Digite novamente: ").lower()
        
def fazer_jogada(matriz): 
    linha, coluna = verifica_jogada(jogada, matriz)
    if rodadas == 0:
        jogador = input("Jogador 1 [X/O]: ").lower()
        if jogador == "x":
            rodada = True
        elif jogador == "o":
            rodada = False
        else:
            while((jogador != "x") or (jogador != "o")):
                jogador = input("Peça Inválida! Digite outra [X/O]: ").lower()
    elif rodada:
        input("Digite sua jogada: ").lower()
        matriz[linha][coluna] = "X"
        rodada = False
    elif not(rodada):
        matriz[linha][coluna] = "O"
        rodada = True
        
         

jogo = matriz(3,3,-1) #Criação da matriz principal do jogo da velha  
fazer_jogada(jogo) 
mostrar_jogo(jogo)




