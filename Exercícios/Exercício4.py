'''Escreva a função mult3(), que aceite como entrada uma lista de inteiros e exiba somente os múltiplos de 3, um por linha.

>>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])
3
6
3
9
9'''



def mult3(numeros):
    for i in numeros:
        if int(i) % 3 == 0:
            print(i)


mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])