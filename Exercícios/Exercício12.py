try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

except:
    print('Valor digitádo não é numero!')

else:
    def inteiro(num):
        if num - int(num) == 0:
           num = int(num)
        return num
    
    if num1 > num2:
        maior, menor = num1, num2
    else:
        maior, menor = num2, num1  

    print(f'O maior número é o {inteiro(maior)} e {inteiro(menor)} é o menor número!')

finally:
    print('Final do Programa!')



