import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, font

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda")
        self.root.geometry("800x500")
        
        # Configuración de colores
        main_bg = "#D0FBFF"  # Fondo principal
        frame_bg = "#E5FDFE"  # Fondo de los frames
        border_color = "#6ECBD4"  # Color de borde para resaltar el borde sutilmente
        button_bg = "#6ECBD4"  # Fondo de los botones
        button_active_bg = "#4BAAB2"  # Fondo de los botones activos
        button_fg = "white"  # Color de texto en los botones
        
        # Configuración de fuente personalizada
        custom_font = font.Font(family="Helvetica", size=12, weight="bold")
        custom_font2 = font.Font(family="Helvetica", size=12)
        
        # Fondo principal
        self.root.configure(background=main_bg)
        
        # Configuración de columnas y filas en el contenedor principal
        self.root.columnconfigure(0, weight=3, minsize=550)  # Área de lista de libros (ancho mínimo 550px)
        self.root.columnconfigure(1, weight=1, minsize=250)  # Área de filtros (ancho mínimo 250px)
        self.root.rowconfigure(1, weight=1)
        
        # Frame de búsqueda en la parte superior con diseño
        search_frame = tk.Frame(self.root, background=border_color, padx=3, pady=3)
        search_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
        
        inner_search_frame = tk.Frame(search_frame, background=frame_bg)
        inner_search_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        search_label = tk.Label(inner_search_frame, text="Buscar libros:", font=custom_font, bg=frame_bg, fg=border_color)
        search_label.grid(row=0, column=0, padx=5)
        
        self.search_entry = tk.Entry(inner_search_frame, font=custom_font2, width=50)
        self.search_entry.grid(row=0, column=1, padx=5, sticky="ew")
        
        search_button = tk.Button(inner_search_frame, text="🔍", command=self.search_books,
                                  bg=button_bg, fg=button_fg, font=custom_font, activebackground=button_active_bg,
                                  activeforeground="white", relief="flat")
        search_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame para la lista de libros (izquierda)
        book_list_frame = tk.Frame(self.root, background=border_color, padx=3, pady=3)
        book_list_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        inner_book_frame = tk.Frame(book_list_frame, background=frame_bg)
        inner_book_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Listbox y scrollbar en el frame interno
        self.book_list = tk.Listbox(inner_book_frame, width=80, height=30, bg=frame_bg, font=custom_font2)
        self.book_list.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(inner_book_frame, orient="vertical", command=self.book_list.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.book_list.config(yscrollcommand=scrollbar.set)
        inner_book_frame.grid_columnconfigure(0, weight=1)
        inner_book_frame.grid_rowconfigure(0, weight=1)
        
        # Panel de filtros (derecha)
        filters_frame = tk.Frame(self.root, background=border_color, padx=3, pady=3)
        filters_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        
        # Añadir padding a la izquierda (10px) en el frame interno de filtros
        inner_filters_frame = tk.Frame(filters_frame, background=frame_bg)
        inner_filters_frame.pack(fill="both", expand=True, padx=(10, 0), pady=5)
        
        filters_title = tk.Label(inner_filters_frame, text="Filtros", font=custom_font, bg=frame_bg, fg=border_color)
        filters_title.grid(row=0, column=0, pady=(0, 20), sticky="ew", padx=(10, 0))
        
        # Clasificar por
        classify_label = tk.Label(inner_filters_frame, text="Clasificar por:", font=custom_font2, bg=frame_bg)
        classify_label.grid(row=1, column=0, sticky="w", pady=(0, 5), padx=(20, 0))
        
        self.classify_combo = ttk.Combobox(inner_filters_frame, values=["Año", "Autor"], state="readonly")
        self.classify_combo.grid(row=2, column=0, padx=(20, 0), pady=5, sticky="ew")
        
        # Botón de seleccionar género
        genre_button = tk.Button(inner_filters_frame, text="Seleccionar Género", command=self.select_genre,
                                 bg=button_bg, fg=button_fg, font=custom_font2, activebackground=button_active_bg,
                                 activeforeground="white", relief="flat")
        genre_button.grid(row=3, column=0, pady=(20, 20), sticky="ew", padx=(20, 0))
        
        # Ordenar por
        sort_label = tk.Label(inner_filters_frame, text="Ordenar por:", font=custom_font2, bg=frame_bg)
        sort_label.grid(row=4, column=0, sticky="w", pady=(20, 5), padx=(20, 0))
        
        asc_button = tk.Button(inner_filters_frame, text="Menor a mayor", command=self.sort_asc,
                               bg=button_bg, fg=button_fg, font=custom_font2, activebackground=button_active_bg,
                               activeforeground="white", relief="flat")
        asc_button.grid(row=5, column=0, pady=5, sticky="ew", padx=(20, 0))
        
        desc_button = tk.Button(inner_filters_frame, text="Mayor a menor", command=self.sort_desc,
                                bg=button_bg, fg=button_fg, font=custom_font2, activebackground=button_active_bg,
                                activeforeground="white", relief="flat")
        desc_button.grid(row=6, column=0, pady=5, sticky="ew", padx=(20, 0))

    def search_books(self):
        pass

    def sort_asc(self):
        pass

    def sort_desc(self):
        pass

    def select_genre(self):
        genres = ["Ficción", "No ficción", "Ciencia", "Historia", "Fantasía", "Biografía"]
        selected_genre = simpledialog.askstring("Seleccionar Género", f"Seleccione un género:\n{', '.join(genres)}")
        
        if selected_genre in genres:
            messagebox.showinfo("Género seleccionado", f"Ha seleccionado el género: {selected_genre}")
        elif selected_genre is not None:
            messagebox.showwarning("Género no válido", "El género ingresado no es válido.")
