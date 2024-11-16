import tkinter as tk
from tkinter import font, messagebox
from n_ario import GenreTree
from libro import Libro  # Importar la clase Libro para manejar persistencia
import subprocess

class InsertWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar Libro")
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
        fields = ["ISBN", "Título", "Autor", "Año Publicación", "Cantidad"]
        self.entries = {}

        for i, field in enumerate(fields):
            tk.Label(content_frame, text=field, bg=light_red, fg=blue).grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(content_frame, width=29)  # Ajuste de ancho del input
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries[field] = entry

        # Botón para seleccionar género
        tk.Label(content_frame, text="Género", bg=light_red, fg=blue).grid(row=len(fields) + 1, column=0, sticky="w", padx=10, pady=5)
        tk.Button(content_frame, text="Selec. Género", command=self.select_genre, bg=blue, fg="white", font=button_font, width=17, relief=tk.FLAT).grid(row=len(fields) + 1, column=1, padx=10, pady=5)

        # Mostrar género seleccionado
        tk.Label(content_frame, textvariable=self.selected_genre, bg=light_red, fg=red).grid(row=len(fields) + 2, column=0, columnspan=2, pady=(5, 5))

        # Botones de acción
        button_frame = tk.Frame(content_frame, background=light_red)
        button_frame.grid(row=len(fields) + 3, column=0, columnspan=2, pady=(25, 10))
        button_frame.grid(row=len(fields) + 3, column=0, columnspan=2, pady=(25, 10))

        tk.Button(button_frame, text="Agregar", command=self.agregar_libro, bg=red, fg="white", font=button_font, width=13, height=1, relief=tk.FLAT).pack(side="left", padx=10)
        tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, width=13, height=1, relief=tk.FLAT).pack(side="left", padx=10)

    def select_genre(self):
        # Usar el árbol n-ario para seleccionar el género
        genre = self.genre_tree.find_genre()
        if genre:
            self.selected_genre.set(f"Género seleccionado: {genre}")
        else:
            self.selected_genre.set("Género seleccionado: Ninguno")

    def agregar_libro(self):
        try:
            # Recolectar datos ingresados por el usuario
            isbn = self.entries["ISBN"].get().strip()
            titulo = self.entries["Título"].get().strip()
            autor = self.entries["Autor"].get().strip()
            año_publicacion = int(self.entries["Año Publicación"].get().strip())
            cantidad = int(self.entries["Cantidad"].get().strip())
            genero = self.selected_genre.get().replace("Género seleccionado: ", "").strip()

            # Validar selección de género
            if genero == "Ninguno":
                raise ValueError("Debe seleccionar un género.")

            # Validar campos obligatorios
            if not all([isbn, titulo, autor, año_publicacion, cantidad]):
                raise ValueError("Todos los campos son obligatorios.")

            # Validar ISBN
            if not isbn.isdigit() or len(isbn) not in [10, 13]:
                raise ValueError("El ISBN debe ser un número de 10 o 13 dígitos.")

            # Guardar libro en el archivo
            mensaje = self.libro_manager.agregar_libro(isbn, titulo, autor, genero, año_publicacion, cantidad)
            messagebox.showinfo("Resultado", mensaje)

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def regresar(self):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])
