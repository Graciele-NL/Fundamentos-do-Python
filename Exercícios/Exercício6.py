'''O intervalo de uma lista de números é a maior diferença entre dois números quaisquer na lista.
 Escreva uma expressão em Python que calcule o intervalo de uma lista de números lst. Se a lista lst for, digamos,
 [3, 7, -2, 12], a expressão deverá ser avaliada como 14 (a diferença entre 12 e –2).'''


lista = [3, 7, -2, 12,35]
maior = lista[0]
menor = lista[0]

for i in lista:   
    
    if i > maior:
        maior = i
    
    if i < menor:
        menor = i
       
print('O valor corresponde a ',maior-menor)