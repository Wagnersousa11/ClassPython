from math import sqrt

n = float(input('Digite um numero: '))

dob = n*2
trip = n*3
#raiz = sqrt(n)
raiz = n**(1/2) #numero elevado a meio para obter a raiz.
print(f'O dobro, triplo e raiz quadrada de {n} são respectivamente: {dob}, {trip} e {raiz}.')
