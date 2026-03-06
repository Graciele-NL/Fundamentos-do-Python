'''A imagem espelho da string vow é a string wov, e a imagem espelho de wood é a string boow. A imagem espelho da string bed, porém,
não pode ser representada como uma string, pois a imagem espelho de e não é um caractere válido.
Desenvolva a função espelho(), que apanhe uma string e retorne sua imagem espelho, mas somente se esta puder ser representada usando as
letras no alfabeto.
>>> espelho('vow')
'wov'
>>> espelho('wood')
'boow'
>>> espelho('bed')
'INVALID'''

def espelho(palavra):
    invertidas_espelho = {'d':'b','b':'d','o':'o','q':'p','p':'q','v':'v','w':'w','x':'x'}
    espelho = True
    nova_palavra = palavra

    for i in palavra:
        if i not in invertidas_espelho.keys():
            espelho = False
        
    if espelho:
        for i in palavra:
            nova_palavra = nova_palavra.replace(i,invertidas_espelho[i])

        return nova_palavra[::-1]

    else:
        return 'INVALID'


print(espelho('bed'))