print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi, 1213, 3-W")
print(" ") # print imprime un espacio

thisdict = { # abriendo diccionario
    "euro":"€", # dando tipos de datos 
    "dollar":"$", # dando tipos de datos 
    "yen":"¥", # dando tipos de datos 
    "libra":"£ ", # dando tipos de  datos 
    "won": "₩" # dando tipos de datos 
} # cerrando diccionario

divisa = input("Introduce una divisa: ") # pide que ingreses una divisa

print(" ") # print imprime un espacio

if divisa in thisdict: # verifica si la divisa esta en el diccionario
    print(f"La divisa {divisa} es: {thisdict[divisa]}") # print imprime la divisa con su signo
else: # define parte falsa
    print(f"La divisa {divisa} no está en el diccionario.") # print imprime si la divisa no esta en el diccionario

print(" ") # print imprime un espacio

