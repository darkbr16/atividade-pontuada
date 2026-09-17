import os
os.system ('cls')
combustivel=input('qual tipo de combustivel ira colocar A para alcool G para gasolina:').upper()
litros=float(input('quantos litros voce ira colocar de combustivel:'))

if combustivel=='G':
    preçobase=6.59
    if litros <=25:
        desconto=0.15
    else:
        desconto=0.30
elif combustivel== 'A':
    preçobase=3.79
    if litros <=25:
        desconto=0.15
    else:
        desconto=0.30
else:
    print('tipo de combustivel nao identificado')
    preçobase=0

if preçobase> 0:
    valorsemdesconto=litros*preçobase
    valorfinal=valorsemdesconto*(1-desconto)

print(f'combustivel selecionado:{combustivel}')
print(f'total a pagar:{valorfinal:.2f}')
