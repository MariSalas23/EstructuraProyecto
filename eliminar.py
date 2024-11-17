import tkinter as tk
from tkinter import messagebox, font
from libro import Libro  # Importar la clase Libro para manejar persistencia
import subprocess  # Para abrir main.py nuevamente

class DeleteWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Eliminación")
        self.root.geometry("470x360")

        # Instancia de la clase Libro
        self.libro_manager = Libro()

        # Colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        white = "#ffffff"
        title_font = font.Font(family="Open Sans", size=16, weight="bold")
        label_font = font.Font(family="Open Sans", size=12)
        button_font = font.Font(family="Open Sans", size=12, weight="bold")

        # Fondo general
        background_frame = tk.Frame(self.root, background=dark_blue, padx=10, pady=10)
        background_frame.pack(fill="both", expand=True)

        # Marco exterior con borde
        outer_frame = tk.Frame(background_frame, background=red, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Marco medio
        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        # Marco interno
        inner_frame = tk.Frame(middle_frame, background=light_blue, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Contenedor blanco para contenido
        content_frame = tk.Frame(inner_frame, background=white, padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Título
        title_label = tk.Label(content_frame, text="Eliminar Libro", font=title_font, background=white, foreground=blue)
        title_label.pack(pady=10)

        # Etiqueta y entrada para ISBN
        label = tk.Label(content_frame, text="Ingrese el ISBN del libro a eliminar:", font=label_font, bg=white, fg=blue)
        label.pack(pady=5)

        self.isbn_entry = tk.Entry(content_frame, font=label_font, width=30)
        self.isbn_entry.pack(pady=5)

        # Marco para los botones
        button_frame = tk.Frame(content_frame, background=white)
        button_frame.pack(pady=15)

        # Botón para confirmar eliminación
        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_book, bg=red, fg=white, font=button_font, relief=tk.FLAT, width=12)
        delete_button.grid(row=0, column=0, padx=10, pady=10)

        # Botón para regresar
        back_button = tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg=white, font=button_font, relief=tk.FLAT, width=12)
        back_button.grid(row=0, column=1, padx=10, pady=10)

    def delete_book(self):
        isbn = self.isbn_entry.get().strip()
        if isbn:
            # Verificar si el libro existe
            libro_existente = self.libro_manager.library_data.get(isbn)
            if not libro_existente:
                messagebox.showwarning("Resultado", "No se encontró un libro con el ISBN proporcionado.")
                return

            # Si la cantidad es mayor a 1, preguntar cuántos ejemplares eliminar
            cantidad_actual = libro_existente["cantidad"]
            if cantidad_actual > 1:
                while True:
                    cantidad_a_eliminar = tk.simpledialog.askstring(
                        "Eliminar ejemplares",
                        f"El libro '{libro_existente['titulo']}' tiene {cantidad_actual} ejemplares.\n"
                        "¿Cuántos desea eliminar?",
                    )
                    if cantidad_a_eliminar is None:  # Si se cancela la operación
                        return
                    try:
                        cantidad_a_eliminar = int(cantidad_a_eliminar)
                        if cantidad_a_eliminar <= 0:
                            raise ValueError("La cantidad debe ser mayor a 0.")
                        if cantidad_a_eliminar > cantidad_actual:
                            raise ValueError("La cantidad a eliminar no puede exceder la cantidad existente.")
                        break  # Salir del bucle si todo es válido
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))

                # Actualizar la cantidad restante
                nueva_cantidad = cantidad_actual - cantidad_a_eliminar
                self.libro_manager.library_data[isbn]["cantidad"] = nueva_cantidad
                self.libro_manager.guardar_libros()
                if nueva_cantidad > 0:
                    messagebox.showinfo(
                        "Resultado",
                        f"Se eliminaron {cantidad_a_eliminar} ejemplar(es) de '{libro_existente['titulo']}'.\n"
                        f"Cantidad restante: {nueva_cantidad}.",
                    )
                    self.isbn_entry.delete(0, tk.END)
                else:
                    # Si la cantidad restante es 0, eliminar el libro del sistema
                    del self.libro_manager.library_data[isbn]
                    self.libro_manager.guardar_libros()
                    messagebox.showinfo("Resultado", f"Se eliminaron todos los ejemplares de '{libro_existente['titulo']}'.")
                    self.isbn_entry.delete(0, tk.END)

            else:
                # Si la cantidad es 1, eliminar el libro directamente
                result = self.libro_manager.eliminar_libro(isbn)
                if "eliminado correctamente" in result.lower():
                    messagebox.showinfo("Resultado", result)
                    self.isbn_entry.delete(0, tk.END)  # Limpia el campo de entrada si la eliminación fue exitosa
                else:
                    messagebox.showwarning("Resultado", result)  # Muestra un aviso si el libro no se encuentra
        else:
            messagebox.showerror("Error", "Por favor, ingrese un ISBN válido.")

    def regresar(self):
        self.root.destroy()  # Cierra la ventana actual
        subprocess.Popen(["python", "main.py"])  # Vuelve a lanzar la ventana principal
