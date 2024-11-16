class Libro:
    def __init__(self):
        self.library_data = {}

    def agregar_libro(self, isbn, titulo, autor, genero, año_publicacion, cantidad):
        if isbn not in self.library_data:
            self.library_data[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "año_publicacion": año_publicacion,
                "cantidad": cantidad
            }
            return f"Libro '{titulo}' agregado correctamente."
        else:
            return f"El libro con ISBN {isbn} ya existe."

    def eliminarLibro(self, isbn):
        if isbn in self.library_data:
            libro_eliminado = self.library_data.pop(isbn)
            return f"Libro '{libro_eliminado['titulo']}' eliminado correctamente."
        else:
            return f"No se encontró ningún libro con el ISBN {isbn}."

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.library_data.values():
            if str(libro.get(criterio, "")).lower() == str(valor).lower():
                resultados.append(libro)
        return resultados

    def listar_libros(self):
        return list(self.library_data.values())
