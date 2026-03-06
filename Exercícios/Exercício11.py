'''Desenvolva um jogo simples que ensine a alunos de jardim da infância a somar números de um dígito. Sua função jogo() apanhará um inteiro 
n como entrada e depois fará n perguntas de adição com números de único dígito. Os números a serem somados deverão ser escolhidos
aleatoriamente a partir do intervalo [0, 9] (isto é, 0 a 9, inclusive). O usuário informará a resposta quando solicitado.
Sua função deverá exibir 'Correto' ou 'Incorreto', dependendo se a resposta é correta ou não. Depois de n perguntas,
sua função deverá exibir o número de respostas corretas.
>>> jogo(3)
8 + 2 =
Digite a resposta: 10
Correto.
6 + 7 =
Digite a resposta: 12
Incorreto.
7 + 7 =
Digite a resposta: 14
Correto.
Você teve 2 respostas corretas entre 3'''

import random

def jogo(partidas):
  
    qtd_acertos = 0

    for partida in range(1,partidas+1):
        aleatorio1 = random.randint(0,9)
        aleatorio2 = random.randint(0,9)

        print(f'{aleatorio1} + {aleatorio2} = ')
        resposta = eval(input('Digite a resposta: '))
        soma_correta = aleatorio1 + aleatorio2

        if resposta == soma_correta :
            print('Correto')
            qtd_acertos +=1
        else:
            print('Incorreto')
        
        print(f'Você teve {qtd_acertos} respostas corretas entre {partidas}')
    

jogo(5)


