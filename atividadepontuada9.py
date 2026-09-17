import os 
os.system ('cls')
salario=float(input('qual e seu salario:'))
valor=float(input('quanto de esprestimo voce quer:'))
presta=int(input('quantas parcelas voce quer pagar'))
parcela=salario*0.30
emprestimo=salario*10

if emprestimo>=salario*10:
    print(f'a parcela sera {parcela} reais')
else:
    print(f'nao podemos fazer seu emprestimo')