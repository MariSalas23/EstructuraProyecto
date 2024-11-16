import tkinter as tk
from tkinter import font, messagebox, simpledialog
import subprocess


class NAryNode:
    def __init__(self, value, question=None):
        self.value = value
        self.children = []
        self.question = question

    def add_child(self, child_node):
        self.children.append(child_node)


class GenreTree:
    def __init__(self):
        self.root = NAryNode("Literatura", "¿Qué tipo de lectura estás buscando?")
        self._build_tree()

    def _build_tree(self):
        fiction = NAryNode("Ficción", "¿Qué tipo de historia prefieres?")
        non_fiction = NAryNode("No Ficción", "¿Qué te interesa explorar?")
        poetry = NAryNode("Poesía", "¿Qué estilo prefieres?")
        self.root.add_child(fiction)
        self.root.add_child(non_fiction)
        self.root.add_child(poetry)

        fiction.add_child(NAryNode("Romance"))
        fiction.add_child(NAryNode("Fantasía"))
        fiction.add_child(NAryNode("Misterio"))

        non_fiction.add_child(NAryNode("Biografía"))
        non_fiction.add_child(NAryNode("Historia"))
        non_fiction.add_child(NAryNode("Ensayo"))

        poetry.add_child(NAryNode("Poesía Épica"))
        poetry.add_child(NAryNode("Poesía Lírica"))
        poetry.add_child(NAryNode("Poesía Contemplativa"))

    def guided_search(self, node):
        if not node.children:
            return node.value

        root = tk.Tk()
        root.withdraw()
        options = {i + 1: child.value for i, child in enumerate(node.children)}
        options_text = "\n".join([f"{i}. {v}" for i, v in options.items()])
        choice = simpledialog.askinteger("Elección", f"{node.question}\n\n{options_text}")
        root.destroy()

        if choice in options:
            selected_child = node.children[choice - 1]
            return self.guided_search(selected_child)
        else:
            return "Selección no válida. Por favor, intenta de nuevo."

    def find_genre(self):
        return self.guided_search(self.root)


class InsertWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar")
        self.root.geometry("452x482")

        # Configuración de colores y fuentes
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_blue = "#b5ccd2"
        light_red = "#f5e2e4"
        button_font = font.Font(family="Open Sans", size=12, weight="bold")
        title_font = font.Font(family="Open Sans", size=20, weight="bold")

        # Árbol de géneros
        self.genre_tree = GenreTree()
        self.selected_genre = tk.StringVar()

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

        tk.Label(content_frame, text="Agregar Libro", font=title_font, bg=light_red, fg=blue).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        fields = ["ISBN", "Título", "Autor", "Año Publicación", "Cantidad"]
        self.entries = {}

        for i, field in enumerate(fields):
            tk.Label(content_frame, text=field, bg=light_red, fg=blue).grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(content_frame)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries[field] = entry

        # Botón para seleccionar género
        tk.Label(content_frame, text="Género", bg=light_red, fg=blue).grid(row=len(fields) + 1, column=0, sticky="w", padx=10, pady=5)
        tk.Button(content_frame, text="Seleccionar Género", command=self.select_genre, bg=blue, fg="white", font=button_font).grid(row=len(fields) + 1, column=1, padx=10, pady=5)

        # Mostrar género seleccionado
        tk.Label(content_frame, textvariable=self.selected_genre, bg=light_red, fg=red).grid(row=len(fields) + 2, column=0, columnspan=2, pady=(5, 10))

        button_frame = tk.Frame(content_frame, background=light_red)
        button_frame.grid(row=len(fields) + 3, column=0, columnspan=2, pady=(25, 10))

        tk.Button(button_frame, text="Agregar", command=self.agregar_libro, bg=red, fg="white", font=button_font, width=11, height=1, relief=tk.FLAT).pack(side="left", padx=10)
        tk.Button(button_frame, text="Regresar", command=self.regresar, bg=blue, fg="white", font=button_font, width=11, height=1, relief=tk.FLAT).pack(side="left", padx=10)

    def select_genre(self):
        genre = self.genre_tree.find_genre()
        self.selected_genre.set(f"Género seleccionado: {genre}")

    def agregar_libro(self):
        try:
            isbn = self.entries["ISBN"].get()
            titulo = self.entries["Título"].get()
            autor = self.entries["Autor"].get()
            año_publicacion = int(self.entries["Año Publicación"].get())
            cantidad = int(self.entries["Cantidad"].get())
            genero = self.selected_genre.get()

            mensaje = f"Libro agregado: {titulo} ({año_publicacion}) - {genero}"
            messagebox.showinfo("Resultado", mensaje)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en los campos numéricos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def regresar(self):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])


if __name__ == "__main__":
    root = tk.Tk()
    app = InsertWindow(root)
<<<<<<< Updated upstream
    root.mainloop()
=======
    root.mainloop()
>>>>>>> Stashed changes
