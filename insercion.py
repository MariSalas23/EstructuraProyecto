import tkinter as tk
from tkinter import font, messagebox
import subprocess

class InsertWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar")
        self.root.geometry("452x482")  # Ajustar el tamaño para acomodar el contenedor adicional
        
        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        light_red = "#f5e2e4"
        white = "#ffffff"
        button_font = font.Font(family="Open Sans", size=12, weight="bold")
        title_font = font.Font(family="Open Sans", size=20, weight="bold")

        background_frame = tk.Frame(self.root, background=light_blue, padx=10, pady=10)
        background_frame.pack(fill="both", expand=True)

        outer_frame = tk.Frame(background_frame, background=dark_blue, padx=10, pady=10)
        outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

        middle_frame = tk.Frame(outer_frame, background=blue, padx=5, pady=5)
        middle_frame.pack(fill="both", expand=True)

        inner_frame = tk.Frame(middle_frame, background=red, padx=20, pady=20)
        inner_frame.pack(fill="both", expand=True)

        # Contenedor blanco dentro del inner_frame para el formulario
        content_frame = tk.Frame(inner_frame, background=light_red, padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Título del formulario con mayor separación abajo
        tk.Label(content_frame, text="Agregar Libro", font=title_font, bg=light_red, fg=blue).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Campos del formulario
        fields = ["ISBN", "Título", "Autor", "Género", "Año Publicación", "Cantidad"]
        self.entries = {}

        for i, field in enumerate(fields):
            tk.Label(content_frame, text=field, bg=light_red, fg=blue).grid(row=i+1, column=0, sticky="w", padx=10, pady=5)
            
            # Validación para que el ISBN solo acepte números
            if field == "ISBN":
                entry = tk.Entry(content_frame, validate="key")
                entry.config(validatecommand=(self.root.register(self.only_numbers), "%P"))
            else:
                entry = tk.Entry(content_frame)
            
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.entries[field] = entry

        # Botones "Agregar" y "Regresar" en la misma fila con más espacio respecto al formulario
        button_frame = tk.Frame(content_frame, background=light_red)
        button_frame.grid(row=len(fields)+2, column=0, columnspan=2, pady=(25, 10))

        tk.Button(button_frame, text="Agregar", command=self.agregar_libro, bg=red, fg="white", font=button_font, width=11, height=1, relief=tk.FLAT).pack(side="left", padx=10)
        tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, width=11, height=1, relief=tk.FLAT).pack(side="left", padx=10)

    def only_numbers(self, text):
        return text.isdigit() or text == ""

    def agregar_libro(self):
        try:
            isbn = self.entries["ISBN"].get()
            titulo = self.entries["Título"].get()
            autor = self.entries["Autor"].get()
            genero = self.entries["Género"].get()
            año_publicacion = int(self.entries["Año Publicación"].get())
            cantidad = int(self.entries["Cantidad"].get())

            mensaje = f"Libro agregado: {titulo} ({año_publicacion})"
            messagebox.showinfo("Resultado", mensaje)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en los campos numéricos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def regresar(self):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])
