import tkinter as tk
from tkinter import font, messagebox
from libro import Libro
from BalancedTree import BalancedTree 

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Biblioteca")
        self.window.geometry("600x500")
        self.window.configure(background="#E9D0FF")
        
        self.libro = Libro()
        self.arbol = BalancedTree()  ##aqui lo que deben hacer es crear otros archivos
        #self.arboln= NarioTree()
        #self.arbolB=BinarioTree()
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        custom_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        titulo_label = tk.Label(self.window, text="Biblioteca", font=custom_font, bg="#E9D0FF", fg="#8145A4")
        titulo_label.pack(pady=10)

        subtitulo_label = tk.Label(self.window, text="¿Qué desea hacer?", font=custom_font, bg="#E9D0FF", fg="#8145A4")
        subtitulo_label.pack(pady=10)
        
        # Frame de opciones
        opciones_frame = tk.Frame(self.window, background="#F1E1FE", pady=10)
        opciones_frame.pack(fill=tk.BOTH, padx=20)
        
        # Botones principales
        tk.Button(opciones_frame, text="Agregar Libro", command=self.mostrar_formulario_agregar, 
                  bg="#8145A4", fg="white", font=("Helvetica", 12), width=15).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(opciones_frame, text="Buscar Libro", command=self.mostrar_formulario_buscar, 
                  bg="#8145A4", fg="white", font=("Helvetica", 12), width=15).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(opciones_frame, text="Visualización", command=self.mostrar_formulario_ver, 
                  bg="#8145A4", fg="white", font=("Helvetica", 12), width=15).grid(row=1, column=0, padx=10, pady=5)
        
        tk.Button(opciones_frame, text="Ordenar por Año", command=self.mostrar_formulario_ordenamiento, 
                  bg="#8145A4", fg="white", font=("Helvetica", 12), width=15).grid(row=1, column=1, padx=10, pady=5)

        self.resultados_frame = tk.Frame(self.window, bg="#E9D0FF")
        self.resultados_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def mostrar_formulario_agregar(self):
        
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.resultados_frame, text="Agregar Libro", bg="#E9D0FF", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Entradas de datos
        fields = ["ISBN", "Título", "Autor", "Género", "Año Publicación", "Cantidad"]
        self.entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(self.resultados_frame, text=field, bg="#E9D0FF").grid(row=i+1, column=0, sticky="w")
            entry = tk.Entry(self.resultados_frame)
            entry.grid(row=i+1, column=1)
            self.entries[field] = entry
        
        tk.Button(self.resultados_frame, text="Agregar", command=self.agregar_libro, bg="#8145A4", fg="white").grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

    def agregar_libro(self):
        isbn = self.entries["ISBN"].get()
        titulo = self.entries["Título"].get()
        autor = self.entries["Autor"].get()
        genero = self.entries["Género"].get()
        año_publicacion = int(self.entries["Año Publicación"].get())
        cantidad = int(self.entries["Cantidad"].get())

        mensaje = self.libro.agregar_libro(isbn, titulo, autor, genero, año_publicacion, cantidad)
        self.arbol.insert(año_publicacion)  
        messagebox.showinfo("Resultado", mensaje)

    def mostrar_formulario_buscar(self):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        # Formulario para buscar libros
        tk.Label(self.resultados_frame, text="Buscar Libro", bg="#E9D0FF", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        # Selección de criterio de búsqueda
        tk.Label(self.resultados_frame, text="Criterio:", bg="#E9D0FF").grid(row=1, column=0, sticky="w")
        self.criterio_var = tk.StringVar()
        self.criterio_var.set("titulo")
        criterios = ["titulo", "autor", "genero", "año_publicacion"]
        self.criterio_menu = tk.OptionMenu(self.resultados_frame, self.criterio_var, *criterios)
        self.criterio_menu.grid(row=1, column=1, sticky="w")
        
        # Entrada de valor de búsqueda
        tk.Label(self.resultados_frame, text="Valor:", bg="#E9D0FF").grid(row=2, column=0, sticky="w")
        self.valor_entry = tk.Entry(self.resultados_frame)
        self.valor_entry.grid(row=2, column=1, sticky="w")
        
        tk.Button(self.resultados_frame, text="Buscar", command=self.buscar_libro, bg="#8145A4", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

    def buscar_libro(self):
        criterio = self.criterio_var.get()
        valor = self.valor_entry.get()
        resultados = self.libro.buscar_libro(criterio, valor)
        
        if resultados:
            resultados_texto = "\n".join([f"{libro['titulo']} - {libro['autor']} ({libro['año_publicacion']})" for libro in resultados])
            messagebox.showinfo("Resultados", resultados_texto)
        else:
            messagebox.showinfo("Resultados", "No se encontraron libros.")

    def mostrar_formulario_ordenamiento(self):
        
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.resultados_frame, text="Ordenar Libros por Año", bg="#E9D0FF", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Botones para ver los árboles
        tk.Button(self.resultados_frame, text="Ver Árbol Binario", command=self.mostrar_arbol_binario, 
                  bg="#8145A4", fg="white").grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.resultados_frame, text="Ver Árbol N-ario", command=self.mostrar_arbol_n_ari, 
                  bg="#8145A4", fg="white").grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.resultados_frame, text="Ver Árbol Balanceado", command=self.mostrar_arbol_balanceado, 
                  bg="#8145A4", fg="white").grid(row=2, column=0, columnspan=2, pady=10)
    def mostrar_formulario_ver(self):
        pass
    def mostrar_arbol_binario(self):
        messagebox.showinfo("Árbol Binario", "El árbol binario aún no está implementado.")

    def mostrar_arbol_n_ari(self):
        messagebox.showinfo("Árbol N-ario", "El árbol N-ario aún no está implementado.")

    def mostrar_arbol_balanceado(self):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        tk.Label(self.resultados_frame, text="Libros Ordenados por Año de Publicación", bg="#E9D0FF", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)

        libros_ordenados = self.arbol.get_level_order()  
        
        if libros_ordenados:
            resultados_texto = "\n".join([str(libro) for libro in libros_ordenados])
            messagebox.showinfo("Libros Ordenados", resultados_texto)
        else:
            messagebox.showinfo("Libros Ordenados", "No hay libros en el árbol.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__": 
    app = Main()
    app.run()
