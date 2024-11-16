import tkinter as tk
from tkinter import simpledialog

class NAryNode:
    def __init__(self, value, question=None):
        self.value = value
        self.children = []
        self.question = question  # Pregunta dependiendo del nodo en el que esté el usuario

    def add_child(self, child_node):
        self.children.append(child_node)

class GenreTree:
    def __init__(self):
        self.root = NAryNode("Literatura", "¿Qué tipo de lectura estás buscando?")
        self._build_tree()

    def _build_tree(self):
        # nodo inicial
        fiction = NAryNode("Ficción", "¿Qué tipo de historia prefieres?")
        non_fiction = NAryNode("No Ficción", "¿Qué te interesa explorar?")
        poetry = NAryNode("Poesía", "¿Qué estilo prefieres?")
        self.root.add_child(fiction)
        self.root.add_child(non_fiction)
        self.root.add_child(poetry)

        # nodo de ficción
        fiction.add_child(NAryNode("Romance"))
        fiction.add_child(NAryNode("Fantasía"))
        fiction.add_child(NAryNode("Misterio"))

        # nodo de no-ficción
        non_fiction.add_child(NAryNode("Biografía"))
        non_fiction.add_child(NAryNode("Historia"))
        non_fiction.add_child(NAryNode("Ensayo"))

        # nodo para poesía
        poetry.add_child(NAryNode("Poesía Épica"))
        poetry.add_child(NAryNode("Poesía Lírica"))
        poetry.add_child(NAryNode("Poesía Contemplativa"))

    def guided_search(self, node):
        if not node.children:
            return node.value  # Nodo hoja: género encontrado
        
        # Mostrar mensajes
        root = tk.Tk()
        root.withdraw()
        # Enumerar las opciones (los hijos de cada nodo)
        options = {i+1: child.value for i, child in enumerate(node.children)}
        # Opciones en formato de lista
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

# Asegurarse de que este código solo se ejecute si el archivo se ejecuta directamente
if __name__ == "__main__":
    genre_tree = GenreTree()
    print("Género seleccionado:", genre_tree.find_genre())
