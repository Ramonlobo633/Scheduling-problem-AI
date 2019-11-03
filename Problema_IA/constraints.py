def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] 
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz
#função que conta todas as violações de restrições de um determinado estado
def conflits(allocation, nurses):
    total_conflits = 0
    total_conflits += conflitsr1(allocation, nurses)
    total_conflits += conflitsr2(allocation, nurses)
    total_conflits += conflitsr3(allocation, nurses)
    total_conflits += conflitsr4(allocation, nurses)

    return total_conflits

def conflitsr1(allocation, nurses):
    conflits = 0
    col = 0
    lin = 0
    count = 0 
    m = crie_matriz(nurses, 21, "0") 
    while lin < nurses:
        while col < 21:
            m[lin][col] = allocation[count]
            col += 1
            count += 1
        lin += 1
        col = 0
    col = 0
    lin = 0
    aux = 0   
    while col < 21:
        while lin < nurses:
            if( m[lin][col] == 1):
                aux += 1
            lin += 1
        if(aux == 0 or aux > 3):
            conflits += 1    
        col += 1
        lin = 0
    return conflits



def conflitsr2(allocation, nurses):
    conflits = 0
    count = 0
    
    for i in range(0, 21*nurses, 21):
        for j in range(i, (i+21)):
            if allocation[j] == '1':
                count += 1
            

        if count != 5:
            conflits += 1
        count = 0
  
    return conflits    

def conflitsr3(allocation, nurses):
    conflits = 0
    count = 0
    nrest = 0
    for i in range(0, 21*nurses, 21):
        for j in range(i, (i+21)):
            if allocation[j] == '1':
                count += 1

                if nrest > 3:
                    conflits += 1

                if nrest <= 3:
                    nrest += 1
            else:
                nrest = 0
   
    
    return conflits   

def conflitsr4(allocation, nurses):
    conflits = 0
    count = 0
    t1, t2, t3 = 0, 0, 0
    for i in range(0, 21*nurses, 21):
        for j in range(i, (i+21)):
            if (allocation[count] == 1):
                t1 += 1
            if (allocation[count+1] == 1):                         
                t2 += 1
            if (allocation[count+2] == 1):                               
                t3 += 1
            count += 1

        count = 0
        if t1 !=7 and t2 != 7 and t3 != 7:
            conflits += 1 
   
    return conflits
