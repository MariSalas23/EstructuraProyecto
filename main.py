import tkinter as tk
from tkinter import font, messagebox
from example import LibraryApp  # Importar LibraryApp
from insercion import InsertWindow
from eliminar import DeleteWindow
from libro import Libro
from visualizar import GraphInterface  # Importar la nueva interfaz de grafo

class MainInterface:
    def __init__(self):
        # Configuración de colores
        self.dark_blue = "#6c93a4"
        self.red = "#ef6869"
        self.blue = "#2f4f74"
        self.light_blue = "#b5ccd2"
        self.light_red = "#f5e2e4"
        self.white = "#ffffff"

        # Crear la instancia de Libro (con persistencia)
        self.libro_instance = Libro()  # Instancia global de Libro

        # Configuración de la ventana principal
        self.window = tk.Tk()
        self.window.title("Sistema de Gestión de Biblioteca")
        self.window.geometry("465x415")
        self.window.configure(background=self.dark_blue)

        # Definir fuentes personalizadas
        title_font = font.Font(family="Open Sans", size=24, weight="bold")
        subtitle_font = font.Font(family="Open Sans", size=12, slant="italic")
        button_font = font.Font(family="Open Sans", size=12, weight="bold")

        # Crear marco con borde
        outer_frame = tk.Frame(self.window, background=self.red, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        middle_frame = tk.Frame(outer_frame, background=self.blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        inner_frame = tk.Frame(middle_frame, background=self.light_blue, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Contenedor blanco dentro del inner_frame
        content_frame = tk.Frame(inner_frame, background=self.white, padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Título y subtítulo
        title_label = tk.Label(content_frame, text="Biblioteca JCM", font=title_font, background=self.white, foreground=self.blue)
        title_label.pack(pady=10)

        subtitle_label = tk.Label(content_frame, text="¿Qué acción desea?", font=subtitle_font, background=self.white, foreground=self.blue)
        subtitle_label.pack(pady=5)

        # Frame para los botones dentro del content_frame
        button_frame = tk.Frame(content_frame, background=self.white)
        button_frame.pack(pady=15)

        # Crear botones con el comando correspondiente
        self.create_button(button_frame, "Inserción", self.open_insert_window, self.red, button_font, 0, 0)
        self.create_button(button_frame, "Búsqueda", self.search_book, self.blue, button_font, 0, 1)
        self.create_button(button_frame, "Eliminación", self.delete_book, self.blue, button_font, 1, 0)
        self.create_button(button_frame, "Visualización", self.open_graph_interface, self.red, button_font, 1, 1)

    def create_button(self, parent, text, command, color, font, row, column):
        """Crea botones con estilos consistentes."""
        button = tk.Button(parent, text=text, command=command, bg=color, fg="white",
                           font=font, width=12, height=2, relief=tk.FLAT)
        button.grid(row=row, column=column, padx=10, pady=10)

    def open_insert_window(self):
        """Abrir ventana de inserción."""
        self.window.destroy()
        new_window = tk.Tk()
        InsertWindow(new_window)
        new_window.mainloop()

    def search_book(self):
        """Abrir ventana de búsqueda."""
        self.window.destroy()
        new_window = tk.Tk()
        LibraryApp(new_window)
        new_window.mainloop()

    def delete_book(self):
        """Abrir ventana de eliminación."""
        self.window.destroy()
        new_window = tk.Tk()
        DeleteWindow(new_window)
        new_window.mainloop()

    def open_graph_interface(self):
        """Abrir la interfaz de grafo."""
        self.window.destroy()
        new_window = tk.Tk()
        GraphInterface(new_window, self.libro_instance)  # Pasar la instancia de libros a la interfaz
        new_window.mainloop()

    def view_books(self):
        """Visualizar libros en una lista o grafo."""
        libros = self.libro_instance.listar_libros()
        if libros:
            libros_texto = "\n".join([f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})" for libro in libros])
            messagebox.showinfo("Lista de Libros", libros_texto)
        else:
            messagebox.showinfo("Lista de Libros", "No hay libros registrados.")

    def run(self):
        """Ejecutar la interfaz."""
        self.window.mainloop()

if __name__ == "__main__":
    app = MainInterface()
    app.run()
