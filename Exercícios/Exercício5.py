'''Implemente a função quatro_letras(), que aceite como entrada uma lista de palavras (ou seja, strings) e retorne a sublista de 
todas as palavras de quatro letras na lista.
>>> quatro_letras(['cão', 'letra', 'pare', 'tela', 'bom', 'dica'])
['pare', 'tela', 'dica']'''


def quatro_letras(nomes):
    lista_quatro_letras = []
    for i in nomes:
        if len(i) == 4:
            lista_quatro_letras.append(i)
    return lista_quatro_letras


print(quatro_letras(['cão', 'letra', 'pare', 'tela', 'bom', 'dica']))