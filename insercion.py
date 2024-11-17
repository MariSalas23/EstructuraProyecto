import tkinter as tk
from tkinter import font, messagebox
from n_ario import GenreTree
from libro import Libro  # Importar la clase Libro para manejar persistencia
import subprocess


class InsertWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inserción")
        self.root.geometry("490x525")

        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        light_red = "#f5e2e4"
        button_font = font.Font(family="Open Sans", size=12, weight="bold")
        title_font = font.Font(family="Open Sans", size=20, weight="bold")

        # Instancia de la clase Libro para manejar persistencia
        self.libro_manager = Libro()

        # Árbol de géneros
        self.genre_tree = GenreTree()
        self.selected_genre = tk.StringVar(value="Género seleccionado: Ninguno")

        # Validación para campos numéricos
        validate_numeric = self.root.register(self.only_numeric)

        # Diseño de la ventana
        background_frame = tk.Frame(self.root, background=light_blue, padx=10, pady=10)
        background_frame.pack(fill="both", expand=True)

        outer_frame = tk.Frame(background_frame, background=dark_blue, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        inner_frame = tk.Frame(middle_frame, background=red, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        content_frame = tk.Frame(inner_frame, background=light_red, padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Título
        tk.Label(content_frame, text="Agregar Libro", font=title_font, bg=light_red, fg=blue).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Campos de entrada
        self.entries = {}
        self.create_label_and_entry(content_frame, "ISBN", 1, validate_numeric)
        self.create_label_and_entry(content_frame, "Título", 2)
        self.create_label_and_entry(content_frame, "Autor", 3)
        self.create_label_and_entry(content_frame, "Año Publicación", 4, validate_numeric)
        self.create_label_and_entry(content_frame, "Cantidad", 5, validate_numeric)

        # Botón para seleccionar género
        tk.Label(content_frame, text="Género", bg=light_red, fg=blue).grid(row=6, column=0, sticky="w", padx=10, pady=5)
        tk.Button(content_frame, text="Selec. Género", command=self.select_genre, bg=blue, fg="white", font=button_font, width=17, relief=tk.FLAT).grid(row=6, column=1, padx=10, pady=5)

        # Mostrar género seleccionado
        tk.Label(content_frame, textvariable=self.selected_genre, bg=light_red, fg=red).grid(row=7, column=0, columnspan=2, pady=(5, 5))

        # Botones de acción
        button_frame = tk.Frame(content_frame, background=light_red)
        button_frame.grid(row=8, column=0, columnspan=2, pady=(25, 10))

        tk.Button(button_frame, text="Agregar", command=self.agregar_libro, bg=red, fg="white", font=button_font, width=13, height=1, relief=tk.FLAT).pack(side="left", padx=10)
        tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, width=13, height=1, relief=tk.FLAT).pack(side="left", padx=10)

    def create_label_and_entry(self, parent, label_text, row, validate_command=None):
        """Crea un label y un campo de entrada en una fila específica."""
        tk.Label(parent, text=label_text, bg="#f5e2e4", fg="#2f4f74").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(parent, width=29, validate="key", validatecommand=(validate_command, "%S")) if validate_command else tk.Entry(parent, width=29)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.entries[label_text] = entry

    def select_genre(self):
        genre = self.genre_tree.find_genre()
        if genre:
            self.selected_genre.set(f"Género seleccionado: {genre.upper()}")
        else:
            self.selected_genre.set("Género seleccionado: Ninguno")

    def agregar_libro(self):
        try:
            # Recolectar datos ingresados por el usuario
            isbn = self.entries["ISBN"].get().strip().upper()
            titulo = self.entries["Título"].get().strip().upper()
            autor = self.entries["Autor"].get().strip().upper()
            año_publicacion = self.entries["Año Publicación"].get().strip()
            cantidad = self.entries["Cantidad"].get().strip()
            genero = self.selected_genre.get().replace("Género seleccionado: ", "").strip().upper()

            # Validar que todos los campos estén llenos
            if not all([isbn, titulo, autor, año_publicacion, cantidad, genero]) or genero == "NINGUNO":
                raise ValueError("Todos los campos deben ser completados.")

            # Validar que los campos numéricos sean válidos
            año_publicacion = int(año_publicacion)
            cantidad = int(cantidad)

            # Validar ISBN
            if len(isbn) not in [10, 13]:
                raise ValueError("El ISBN debe contener exactamente 10 o 13 dígitos.")

            # Validar año de publicación
            if año_publicacion < 0 or año_publicacion > 2024:
                raise ValueError("El año de publicación debe estar entre 0 y 2024.")

            # Validar cantidad
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser un número negativo.")

            # Verificar si el ISBN ya existe
            libro_existente = self.libro_manager.library_data.get(isbn)
            if libro_existente:
                # Si el ISBN ya existe, preguntar si desea aumentar la cantidad
                titulo_existente = libro_existente["titulo"]
                respuesta = messagebox.askokcancel(
                    "ISBN existente",
                    f"Ese ISBN ya existe, ¿desea aumentar la cantidad de ejemplares de \"{titulo_existente}\"?"
                )
                if respuesta:  # Si el usuario confirma, sumar las cantidades
                    nueva_cantidad = libro_existente["cantidad"] + cantidad
                    self.libro_manager.library_data[isbn]["cantidad"] = nueva_cantidad
                    self.libro_manager.guardar_libros()
                    messagebox.showinfo(
                        "Cantidad actualizada",
                        f"La cantidad de ejemplares de \"{titulo_existente}\" ahora es {nueva_cantidad}."
                    )
                    for field in self.entries.values():
                        field.delete(0, tk.END)
                        self.selected_genre.set("Género seleccionado: Ninguno")
                return

            # Si el ISBN no existe, agregar el nuevo libro
            mensaje = self.libro_manager.agregar_libro(isbn, titulo, autor, genero, año_publicacion, cantidad)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Resultado", mensaje)

            # Limpiar los campos solo si se agrega correctamente
            if "agregado correctamente" in mensaje:
                for field in self.entries.values():
                    field.delete(0, tk.END)
                self.selected_genre.set("Género seleccionado: Ninguno")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def regresar(self):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])

    def only_numeric(self, char):
        return char.isdigit()
