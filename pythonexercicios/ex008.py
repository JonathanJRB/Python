# Solicita que o usuário insira um valor em metros
metros = float(input('Digite o valor em metros: '))


# Converte metros para centímetros e milímetros
centimetros = int(float(metros * 100))
milimetros = int(float(metros * 1000))

# Exibe os resultados
print(f'{metros} metros é igual a {centimetros} centímetros.')
print(f'{metros} metros é igual a {milimetros} milímetros. ')