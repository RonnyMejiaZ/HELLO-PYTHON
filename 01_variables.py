#variables

string_var = "Esta es una variable"
print(string_var)

#numero entero
int_number = 1234
print(int_number)

#multiples argumentos
print(string_var, int_number)

#cambiar tipo de variable (casting)
int_to_str = str(int_number)
print(int_to_str)
print(type(int_to_str))

#contar caracteres
print(len(string_var))

#contar caracteres de numero entero
print("Cantidad de caracteres: ",len(str(int_number)))

#Variables en una sola linea
x, y, z = 10, 20, 30
print(z, y, x)

#Variables en una sola linea con diferentes tipos de datos
a, b, c = "Hello", 123, 45.67
print(a, b, c)

#Inputs
"""
first_name = input("Enter your first name: ")
print("Hello", first_name)
"""
#forzamos el tipo con type hints
address: str = "Enter your address:"
address: int = 32
print(type(address))
#con type hints nos aseguramos que la variable sea del tipo que indicamos

