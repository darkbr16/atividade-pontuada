import os
os.system ('cls')
print ('bem vindo a nossa loja de cds')
print ('nossa loja trabalha com cores em vez de etiquetas esta e a tabela de preços')
print (' cor     valor')
print ('verde    R$10')
print ('azul     R$20')
print('amarelo   R$30')
print('vermelho  R$40')
cor=input('digite qual e a cor do cd escolhido:').lower()
match cor:
    case "verde":
        print('este cd custa R$10  ')
    case "azul":
        print('este cd custa R$20  ')
    case "amarelo":
        print('este cd custa R$30  ')
    case "vermelho":
        print('este cd custa R$40  ')
    case _:
        print('cor invalida')