''' Implemente um programa que solicita um inteiro positivo n e exibe na tela todos os divisores positivos de n. Nota: 0 
não é um divisor de qualquer inteiro, e n divide por si mesmo.
>>>
Digite n: 49
1
7
49'''

n = int(input('Digite um número para saber seus divisores: '))
for i in range(1,n + 1):
    if n%i == 0:
        print(i)


