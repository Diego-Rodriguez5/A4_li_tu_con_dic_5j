print("Ejemplo de tuplas")
canciones=("Te amo", "El NoaNoa", "Amor eterno")
print(canciones)  
y = list(canciones) #Crea una variable la tupla "canciones" para poder editarla
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)