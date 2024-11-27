# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable))) # Tipo 'NoneType'
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) # 'len()' Cuenta los caracteres de las variables que le pasamos

# Variables en una sola línea. ¡Cuidad con abusar de esta sintaxis!
name, surname, alias, age = 'Rubén', 'Pérez', 'zRamBoXx', 27
print('Me llamo:', name, surname, '. Mi edad es:', age,'. Y mi nickname es:', alias)

'''
name = input('¿Cómo te llamas?: ')
age = input('¿Qué edad tienes?: ')

print(name)
print(age)
'''

name = 35
age = 'Rubén'

print('Nombre: ', name)
print('Edad: ', age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(address)
print(type(address))

