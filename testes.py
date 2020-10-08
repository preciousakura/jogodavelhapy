def matriz(linhas, colunas, val_inic): #Criar matriz
    mat = [[val_inic] * colunas for _ in range(linhas)]
    return mat
    
def mostrar_jogo(jogo_atual): 
    print('  A   B   C')
    for i in range(len(jogo_atual)): 
        for j in range(len(jogo_atual[0])): 
            print(i,'   |   |   ',i)

    
jogo = matriz(3,3,-1)
mostrar_jogo(jogo)