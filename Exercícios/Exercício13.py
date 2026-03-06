'''Fazer um programa que peça um número e retorne o fatorial desse número (Sem usar biblioteca)'''

num = int(input('Digite um número inteiro natual: '))


def fatorial(num):
    if num > 0:
        fatorial = 1
        while num > 1:
            fatorial *= num
            print(f'{num} x ',end='')
            num -=1

        print(f'1 = {fatorial}') 
    else:
        print(f'Fatorial de 0 é 1!')   

fatorial(num)





