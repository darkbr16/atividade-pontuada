import os
os.system ("cls")
nome=input('digite seu nome:')
sexo=input('digite seu sexo feminino (f) masculino (m):')
estado_civil=input('voce e casado/casada ou solteiro/solteira:').lower()

if estado_civil=='casado' or estado_civil=='casada':
        tempo=float (input('quanto tempo de casados em anos'))
else:
    print('=====dados do usuario=====')

print(nome)
print(sexo)
if estado_civil=='casado' or estado_civil=='casada':
    print(estado_civil)
    print(tempo)
else:
    print(estado_civil)