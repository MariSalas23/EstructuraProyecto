# Estructura de datos para almacenar información de libros
library_data = {
    "978-3-16-148410-0": {
        "título": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "género": "Ficción",
        "año_publicación": 1943,
        "cantidad": 5
    },
    "978-0-262-03488-7": {
        "título": "1984",
        "autor": "George Orwell",
        "género": "Distopía",
        "año_publicación": 1949,
        "cantidad": 3
    },
    # Agrega más libros según sea necesario
}

# Función para agregar un libro a la biblioteca
def agregar_libro(isbn, título, autor, género, año_publicación, cantidad):
    if isbn not in library_data:
        library_data[isbn] = {
            "título": título,
            "autor": autor,
            "género": género,
            "año_publicación": año_publicación,
            "cantidad": cantidad
        }
        print(f"Libro '{título}' agregado correctamente.")
    else:
        print(f"El libro con ISBN {isbn} ya existe.")

# Función para eliminar un libro por ISBN
def eliminar_libro(isbn):
    if isbn in library_data:
        del library_data[isbn]
        print(f"Libro con ISBN {isbn} eliminado correctamente.")
    else:
        print(f"No se encontró un libro con ISBN {isbn}.")

# Función para buscar un libro por ISBN
def buscar_libro(isbn):
    return library_data.get(isbn, f"No se encontró un libro con ISBN {isbn}.")

# Función para listar todos los libros
def listar_libros():
    return library_data
