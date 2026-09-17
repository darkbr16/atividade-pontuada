import os
os.system ("cls")
nota1=float(input('digite uma nota:'))
nota2=float(input('digite outra nota:'))

media=(nota1+nota2)/2
faltante=6-media
match media:
    case x if media>=6:
        resultado=(f'parabens voce passou de ano com {media} de media')
    case x if media>=4.1 and media <=5.9:
        resultado=(f'nao desista voce esta na recuperaçao sua media foi de {media} voce precisa de {faltante} ponto para passar ')
    case x if media<=4:
         resultado=(f'infelizmente voce perdeu de ano sua media foi {media}')

print (resultado)