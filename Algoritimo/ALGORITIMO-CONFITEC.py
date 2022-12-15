## INICIANDO CALCULADORA DE PRODUTO ENTRE MATRIZES

matriz_A = [[0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0]]
matriz_B = [[0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0]]
matriz_RESULTADO = [[0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0]]

## GERANDO A MATRIZ A COM BASE NA DIGITAÇÃO DO USUÁRIO.

print("Definindo Matriz A.... \n")

for vLINHA1 in range(0,4):
    for vCOLUNA1 in range(0,4):
        matriz_A[vLINHA1][vCOLUNA1] = int(input(f'Digite um valor para a Matriz A na posição [{vLINHA1},{vCOLUNA1}] : '))

## IMPRIMINDO MATRIZ A

print("\n= Matriz A definida " + ('==' * 40))

for vLINHA2 in range(0,4):
    for vCOLUNA2 in range(0,4):
        print(f'[{matriz_A[vLINHA2][vCOLUNA2]:^5}]',end='')
    print()

## GERANDO A MATRIZ B COM BASE NA DIGITAÇÃO DO USUÁRIO.

print("\n Definindo Matriz B... \n")

for vLINHA3 in range(0,4):
    for vCOLUNA3 in range(0,4):
        matriz_B[vLINHA3][vCOLUNA3] = int(input(f'Digite um valor para a Matriz B na posição [{vLINHA3},{vCOLUNA3}] : '))

## IMPRIMINDO A MATRIZ B

print("\n= Matriz B definida " + ('==' * 40))

for vLINHA4 in range(0,4):
    for vCOLUNA4 in range(0,4):
        print(f'[{matriz_B[vLINHA4][vCOLUNA4]:^5}]',end='')
    print()

## CALCULANDO O PRODUTO COM BASE NA MATRIZ A E B

print("\n= Calculando Produto " + ('==' * 40))

for vCOUNTA in range(0,len(matriz_A)):
    for vCOUNTB in range(0,len(matriz_B)):
        for vCOUNTB2 in range(0,len(matriz_B)):
            matriz_RESULTADO[vCOUNTA][vCOUNTB] += matriz_A[vCOUNTA][vCOUNTB2] * matriz_B[vCOUNTB2][vCOUNTB]

## IMPRIMINDO O RESULTADO DO PRODUTO

print("\n O produto entre as duas Matrizes é : \n")

for vLINHA5 in range(0,4):
    for vCOLUNA5 in range(0,4):
        print(f'[{matriz_RESULTADO[vLINHA5][vCOLUNA5]:^5}]',end='')
    print()
