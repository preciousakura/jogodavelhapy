def acharLinha(entrada, item): #busca binária
    primeiro = 0
    ult = len(entrada)-1
    found = False
    while primeiro <= ult and not found:
        meio = (primeiro + ult)//2
        if entrada[meio] == item:
            found = True
        else:
            if item<entrada[meio]:
                ult = meio-1
            else:
                primeiro = meio+1
    return item
    
    
