import os
os.system ("cls")
nome=input('digite o nome do produto:')
quantidade=int(input('quanto desse produto voce esta levando:'))
preçounitario=float(input('digite o preço do produto:'))
total=quantidade*preçounitario

match quantidade:
    case x if quantidade <= 5:
        porcentagem = 0.02
        texto_desconto = "2%"
    case x if quantidade <= 10: 
        porcentagem = 0.03
        texto_desconto = "3%"
    case _:  
        porcentagem = 0.05
        texto_desconto = "5%"

desconto = total * porcentagem
valor_final = total - desconto

print(
    f"voce tera que pagar R$ {valor_final:.2f} tendo um desconto de {texto_desconto}"
)