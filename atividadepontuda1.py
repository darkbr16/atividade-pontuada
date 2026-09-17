import os
os.system ("cls")
numero1=float (input('digite um numero:'))
numero2=float (input('digite outro numero:'))
numero3=float (input('digite um ultimo numero:'))
soma=numero1+numero2

if soma>numero3:
    print (f'a soma entre {numero1} e {numero2} da {soma} e sao maiores que {numero3} ')

elif soma==numero3 :
    print (f'a soma entre {numero1} e {numero2} da {soma} que e igual ao {numero3} ')
else:
    print (f'a soma entre {numero1} e {numero2} da {soma} e nao sao maiores que {numero3} ')
    