import json

class Libro:
    def __init__(self, archivo_persistencia="libros.txt"):
        self.archivo_persistencia = archivo_persistencia
        self.library_data = {}
        self.cargar_libros()  # Carga los libros existentes al iniciar

    def guardar_libros(self):
        """Guarda los datos de los libros en un archivo JSON."""
        try:
            with open(self.archivo_persistencia, "w") as file:
                json.dump(self.library_data, file, indent=4)
        except IOError:
            print("Error al guardar los libros en el archivo.")

    def cargar_libros(self):
        """Carga los datos de los libros desde un archivo JSON."""
        try:
            with open(self.archivo_persistencia, "r") as file:
                self.library_data = json.load(file)
        except FileNotFoundError:
            print(f"El archivo {self.archivo_persistencia} no existe. Se creará uno nuevo.")
            self.library_data = {}
        except json.JSONDecodeError:
            print("Error al leer el archivo. Puede estar corrupto.")
            self.library_data = {}

    def agregar_libro(self, isbn, titulo, autor, genero, año_publicacion, cantidad):
        if isbn not in self.library_data:
            self.library_data[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "fecha": año_publicacion,
                "cantidad": cantidad
            }
            self.guardar_libros()  # Guarda los cambios en el archivo
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
<<<<<<< HEAD

    def eliminar_libro(self, isbn):
        if isbn in self.library_data:
            del self.library_data[isbn]
            self.guardar_libros()  # Guarda los cambios en el archivo
            return f"El libro con ISBN {isbn} ha sido eliminado."
        return f"No se encontró ningún libro con ISBN {isbn}."
=======
>>>>>>> 93c490c56abfc5332fbd715e7376faa63353c61c
