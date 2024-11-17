import json
import os

class Libro:
    def __init__(self, archivo_persistencia="libros.txt"):
        self.archivo_persistencia = archivo_persistencia
        self.library_data = {}
        self.cargar_libros()

    def guardar_libros(self):
        """Guarda los datos de los libros en un archivo JSON."""
        try:
            with open(self.archivo_persistencia, "w") as file:
                json.dump(self.library_data, file, indent=4)
        except IOError as e:
            print(f"Error al guardar los libros en el archivo: {e}")

    def cargar_libros(self):
        """Carga los datos de los libros desde un archivo JSON."""
        try:
            if os.path.exists(self.archivo_persistencia):
                with open(self.archivo_persistencia, "r") as file:
                    self.library_data = json.load(file)
            else:
                self.library_data = {}
        except json.JSONDecodeError:
            print("Error al leer el archivo. Puede estar corrupto.")
            self.library_data = {}

    def agregar_libro(self, isbn, titulo, autor, genero, fecha, cantidad):
        if isbn not in self.library_data:
            self.library_data[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "fecha": fecha,
                "cantidad": cantidad
            }
            self.guardar_libros()
            return f"Libro '{titulo}' agregado correctamente."
        else:
            return f"El libro con ISBN {isbn} ya existe."

    def listar_libros(self):
        """Devuelve una lista de libros con sus detalles."""
        return [{"isbn": isbn, **datos} for isbn, datos in self.library_data.items()]

    def buscar_libro(self, campo, valor):
        """Busca libros que coincidan con el campo y valor especificados."""
        return [
            {"isbn": isbn, **datos}
            for isbn, datos in self.library_data.items()
            if campo in datos and valor.lower() in datos[campo].lower()
        ]

    def eliminar_libro(self, isbn):
        if isbn in self.library_data:
            del self.library_data[isbn]
            self.guardar_libros()  # Guarda los cambios en el archivo
            return f"Libro con ISBN {isbn} eliminado correctamente."
        else:
            return f"No se encontró un libro con ISBN {isbn}."
