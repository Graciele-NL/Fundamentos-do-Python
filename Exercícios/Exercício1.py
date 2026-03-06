''' Implemente um programa que solicita uma lista de nomes de aluno do usuário e exiba aqueles nomes que começam com as letras de A até M.
>>>
EX:
Digite a lista: ['Ellie', 'Steve', 'Sam', 'Owen', 'Mavin']
Ellie
Gavinsoma
'''

letras = 'abcdefghijklm'
nomes = input('Digite uma lista de nome separados por um espaço: ')
nomes = list(nomes.split(" "))

for nome in nomes:
    nome = nome.lower()
    
    if nome[0] in letras:
        print(nome.capitalize())


        



