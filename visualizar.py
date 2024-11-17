import tkinter as tk
from tkinter import font
import networkx as nx
import matplotlib.pyplot as plt
from libro import Libro

class Visualizar:
    def __init__(self, libro_manager):
        self.libro_manager = libro_manager

    def crear_grafo(self):
        """Crea el grafo de relaciones basado en los datos del libro."""
        self.graph = nx.Graph()

        libros = self.libro_manager.listar_libros()

        for libro in libros:
            titulo = libro['titulo']
            autor = libro['autor']
            genero = libro['genero']
            fecha = libro['fecha']

            # Agregar nodos
            self.graph.add_node(titulo, type="Libro")
            self.graph.add_node(autor, type="Autor")
            self.graph.add_node(genero, type="Género")
            self.graph.add_node(fecha, type="Año")

            # Agregar aristas (relaciones)
            self.graph.add_edge(titulo, autor)  # Relación libro-autor
            self.graph.add_edge(titulo, genero)  # Relación libro-género
            self.graph.add_edge(titulo, fecha)  # Relación libro-año

            # Relación entre géneros para libros con el mismo género
            for other_libro in libros:
                if other_libro != libro and other_libro['genero'] == genero:
                    self.graph.add_edge(genero, other_libro['titulo'])

    def mostrar_grafo(self, parent_window):
        """Dibuja y muestra el grafo generado."""
        self.crear_grafo()

        # Configuración de colores para nodos según tipo
        node_colors = []
        for node, attr in self.graph.nodes(data=True):
            if attr['type'] == 'Libro':
                node_colors.append('lightblue')
            elif attr['type'] == 'Autor':
                node_colors.append('orange')
            elif attr['type'] == 'Género':
                node_colors.append('lightgreen')
            elif attr['type'] == 'Año':
                node_colors.append('pink')

        # Crear la ventana de Matplotlib para mostrar el grafo
        plt.figure(figsize=(10, 7))
        pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos, node_color=node_colors, node_size=800)
        nx.draw_networkx_edges(self.graph, pos, edge_color="gray", width=1.5)
        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_color="black", font_weight="bold")

        plt.title("Relaciones en la Biblioteca", fontsize=15)
        plt.axis("off")
        plt.show()
        
class GraphInterface:
    def __init__(self, root, libro_manager):
        self.root = root
        self.root.title("Relaciones en la Biblioteca")
        self.root.state("zoomed")  # Abrir en pantalla completa

        # Colores
        dark_blue = "#6c93a4"
        red = "#ef6869"
        blue = "#2f4f74"
        light_red = "#f5e2e4"
        white = "#ffffff"

        # Fuentes
        button_font = font.Font(family="Open Sans", size=16, weight="bold")

        # Crear la jerarquía de marcos
        background_frame = tk.Frame(self.root, bg=dark_blue, padx=30, pady=30)
        background_frame.pack(fill="both", expand=True)

        outer_frame = tk.Frame(background_frame, bg=red, padx=15, pady=15)
        outer_frame.pack(fill="both", expand=True)

        middle_frame = tk.Frame(outer_frame, bg=blue, padx=10, pady=10)
        middle_frame.pack(fill="both", expand=True)

        inner_frame = tk.Frame(middle_frame, bg=light_red, padx=30, pady=30)
        inner_frame.pack(fill="both", expand=True)

        # Área central (blanca) para mostrar resultados
        content_frame = tk.Frame(inner_frame, bg=white)
        content_frame.pack(fill="both", expand=True, padx=15, pady=20)

        # Crear botones en la parte inferior
        button_frame = tk.Frame(inner_frame, bg=light_red)
        button_frame.pack(fill="x", pady=20)

        # Crear los botones con mayor espacio entre ellos
        self.create_button(button_frame, "Grafo", lambda: self.mostrar_grafo(libro_manager), red, button_font, 0, 0)
        self.create_button(button_frame, "A. Binario", self.placeholder_action, blue, button_font, 0, 1)
        self.create_button(button_frame, "A. N-ario", self.placeholder_action, red, button_font, 0, 2)
        self.create_button(button_frame, "A. AVL", self.placeholder_action, blue, button_font, 0, 3)
        self.create_button(button_frame, "Regresar", self.regresar, red, button_font, 0, 4)

    def create_button(self, parent, text, command, color, font, row, column):
        """Crea un botón y lo posiciona en el grid."""
        button = tk.Button(
            parent, text=text, command=command, bg=color, fg="white", font=font, width=14, height=2, relief=tk.FLAT
        )
        button.grid(row=row, column=column, padx=15, pady=10)  # Espacio entre botones

    def mostrar_grafo(self, libro_manager):
        """Muestra el grafo al presionar el botón correspondiente."""
        visualizador = Visualizar(libro_manager)
        visualizador.mostrar_grafo(self.root)

    def placeholder_action(self):
        """Acción de marcador de posición para otros botones."""
        messagebox.showinfo("Información", "Funcionalidad no implementada.")

    def regresar(self):
        """Cierra la ventana actual y regresa al menú principal."""
        self.root.destroy()
        import main  # Importar el archivo principal
        main.MainInterface().run()