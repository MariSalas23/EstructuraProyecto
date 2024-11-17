# Implementación de estructuras de datos y algoritmos en Python

# Búsqueda Binaria (requiere lista ordenada)
# Realiza una búsqueda binaria en una lista ordenada.
# Retorna el índice del elemento si se encuentra, o -1 si no se encuentra.
# Búsqueda Binaria con soporte de claves
def busqueda_binaria(lista, objetivo, key=lambda x: x):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_actual = key(lista[medio])  # Obtener el valor a comparar
        if valor_actual == objetivo:
            return medio
        elif valor_actual < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ordenamiento por Burbuja con soporte de claves
def ordenamiento_burbuja(lista, key=lambda x: x):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key(lista[j]) > key(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento por Inserción con soporte de claves
def ordenamiento_insercion(lista, key=lambda x: x):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and key(clave) < key(lista[j]):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ordenamiento por Selección con soporte de claves
def ordenamiento_seleccion(lista, key=lambda x: x):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if key(lista[j]) < key(lista[min_idx]):
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Merge Sort con soporte de claves
def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], key)
    derecha = merge_sort(lista[medio:], key)
    return merge(izquierda, derecha, key)

def merge(izquierda, derecha, key):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if key(izquierda[i]) < key(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
