mi_diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid",
    "es_estudiante": False
}

# Recorrer solo las claves
for clave in mi_diccionario:
    print(clave)

# Recorrer solo los valores
for valor in mi_diccionario.values():
    print(valor)

# Recorrer claves y valores
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")