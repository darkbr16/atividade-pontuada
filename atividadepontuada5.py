import os
os.system('cls')
numero1=float(input('digite um numero:'))
numero2=float(input('digite outro numero:'))
operaçoes=input('digite uma das 4 operaçoes a seguir para calcular (+|-|*|/):')

match operaçoes:
    case '+':
        resultado=numero1+numero2
        print(f'o resultado da soma do {numero1} e {numero2} e {resultado:.2f}')
    case '-':
        resultado=numero1-numero2
        print(f'o resultado da subtraçao do {numero1} e {numero2} e {resultado:.2f}')
    case '*':
        resultado=numero1*numero2
        print(f'o resultado da multiplicaçao do {numero1} e {numero2} e {resultado:.2f}')
    case '/':
        resultado=numero1/numero2
        print(f'o resultado da divisao do {numero1} e {numero2} e {resultado:.2f}')