from tkinter import font, ttk, simpledialog, messagebox
import tkinter as tk
from libro import Libro  # Importar la clase Libro desde libro.py
from metodos import ordenamiento_burbuja, ordenamiento_insercion, ordenamiento_seleccion, merge_sort, busqueda_binaria
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

        self.classify_combo = ttk.Combobox(filters_frame, values=["Título", "Año", "Autor", "Género"], state="readonly", font=label_font)
        self.classify_combo.set("Título")  # Selección por defecto: "Título"
        self.classify_combo.pack(fill="x", padx=10, pady=5)

        # Asociar evento al Combobox para habilitar/inhiblar el botón según el filtro
        self.classify_combo.bind("<<ComboboxSelected>>", self.update_genre_button_state)

        # Configurar el botón "Seleccionar Género" e inhabilitarlo por defecto
        self.genre_button = tk.Button(filters_frame, text="Seleccionar Género", command=self.select_genre, bg=blue, fg="white", font=button_font, relief=tk.FLAT)
        self.genre_button.pack(fill="x", padx=10, pady=(20, 20))
        self.genre_button.config(state="disabled")  # Inhabilitar por defecto

        asc_button = tk.Button(filters_frame, text="Menor a Mayor", command=self.sort_asc, bg=red, fg="white", font=button_font, relief=tk.FLAT)
        asc_button.pack(fill="x", padx=10, pady=8)

        desc_button = tk.Button(filters_frame, text="Mayor a Menor", command=self.sort_desc, bg=red, fg="white", font=button_font, relief=tk.FLAT)
        desc_button.pack(fill="x", padx=10, pady=8)

        regresar_button = tk.Button(filters_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, relief=tk.FLAT)
        regresar_button.pack(fill="x", padx=10, pady=20)

        # Cargar y mostrar libros al inicializar
        self.load_books()

    def load_books(self):
        libros = self.libro_manager.listar_libros()
        libros_ordenados = ordenamiento_burbuja(libros, key=lambda x: x["titulo"])
        self.book_list.delete(0, tk.END)
        for libro in libros_ordenados:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")

    def sort_asc(self):
        """Ordenar libros de menor a mayor según el campo seleccionado."""
        campo = self.classify_combo.get().lower()
        libros = self.libro_manager.listar_libros()

        # Seleccionar el método de ordenamiento según el campo
        if campo == "año":
            libros_ordenados = merge_sort(libros, key=lambda x: int(x["fecha"]))
        elif campo == "autor":
            libros_ordenados = ordenamiento_insercion(libros, key=lambda x: x["autor"].lower())
        elif campo == "género":
            libros_ordenados = ordenamiento_seleccion(libros, key=lambda x: x["genero"].lower())
        else:
            libros_ordenados = ordenamiento_burbuja(libros, key=lambda x: x["titulo"].lower())

        # Mostrar libros ordenados
        self.book_list.delete(0, tk.END)
        for libro in libros_ordenados:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")

    def sort_desc(self):
        """Ordenar libros de mayor a menor según el campo seleccionado."""
        campo = self.classify_combo.get().lower()
        libros = self.libro_manager.listar_libros()

        # Seleccionar el método de ordenamiento según el campo
        if campo == "año":
            libros_ordenados = merge_sort(libros, key=lambda x: int(x["fecha"]))
        elif campo == "autor":
            libros_ordenados = ordenamiento_insercion(libros, key=lambda x: x["autor"].lower())
        elif campo == "género":
            libros_ordenados = ordenamiento_seleccion(libros, key=lambda x: x["genero"].lower())
        else:
            libros_ordenados = ordenamiento_burbuja(libros, key=lambda x: x["titulo"].lower())

        # Invertir el orden para mayor a menor
        libros_ordenados.reverse()

        # Mostrar libros ordenados
        self.book_list.delete(0, tk.END)
        for libro in libros_ordenados:
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")

    def search_books(self):
        """Buscar libros según el campo seleccionado."""
        campo = self.classify_combo.get().lower()  # Obtener el campo seleccionado
        valor = self.search_entry.get().strip().upper()  # Convertir el valor ingresado a MAYÚSCULAS

        libros = self.libro_manager.listar_libros()  # Obtener todos los libros

        # Mapear los campos seleccionados a las claves reales en los datos
        campo_mapeado = {
            "título": "titulo",
            "año": "fecha",
            "autor": "autor",
            "género": "genero"
        }.get(campo)

        if not campo_mapeado:
            messagebox.showerror("Error", "El campo seleccionado no es válido para buscar.")
            return

        # Si el input está vacío, mostrar todos los libros ordenados según el filtro
        if not valor:
            if campo_mapeado == "fecha":
                libros_ordenados = merge_sort(libros, key=lambda x: int(x["fecha"]))
            elif campo_mapeado == "autor":
                libros_ordenados = ordenamiento_insercion(libros, key=lambda x: x["autor"])
            elif campo_mapeado == "genero":
                libros_ordenados = ordenamiento_seleccion(libros, key=lambda x: x["genero"])
            else:  # Por defecto, "Titulo"
                libros_ordenados = ordenamiento_burbuja(libros, key=lambda x: x["titulo"])

            # Mostrar todos los libros ordenados
            self.book_list.delete(0, tk.END)
            for libro in libros_ordenados:
                self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")
            return

        # Si el input tiene un valor, realizar la búsqueda binaria
        if campo_mapeado == "fecha":
            try:
                valor = int(valor)  # Convertir a entero para buscar por año
                libros_ordenados = merge_sort(libros, key=lambda x: int(x["fecha"]))
            except ValueError:
                messagebox.showerror("Error", "El valor ingresado para 'Año' debe ser numérico.")
                return
        elif campo_mapeado == "autor":
            libros_ordenados = ordenamiento_insercion(libros, key=lambda x: x["autor"])
        elif campo_mapeado == "genero":
            libros_ordenados = ordenamiento_seleccion(libros, key=lambda x: x["genero"])
        elif campo_mapeado == "titulo":
            libros_ordenados = ordenamiento_burbuja(libros, key=lambda x: x["titulo"])
        else:
            messagebox.showerror("Error", "El campo seleccionado no es válido para buscar.")
            return

        # Realizar la búsqueda binaria
        try:
            indice = busqueda_binaria(libros_ordenados, valor, key=lambda x: x[campo_mapeado])
        except KeyError:
            messagebox.showerror("Error", "El campo seleccionado no es válido para buscar.")
            return

        # Mostrar el resultado de la búsqueda
        self.book_list.delete(0, tk.END)
        if indice != -1:
            libro = libros_ordenados[indice]
            self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")
        else:
            self.book_list.insert(tk.END, "No se encontraron resultados.")

    def select_genre(self):
        """Filtrar libros por género seleccionado."""
        genres = list(set([libro["genero"] for libro in self.libro_manager.listar_libros()]))
        selected_genre = simpledialog.askstring("Seleccionar Género", f"Seleccione un género:\n{', '.join(genres)}")

        if selected_genre in genres:
            libros = [libro for libro in self.libro_manager.listar_libros() if libro["genero"] == selected_genre]
            self.book_list.delete(0, tk.END)
            for libro in libros:
                self.book_list.insert(tk.END, f"{libro['titulo']} - {libro['autor']} ({libro['fecha']})")
        else:
            messagebox.showwarning("Género no válido", "El género ingresado no es válido.")

    def update_genre_button_state(self, event):
        """Habilitar o inhabilitar el botón de seleccionar género."""
        if self.classify_combo.get().lower() == "género":
            self.genre_button.config(state="normal")  # Habilitar
        else:
            self.genre_button.config(state="disabled")  # Inhabilitar


    def select_genre(self):
        """Seleccionar un género de una lista numerada."""
        genres = [
            "1. ROMANCE",
            "2. FANTASÍA",
            "3. MISTERIO",
            "4. BIOGRAFÍA",
            "5. HISTORIA",
            "6. ENSAYO",
            "7. POESÍA ÉPICA",
            "8. POESÍA LÍRICA",
            "9. POESÍA CONTEMPLATIVA"
        ]

        while True:
            selected_number = simpledialog.askstring(
                "Seleccionar Género",
                "Seleccione el número del género:\n" + "\n".join(genres)
            )

            if not selected_number:
                break  # Cancelar selección

            try:
                selected_number = int(selected_number)
                if 1 <= selected_number <= 9:
                    genre = genres[selected_number - 1].split(". ")[1]
                    self.search_entry.delete(0, tk.END)
                    self.search_entry.insert(0, genre)
                    break
                else:
                    messagebox.showerror("Error", "Seleccione un número válido entre 1 y 9.")
            except ValueError:
                messagebox.showerror("Error", "Debe ingresar un número válido.")

    def regresar(self):
        """Cerrar la ventana actual y volver al menú principal."""
        self.root.destroy()  # Cierra la ventana actual
        subprocess.Popen(["python", "main.py"])
