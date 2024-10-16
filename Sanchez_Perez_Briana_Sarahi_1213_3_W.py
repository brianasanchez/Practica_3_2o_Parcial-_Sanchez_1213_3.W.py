print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi, 1213, 3-W")
print(" ") # print imprime un espacio

thisdict = { # abriendo diccionario
    "manzana": 30.0, # dando tipos de datos 
    "pera": 25.0, # dando tipos de datos 
    "plátano": 18.0, # dando tipos de datos 
    "naranja": 22.0, # dando tipos de datos 
    "mango": 35.0 # dando tipos de datos 
} # cerrando diccionario

fruta = input("¿Qué fruta deseas? ") # pide que ingreses la fruta que quieras 

print(" ") # print imprime un espacio

kilos = float(input("¿Cuántos kilos deseas? "))
 # pide que ingreses los kilos de fruta que quieras

print(" ") # print imprime un espacio

if fruta in thisdict: # verifica si la fruta esta en el diccionario
    precio = thisdict[fruta] # da el precio de la fruta
    total = precio * kilos # da el total a pagar 
    print(f"El precio de {kilos} kilos de {fruta} es ${total:.2f}.") 
    # print imprime el precio de los kilos de la fruta con su total 
else: # define parte falsa
    print(f"Lo siento, no tenemos {fruta}.") # print imprime que no tiene esa fruta

print(" ") # print imprime un espacio