print("Ejemplo de listas")
arcoirirs=["verde","azul","morado"]

print(arcoirirs)
longuitud=len(arcoirirs)
print("Elementos que contiene la lista de acoiris:", longuitud)
print(f"Elementos que contiene la lista de acoiris v2 {longuitud}")
print("Accediendo a un elemento de la lista:")
print(arcoirirs[1])
print(f"Elemento en la posicion 0 es: {arcoirirs[0]}")
print(f"El primer color del acoriris es:", arcoirirs[0])
print("Agregar a un elemento de la lista")
print(arcoirirs)
arcoirirs.append("naranja")
print(arcoirirs)
print("Listar los elementos de la lista ciclo for:")
for rodriguez in arcoirirs:
    print(rodriguez)
    