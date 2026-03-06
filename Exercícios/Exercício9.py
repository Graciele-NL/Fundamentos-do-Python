'''Implemente a função parSoma(), que aceite como entrada uma lista de inteiros distintos lst e um inteiro n, 
e exiba os índices de todos os pares de valores em lst que somam n.
>>> parSoma([7, 8, 5, 3, 4, 6], 11)
0 4
1 3
2 5'''

lista = [7, 8, 5, 3, 4, 6, -10, 0]


def parSoma(lista,n):
    for i in lista: #Laço que percorre a lista;
        if (n - i) in lista: # Condição que avalia o complementar de n e busca na lista;
            if lista.index(i) < lista.index(n-i): # Avalia se o index já foi encontrado;
                return f'{lista.index(i)} {lista.index(n-i)}' # Imprime os index que formam a soma;

print(parSoma(lista,13))


