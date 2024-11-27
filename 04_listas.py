### Lists ###
print(' ')
print('#'*15)
print('#'*3, ' Lists ', '#'*3)
print('#'*15)
print(' ')

my_list = list()
my_other_list = []

print(len(my_list))

my_other_list = [35, 25, 25, 36, 2, 98, 2]

print(my_other_list)
print(len(my_other_list))

my_list = [27, 1.77, "Rubén", 'Pérez']
print(type(my_list))

print(my_other_list[1])
print(my_list[-1])

print(my_list.count("Rubén"))
print(my_other_list.count(25))

age, height, name, surname = my_list # si no ponemos todos los elementos da Error
print(name)

name, height, surname, age = my_list[2],my_list[1],my_list[3],my_list[0]
print(surname)

print(my_list + my_other_list)
print(' ')

my_list.append('RPBsolutions')
print(my_list)
print(' ')

my_list.insert(1,'Azul')
print(my_list)
print(' ')

my_list.remove('Azul')
print(my_list)
print(' ')

my_other_list.remove(25)
print(my_other_list)
print(' ')

print(my_list.pop()) # Para eliminar el último elemento de la lista
my_list.pop(0) # Para eliminar el valor que queramos según su posición en la lista
print(my_list)
print(' ')

my_pop_element = my_list.pop(1)
print(my_pop_element)
print(my_list)

del my_list[0]
print(my_list)

my_list.clear()
print(my_list)

my_other_list[1] = 27
print(my_other_list)

my_new_list = my_other_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

print(my_new_list.reverse())



#my_list = ['Hola Python']
#print(my_list)
#print(type(my_list))

