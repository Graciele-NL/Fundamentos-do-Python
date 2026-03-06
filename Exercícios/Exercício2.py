''' Implemente um programa que solicita ao usuário que entre com as coordenadas x e y (cada um entre –10 e 10) de um dardo e calcula se 
o dardo atingiu o alvo, um círculo com centro (0,0) e raio 8. Se tiver atingido, a string Está dentro! deverá ser exibida na tela.
>>>
Digite x: 2.5
Digite y: 4
Está dentro!'''

x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))

def distancia(x,y):
    distancia = ((x**2) + (y**2))**0.5
    return distancia

if distancia(x,y) <= 8:
    print('Está dentro!')

