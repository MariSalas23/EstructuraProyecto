from tkinter import font, ttk, simpledialog, messagebox
import tkinter as tk
from libro import Libro  # Importar la clase Libro desde libro.py
import subprocess  # Para manejar el regreso al menú principal


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda")

        # Configurar ventana para pantalla completa
        self.root.state('zoomed')  # Configurar ventana en modo maximizado (pantalla completa)

        # Crear instancia de Libro
        self.libro_manager = Libro()  # Objeto para gestionar libros

        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        white = "#ffffff"
        title_font = font.Font(family="Open Sans", size=16, weight="bold")
        button_font = font.Font(family="Open Sans", size=12, weight="bold")
        label_font = font.Font(family="Open Sans", size=12)

        # Contenedor principal
        background_frame = tk.Frame(self.root, background=dark_blue, padx=10, pady=10)
        background_frame.pack(fill="both", expand=True)

        # Marco exterior
        outer_frame = tk.Frame(background_frame, background=red, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Marco medio
        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        # Marco interior
        inner_frame = tk.Frame(middle_frame, background=light_blue, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Frame de búsqueda
        search_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        search_frame_border.pack(fill="x", padx=10, pady=10)

        search_frame = tk.Frame(search_frame_border, background=white, padx=10, pady=10)
        search_frame.pack(fill="x")

        search_label = tk.Label(search_frame, text="Buscar libros:", font=label_font, bg=white, fg=blue)
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, font=label_font, width=40)
        self.search_entry.pack(side="left", padx=5, expand=True, fill="x")

        search_button = tk.Button(search_frame, text="🔍", command=self.search_books, bg=red, fg="white", font=button_font, relief=tk.FLAT)
        search_button.pack(side="left", padx=5)

        # Frame de lista de libros
        book_list_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        book_list_frame_border.pack(fill="both", expand=True, padx=10, pady=10, side="left")

        book_list_frame = tk.Frame(book_list_frame_border, background=white, padx=10, pady=10)
        book_list_frame.pack(fill="both", expand=True)

        self.book_list = tk.Listbox(book_list_frame, width=60, height=20, bg=light_blue, font=label_font)
        self.book_list.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(book_list_frame, orient="vertical", command=self.book_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.book_list.config(yscrollcommand=scrollbar.set)

        # Panel de filtros
        filters_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        filters_frame_border.pack(fill="y", side="right", padx=10, pady=10)

        filters_frame = tk.Frame(filters_frame_border, background=white, padx=10, pady=10)
        filters_frame.pack(fill="y", expand=True)

        filters_title = tk.Label(filters_frame, text="Filtros", font=title_font, bg=white, fg=blue, pady=17)
        filters_title.pack(pady=(0, 20))

        classify_label = tk.Label(filters_frame, text="Clasificar por:", font=label_font, bg=white, fg=blue)
        classify_label.pack(anchor="w", padx=10)

        self.classify_combo = ttk.Combobox(filters_frame, values=["Año", "Autor"], state="readonly", font=label_font)
        self.classify_combo.pack(fill="x", padx=10, pady=5)

        genre_button = tk.Button(filters_frame, text="Seleccionar género", command=self.select_genre, bg=blue, fg="white", font=button_font, relief=tk.FLAT)
        genre_button.pack(fill="x", padx=10, pady=(10, 20))

        sort_label = tk.Label(filters_frame, text="Ordenar por:", font=label_font, bg=white, fg=blue)
        sort_label.pack(anchor="w", padx=10)

        asc_button = tk.Button(filters_frame, text="Menor a mayor", command=self.sort_asc, bg=red, fg="white", font=button_font, relief=tk.FLAT)
        asc_button.pack(fill="x", padx=10, pady=8)

        desc_button = tk.Button(filters_frame, text="Mayor a menor", command=self.sort_desc, bg=red, fg="white", font=button_font, relief=tk.FLAT)
        desc_button.pack(fill="x", padx=10, pady=8)

        # Botón de regresar
        regresar_button = tk.Button(filters_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, relief=tk.FLAT)
        regresar_button.pack(fill="x", padx=10, pady=8)

        # Cargar libros al inicializar
        self.load_books()

    def load_books(self):
        self.book_list.delete(0, tk.END)
        for libro in self.libro_manager.listar_libros():
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})")

    def search_books(self):
        search_text = self.search_entry.get()
        resultados = self.libro_manager.buscar_libro("titulo", search_text)
        self.book_list.delete(0, tk.END)
        for libro in resultados:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})")

    def sort_asc(self):
        libros = sorted(self.libro_manager.listar_libros(), key=lambda x: x["titulo"])
        self.book_list.delete(0, tk.END)
        for libro in libros:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})")

    def sort_desc(self):
        libros = sorted(self.libro_manager.listar_libros(), key=lambda x: x["titulo"], reverse=True)
        self.book_list.delete(0, tk.END)
        for libro in libros:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})")

    def select_genre(self):
        genres = ["Ficción", "No ficción", "Ciencia", "Historia", "Fantasía", "Biografía"]
        selected_genre = simpledialog.askstring("Seleccionar género", f"Seleccione un género:\n{', '.join(genres)}")
        if selected_genre in genres:
            resultados = self.libro_manager.buscar_libro("genero", selected_genre)
            self.book_list.delete(0, tk.END)
            for libro in resultados:
                self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})")
        elif selected_genre is not None:
            messagebox.showwarning("Género no válido", "El género ingresado no es válido.")

    def regresar(self):
        """Cierra la ventana actual y regresa al menú principal."""
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])
