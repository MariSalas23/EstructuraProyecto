import tkinter as tk
from tkinter import font, messagebox
from libro import agregar_libro, eliminar_libro, buscar_libro, listar_libros

class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Biblioteca")
        self.window.geometry("400x265")
        
        # Cambiar el color de fondo de la ventana principal usando un color hexadecimal
        self.window.configure(background="#E9D0FF")
        
        # Definir una fuente personalizada
        custom_font = font.Font(family="Helvetica", size=12, weight="bold")
        custom_font2 = font.Font(family="Helvetica", size=12)
        
        # Crear un Frame con el mismo color de fondo
        main_frame = tk.Frame(self.window, background="#E9D0FF")
        main_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Crear Labels con borde
        self.create_bordered_label(main_frame, "Menú", custom_font, "#F1E1FE", "#8145A4")
        self.create_bordered_label(main_frame, "¿Qué acción desea?", custom_font2, "#F1E1FE", "#8145A4")
        
        # Frame para agrupar los botones con borde
        bordered_frame = tk.Frame(main_frame, background="#8145A4", padx=2, pady=2)
        bordered_frame.pack(pady=10, fill=tk.BOTH, padx=20)
        
        # Frame interno con fondo morado claro para los botones
        inner_frame = tk.Frame(bordered_frame, background="#F1E1FE")
        inner_frame.pack(fill=tk.BOTH, expand=True)

        # Configurar columnas para centrar los botones
        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(1, weight=1)

        # Crear botones dentro del inner_frame en una cuadrícula 2x2
        self.create_button(inner_frame, "Inserción", self.open_insert_interface, row=0, column=0)
        self.create_button(inner_frame, "Búsqueda", self.open_search_interface, row=0, column=1)
        self.create_button(inner_frame, "Eliminación", self.open_delete_interface, row=1, column=0)
        self.create_button(inner_frame, "Visualización", self.open_display_interface, row=1, column=1)

    def create_bordered_label(self, parent, text, font, bg_color, border_color):
        # Frame para el borde del Label
        border_frame = tk.Frame(parent, background=border_color, padx=2, pady=2)
        border_frame.pack(pady=10, fill=tk.X, padx=20)
        
        # Label dentro del frame con borde
        label = tk.Label(border_frame, text=text, font=font, background=bg_color, foreground=border_color)
        label.pack(fill=tk.X)

    def create_button(self, parent, text, command, row, column):
        tk.Button(parent, text=text, command=command,
                  bg="#8145A4", fg="white", font=("Helvetica", 12), width=15,
                  relief=tk.FLAT, activebackground="#5A2B8A", activeforeground="white").grid(
                      row=row, column=column, padx=10, pady=8, sticky='ew')

    def open_insert_interface(self):
        self.show_message("Inserción", agregar_libro("978-1-4028-9462-6", "To Kill a Mockingbird", "Harper Lee", "Ficción", 1960, 4))

    def open_search_interface(self):
        self.show_message("Búsqueda", buscar_libro("978-1-4028-9462-6"))

    def open_delete_interface(self):
        self.show_message("Eliminación", eliminar_libro("978-1-4028-9462-6"))

    def open_display_interface(self):
        self.show_message("Visualización", listar_libros())

    def show_message(self, title, message):
        if isinstance(message, dict):
            message = "\n".join(f"{k}: {v}" for k, v in message.items())
        messagebox.showinfo(title, message)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MainInterface()
    app.run()



