### Strings ###
print(' ')
print('#'*17)
print('#'*3, ' Strings ', '#'*3)
print('#'*17)
print(' ')

my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' y ' + my_other_string)

my_new_line_string = 'Este es un string\ncon salto de línea'
print(my_new_line_string)

my_new_tab_string = '\tEste es un string con tabulación'
print(my_new_tab_string)

my_scape_string = '\tEste es un string\nescapado'
print(my_scape_string)

### Formateo ###
print(' ')
print('#'*18)
print('#'*3, ' Formateo ', '#'*3)
print('#'*18)
print(' ')

name, surname, age = 'Rubén', 'Pérez', 35

print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))# Para hacer referencia a los strings que tengo ya establecidos
print('Mi nombre es %s %s y mi edad es %d' %(name,surname,age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')# Formatear e inferir los valores correspondientes

### Desempaquetado de caracteres ###
print(' ')
print('#'*38)
print('#'*3, ' Desempaquetado de caracteres ', '#'*3)
print('#'*38)
print(' ')

language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

### División ###
print(' ')
print('#'*18)
print('#'*3, ' División ', '#'*3)
print('#'*18)
print(' ')

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

### Reverse ###
print(' ')
print('#'*17)
print('#'*3, ' Reverse ', '#'*3)
print('#'*17)
print(' ')

reverse_language = language[::-1]
print(reverse_language)

### Funciones ###
print(' ')
print('#'*19)
print('#'*3, ' Funciones ', '#'*3)
print('#'*19)
print(' ')

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith('py'))