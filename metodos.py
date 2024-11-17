# Implementación de estructuras de datos y algoritmos en Python 


# Búsqueda Binaria (requiere lista ordenada)
# Realiza una búsqueda binaria en una lista ordenada.
# Retorna el índice del elemento si se encuentra, o -1 si no se encuentra.
def busqueda_binaria(lista, objetivo): 
    inicio = 0 
    fin = len(lista) - 1 
    while inicio <= fin: 
        medio = (inicio + fin) // 2 
        if lista[medio] == objetivo: 
            return medio 
        elif lista[medio] < objetivo: 
            inicio = medio + 1 
        else: 
            fin = medio - 1 
    return -1 

# Búsqueda Lineal
# Realiza una búsqueda lineal en una lista para encontrar un objetivo.
# Retorna el índice del objeto si se encuentra, o -1 si no se encuentra.
def busqueda_lineal(lista, objetivo): 
    for indice, valor in enumerate(lista): 
        if valor == objetivo: 
            return indice 
    return -1 

# Métodos de Ordenamiento
# Ordena la lista en su lugar.

# Ordenamiento por Burbuja
# Implementación del algoritmo de ordenamiento burbuja.
# Ordenamiento por Burbuja con soporte de claves
def ordenamiento_burbuja(lista, key=lambda x: x):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key(lista[j]) > key(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento por Inserción
# Implementación del algoritmo de ordenamiento por inserción.
def ordenamiento_insercion(lista): 
    for i in range(1, len(lista)): 
        clave = lista[i] 
        j = i - 1 
        while j >= 0 and clave < lista[j]: 
            lista[j + 1] = lista[j] 
            j -= 1 
        lista[j + 1] = clave 
    return lista 

# Ordenamiento por Selección
# Implementación del algoritmo de ordenamiento por selección.
def ordenamiento_seleccion(lista): 
    for i in range(len(lista)): 
        min_idx = i 
        for j in range(i+1, len(lista)): 
            if lista[j] < lista[min_idx]: 
                min_idx = j 
        lista[i], lista[min_idx] = lista[min_idx], lista[i] 
    return lista 

# Merge Sort
# Implementación del algoritmo por ordenamiento mergesort.
def merge_sort(lista): 
    if len(lista) <= 1: 
        return lista 
    medio = len(lista) // 2 
    izquierda = merge_sort(lista[:medio]) 
    derecha = merge_sort(lista[medio:]) 
    return merge(izquierda, derecha) 

def merge(izquierda, derecha): 
    resultado = [] 
    i = j = k = 0 
    while i < len(izquierda) and j < len(derecha): 
        if izquierda[i] < derecha[j]: 
            resultado.append(izquierda[i]) 
            i += 1 
        else: 
            resultado.append(derecha[j]) 
            j += 1 
    resultado.extend(izquierda[i:]) 
    resultado.extend(derecha[j:]) 
    return resultado 

# Quick Sort
# Implementación del algoritmo por ordenamiento mergesort.
def quick_sort(lista): 
    if len(lista) <= 1: 
        return lista 
    pivot = lista[len(lista) // 2] 
    izquierda = [x for x in lista if x < pivot] 
    centro = [x for x in lista if x == pivot] 
    derecha = [x for x in lista if x > pivot] 
    return quick_sort(izquierda) + centro + quick_sort(derecha)

# Clase Nodo para las estructuras de datos Pila y Cola
# Clase que define un nodo con un valor y un puntero al siguiente nodo.
# Se utiliza para construir pilas y colas.
class Nodo: 
    def __init__(self, valor): 
        self.valor = valor 
        self.siguiente = None 

# Clase Cola - Estructura FIFO (First In First Out)
# Clase para implementar una cola utilizando nodos. 
class Cola: 
    def __init__(self): 
        self.frente = None 
        self.final = None 

    # Agrega un nuevo elemento al final de la cola.
    def encolar(self, valor):
        nuevo_nodo = Nodo(valor) 
        if self.esta_vacia(): 
            self.frente = self.final = nuevo_nodo 
        else: 
            self.final.siguiente = nuevo_nodo 
            self.final = nuevo_nodo 
        print(f"Encolado: {valor}") 

    # Los elementos son agregados al final de la cola y removidos desde el frente.
    def desencolar(self): 
        if self.esta_vacia(): 
            return None 
        valor = self.frente.valor 
        self.frente = self.frente.siguiente
        # Remueve el elemento del frente de la cola y lo retorna
        print(f"Desencolado: {valor}") 
        if self.frente is None: 
            self.final = None 
        return valor 

    # Muestra todos los elementos de la pila.
    def mostrar(self): 
        actual = self.frente 
        cola_valores = [] 
        while actual is not None: 
            cola_valores.append(actual.valor) 
            actual = actual.siguiente 
        print(f"Elementos en la cola: {cola_valores}") 

    # Retorna True si la cola está vacía, False de lo contrario.
    def esta_vacia(self): 
        return self.frente is None  

# Clase Pila - Estructura LIFO (Last In First Out)
# Clase para implementar una pila utilizando nodos. 
class Pila: 
    def __init__(self):
        # El nodo superior (top) de la pila
        self.top = None

    # Apila (agrega) un nuevo elemento a la pila.
    def apilar(self, valor): 
        nuevo_nodo = Nodo(valor) 
        nuevo_nodo.siguiente = self.top 
        self.top = nuevo_nodo 
        print(f"Apilado: {valor}") 

    # Desapila (remueve) el elemento superior de la pila y lo retorna.
    # Los elementos son agregados y removidos desde la parte superior de la pila.
    def desapilar(self): 
        if self.esta_vacia(): 
            return None 
        valor = self.top.valor 
        self.top = self.top.siguiente 
        print(f"Desapilado: {valor}") 
        return valor
    
    # Muestra todos los elementos de la pila.
    def mostrar(self): 
        actual = self.top 
        pila_valores = [] 
        while actual is not None: 
            pila_valores.append(actual.valor) 
            actual = actual.siguiente 
        print(f"Elementos en la pila: {pila_valores}")

    # Retorna el valor en el tope de la pila sin removerlo.
    def ver_top(self):
        if self.esta_vacia():
            return None
        return self.top.valor

    # Retorna True si la pila está vacía, False de lo contrario.
    def esta_vacia(self): 
        return self.top is None 