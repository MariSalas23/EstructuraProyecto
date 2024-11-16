import tkinter as tk
from tkinter import font, messagebox
import subprocess
from libro import Libro

class DeleteWindow:
    def __init__(self, root, libro_instance):
        self.root = root
        self.root.title("Eliminar Libro")
        self.root.geometry("400x320")
        self.libro_instance = libro_instance
        
        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        white = "#ffffff"
        title_font = font.Font(family="Open Sans", size=16, weight="bold")
        label_font = font.Font(family="Open Sans", size=12)

        # Crear el marco exterior en rojo
        outer_frame = tk.Frame(self.root, background=red, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Crear el marco medio en azul
        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        # Crear el marco interior en light_blue
        inner_frame = tk.Frame(middle_frame, background=light_blue, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Contenedor blanco dentro del inner_frame para el formulario
        content_frame = tk.Frame(inner_frame, background=white, padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Título de la ventana
        title_label = tk.Label(content_frame, text="Eliminar Libro", font=title_font, bg=white, fg=blue)
        title_label.pack(pady=(0, 10))

        # Etiqueta e ingreso de ISBN
        isbn_label = tk.Label(content_frame, text="Ingrese ISBN del libro a eliminar:", font=label_font, bg=white, fg=dark_blue)
        isbn_label.pack(pady=5)
        
        self.isbn_entry = tk.Entry(content_frame, font=label_font, width=30)
        self.isbn_entry.pack(pady=5)

        # Frame para los botones en el contenedor blanco
        button_frame = tk.Frame(content_frame, background=white)
        button_frame.pack(pady=(20, 0))

        # Botón de eliminar
        delete_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_libro, bg=red, fg="white", font=label_font, relief=tk.FLAT, width=10)
        delete_button.grid(row=0, column=0, padx=5)

        # Botón de regresar
        back_button = tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=label_font, relief=tk.FLAT, width=10)
        back_button.grid(row=0, column=1, padx=5)

    def eliminar_libro(self):
        isbn = self.isbn_entry.get()
        if not isbn:
            messagebox.showerror("Error", "Debe ingresar un ISBN válido.")
            return
        resultado = self.libro_instance.eliminarLibro(isbn)  
        messagebox.showinfo("Resultado", resultado)

    def regresar(self):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"]) 
