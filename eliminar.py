import tkinter as tk
from tkinter import messagebox, font
import subprocess  # Para abrir main.py nuevamente

class DeleteWindow:
    def __init__(self, root, libro_manager):
        self.root = root
        self.libro_manager = libro_manager
        self.root.title("Eliminar")
        self.root.geometry("470x360")

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
            result = self.libro_manager.eliminar_libro(isbn)
            messagebox.showinfo("Resultado", result)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un ISBN válido.")

    def regresar(self):
        self.root.destroy()  # Cierra la ventana actual
        subprocess.Popen(["python", "main.py"])  # Vuelve a lanzar la ventana principal
