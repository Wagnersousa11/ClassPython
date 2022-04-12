m = float(input('Digite a quantidade de metros a serem convertidos: '))

cent = m*100
mili = cent*10

print(f'{m:.2f} metro(s) convertido(s) para centimetro(s) e milimetro(s) ficam respectivamente: {int(cent)}cm e {int(mili)}mm.')