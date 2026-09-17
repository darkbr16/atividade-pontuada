import os
os.system ('cls')
morango=float(input('quantos kilos de morango voce quer comprar:'))
macas=float(input('quantos kilos de maça voce quer comprar:'))

if macas <=5:
    preço=macas*1.80
else:
    preço=macas*1.50
if morango <=5:
    preço2=morango*2.50
else:
    preço2=morango*2.20

somadospreços=preço+preço2
if somadospreços >15:
    desconto=somadospreços*0.10
    valorfinal=somadospreços-desconto
    print (f'pela compra ser superir a 15 reais tera um desconto de 10% sendo o valor {valorfinal:.2f}')