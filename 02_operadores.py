### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 4) # Te da el resto de la operación
print(10 // 4) # Floor division: División aproximada a un número entero
print(2 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4) 

print ('Hola ' + 'Python ' + '¿Qué tal?')
#print ('Hola' - 'Python') # Error.
print ('Hola ' + 'Python ' + str(5)) # Si concatenas letras con números tienes que cambiarle el tipo de los números a letras.
print('Hola ' * 5)
print('Hola ' * (2**3))

my_float = 2.5*2
print('Hola ' * int(my_float))

### Operadores comparativos ###
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 > 4)
print(3 == 4)
print(3 != 4)

print('Hola mundo')

print(' ')
print('#'*28)
print('#'*3, ' Operadores Lógicos ', '#'*3)
print('#'*28)

print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')
print(3 < 4 and 'Hola' < 'Python')
print(3 < 4 or 'Hola' > 'Python')
print(3 < 4 or ('Hola' > 'Python' and 4 == 4))
print(not(3 > 4))# 'not' sirve para negar la condición
