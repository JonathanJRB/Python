# Só mostra verdadeiro se for numero

n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem numero? ', n.isnumeric())

# Só mostra verdade para alfabeto

o = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(o))
print('Só tem letra? ', o.isalpha())

# Só mostra verdadeiro se for letra maiuscula

b = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(b))
print('O formato tá maiusculo? ', b.isupper())