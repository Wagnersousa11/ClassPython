x = input('Digite algo: ')
print(f'O tipo primitivo desta variavel é: {type(x)}')
print(f'A variavél é alfa numerica ?  {x.isalnum()}')
print(f'A variavel contem somente letras ? {x.isalpha()}')
print(f'Só tem espaços ? {x.isspace()}')
print(f'É um numero ? {x.isnumeric()}')
print(f'A variavel esta em letras minusculas ? {x.islower()}')
print(f'A variavel esta em letras maiúsculas ? {x.isupper()}')
print(f'A variavel esta capitalizada ? {x.istitle()}')

