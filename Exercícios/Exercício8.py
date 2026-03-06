'''Escreva uma função mês() que aceite um número entre 1 e 12 como entrada e retorne a abreviação em três letras do mês correspondente.
 Faça isso sem usar uma instrução if, apenas operações de strings. Dica: use uma string para armazenar as abreviações em ordem.
>>> mês(1)
'Jan'
>>> mês(11)
'Nov'''

Mes = {1: 'jan', 2:'Fev', 3:'Mar' , 4:'Abr',5:'Mai',6:'Jun',7:'jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}

def mes(n):
    return Mes.get(n)

print(mes(12))

