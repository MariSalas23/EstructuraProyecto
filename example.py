import tkinter as tk
from tkinter import font, ttk, simpledialog, messagebox

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda")
        self.root.geometry("1000x600")  # Ajusta el ancho a 1000 píxeles

        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        white = "#ffffff"
        title_font = font.Font(family="Open Sans", size=16, weight="bold")
        button_font = font.Font(family="Open Sans", size=12, weight="bold")
        label_font = font.Font(family="Open Sans", size=12)

        # Contenedor principal en dark_blue para el fondo
        background_frame = tk.Frame(self.root, background=dark_blue, padx=10, pady=10)
        background_frame.pack(fill="both", expand=True)

        # Marco exterior en rojo
        outer_frame = tk.Frame(background_frame, background=red, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Marco medio en azul
        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        # Marco interior en light_blue
        inner_frame = tk.Frame(middle_frame, background=light_blue, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Frame de búsqueda con borde estilo azul
        search_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        search_frame_border.pack(fill="x", padx=10, pady=10)
        
        search_frame = tk.Frame(search_frame_border, background=white, padx=10, pady=10)
        search_frame.pack(fill="x")
        
        search_label = tk.Label(search_frame, text="Buscar libros:", font=label_font, bg=white, fg=blue)
        search_label.pack(side="left", padx=5)
        
        self.search_entry = tk.Entry(search_frame, font=label_font, width=40)
        self.search_entry.pack(side="left", padx=5, expand=True, fill="x")
        
        search_button = tk.Button(search_frame, text="🔍", command=self.search_books,
                                  bg=red, fg="white", font=button_font, relief=tk.FLAT)
        search_button.pack(side="left", padx=5)

        # Frame de lista de libros con borde estilo azul
        book_list_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        book_list_frame_border.pack(fill="both", expand=True, padx=10, pady=10, side="left")
        
        book_list_frame = tk.Frame(book_list_frame_border, background=white, padx=10, pady=10)
        book_list_frame.pack(fill="both", expand=True)
        
        self.book_list = tk.Listbox(book_list_frame, width=60, height=20, bg=light_blue, font=label_font)
        self.book_list.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(book_list_frame, orient="vertical", command=self.book_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.book_list.config(yscrollcommand=scrollbar.set)

        # Panel de filtros con borde estilo azul, sin espacio extra
        filters_frame_border = tk.Frame(inner_frame, background=blue, padx=3, pady=3)
        filters_frame_border.pack(fill="y", side="right", padx=10, pady=10)
        
        filters_frame = tk.Frame(filters_frame_border, background=white, padx=10, pady=10)
        filters_frame.pack(fill="y", expand=True)
        
        filters_title = tk.Label(filters_frame, text="Filtros", font=title_font, bg=white, fg=blue)
        filters_title.pack(pady=(0, 20))
        
        # Clasificar por
        classify_label = tk.Label(filters_frame, text="Clasificar por:", font=label_font, bg=white, fg=blue)
        classify_label.pack(anchor="w", padx=10)
        
        self.classify_combo = ttk.Combobox(filters_frame, values=["Año", "Autor"], state="readonly", font=label_font)
        self.classify_combo.pack(fill="x", padx=10, pady=5)
        
        # Botón de seleccionar género
        genre_button = tk.Button(filters_frame, text="Seleccionar Género", command=self.select_genre,
                                 bg=blue, fg="white", font=button_font, relief=tk.FLAT)
        genre_button.pack(fill="x", padx=10, pady=(10, 20))
        
        # Ordenar por
        sort_label = tk.Label(filters_frame, text="Ordenar por:", font=label_font, bg=white, fg=blue)
        sort_label.pack(anchor="w", padx=10)
        
        asc_button = tk.Button(filters_frame, text="Menor a mayor", command=self.sort_asc,
                               bg=red, fg="white", font=button_font, relief=tk.FLAT)
        asc_button.pack(fill="x", padx=10, pady=5)
        
        desc_button = tk.Button(filters_frame, text="Mayor a menor", command=self.sort_desc,
                                bg=red, fg="white", font=button_font, relief=tk.FLAT)
        desc_button.pack(fill="x", padx=10, pady=5)

    def search_books(self):
        # Implementación de búsqueda
        pass

    def sort_asc(self):
        # Implementación de orden ascendente
        pass

    def sort_desc(self):
        # Implementación de orden descendente
        pass

    def select_genre(self):
        genres = ["Ficción", "No ficción", "Ciencia", "Historia", "Fantasía", "Biografía"]
        selected_genre = simpledialog.askstring("Seleccionar Género", f"Seleccione un género:\n{', '.join(genres)}")
        
        if selected_genre in genres:
            messagebox.showinfo("Género seleccionado", f"Ha seleccionado el género: {selected_genre}")
        elif selected_genre is not None:
            messagebox.showwarning("Género no válido", "El género ingresado no es válido.")
