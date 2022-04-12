#Conversor de medidas

m = float(input('Digite uma distancia em metros a ser convertida: '))

cent = m*100
mili = cent*10
km = m/1000

print(f'{m:.2f} metro(s) convertido(s) para kilometro(s), centimetro(s) e milimetro(s) ficam respectivamente: {km}km, {int(cent)}cm e {mili:.0f}mm.')
