'''Crie uma função que verifica se uma matriz é simétrica.

Nota: Para que uma matriz seja simétrica é necessário que ela:
- Precisa ser uma matriz quadrada;
- Precisa ser igual a sua transposta;

def: matriz transposta é aquela que é gerada ao transpormos as linhas de uma matriz como coluna de uma nova matriz, a transposta.'''

matriz1 = [[1,-2,4], #Matriz quadrada e igual a sua transposta;
           [-2,2,0],
           [4,0,3]]


matriz2 = [[0,2], #Matriz NÃO é quadrada e não é igual a sua transposta;
           [0,6],
           [4,8]]

matriz3 = [[0,5,2,15], #Matriz quadrada e NÃO é igual a sua transposta;
           [0,9,5,-8],
           [8,7,-9,10],
           [8,7,6,9]]


'''Algoritmo:
1 - Ler a matriz;
2 - Validar se o número de o número de linhas é igual ao de colunas, se não o retorno é uma matriz não simétrica, se sim seguir o próximo passo;
3 - Validar se a primeira linha é iagual a primeira coluna, se a segunda linha é igual a segunda coluna e se a enésimo linha é igual a enésima coluna. Se todas as
verificações forem verdadeiras, teremos uma matriz simétrica.'''


def MatSimetrica(matriz):
    Matquadrada  = True
    Matsimetrico = True

    for i in range(len(matriz)): #Esse bloco de código também trata erros ao receber matrizes incomplestas. Ex: [[0,2,5],[0,3],[1,6,5]].
        if len(matriz) != len(matriz[i]):
            Matquadrada = False    
            Matsimetrico = False

    if Matquadrada:       
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] != matriz[j][i]:
                    Matsimetrico = False

    if Matsimetrico:
        return 'Matriz Simética!'
    else:
        return 'Não é Simétrica!'
    

print(f'Matriz1: {MatSimetrica(matriz1)}')
print(f'Matriz2: {MatSimetrica(matriz2)}')
print(f'Matriz3: {MatSimetrica(matriz3)}')


            
    