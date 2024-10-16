print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi, 1213, 3-W")
print(" ") # print imprime un espacio

nombre = input("Ingresa tu nombre: ") # pide que ingreses tu nombre
edad = input("Ingresa tu edad: ") # pide que ingreses tu edad
direccion = input("Ingresa tu direccion: ") # pide que ingreses tu direccion
telefono = input("Ingresa tu numero de telefono: ") # pide que ingreses tu numero de telefono

print(" ") # print imprime un espacio

thisdict = { # abriendo diccionario
    "nombre": nombre, #  dando tipos de datos 
    "edad": edad, #  dando tipos de datos 
    "direccion": direccion, #  dando tipos de datos 
    "telefono": telefono #  dando tipos de datos 
} # 

print(f"{thisdict['nombre']} tiene {thisdict['edad']} años,")
 # print imprime el nombre y la edad ingresada
print(f"vive en {thisdict['direccion']}") # print imprime la direccion ingresada
print(f"y su número de teléfono es {thisdict['telefono']}.")
 # print imprime el numero de telefono ingresado

print(" ") # print imprime un espacio
