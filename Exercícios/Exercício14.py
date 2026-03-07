'''Implemente uma função que, dado um número n, retorne os n primeiros números da sequência de Fibonacci.'''

'''Ex:
Entrada: 7
Saída:
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7 
'''

def fibonacci(n):
    seqFi_Inicial = [0,1] #Primeiros dois elementos da sequencia;

    if n == 1 or n == 0:  #Retorno para se n < 2;
        return [0]
    else:                 #Lista Com a sequencia de Fibonacci
        for i in range(n-2):
            seqFi_Inicial.append(seqFi_Inicial[i]+seqFi_Inicial[i+1])

        return seqFi_Inicial
    

print(*fibonacci(20))     # O '*' Mostra uma vizualização sem os simbolos.


