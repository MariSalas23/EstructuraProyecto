import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Toplevel
from libro import Libro

class Visualizar:
    def __init__(self, libro_manager):
        self.libro_manager = libro_manager

    def crear_grafo(self):
        # Crear el grafo
        self.graph = nx.Graph()

        libros = self.libro_manager.listar_libros()

        for libro in libros:
            isbn = libro['isbn']
            titulo = libro['titulo']
            autor = libro['autor']
            fecha = libro['fecha']
            genero = libro['genero']

            # Nodos
            self.graph.add_node(titulo, type="Libro")
            self.graph.add_node(autor, type="Autor")
            self.graph.add_node(genero, type="Género")
            self.graph.add_node(fecha, type="Año")

            # Relaciones
            self.graph.add_edge(titulo, autor)  # Relación libro-autor
            self.graph.add_edge(titulo, genero)  # Relación libro-género
            self.graph.add_edge(titulo, fecha)  # Relación libro-año

            # Géneros
            for other_libro in libros:
                if other_libro != libro and other_libro['genero'] == genero:
                    self.graph.add_edge(genero, other_libro['titulo'])

    def mostrar_grafo(self, parent_window):
        grafico_window = Toplevel(parent_window)
        grafico_window.title("Relaciones en la Biblioteca")
        grafico_window.geometry("800x600")

        self.crear_grafo()

        node_colors = []
        for node in self.graph.nodes(data=True):
            if node[1]['type'] == 'Libro':
                node_colors.append('lightblue')
            elif node[1]['type'] == 'Autor':
                node_colors.append('orange')
            elif node[1]['type'] == 'Género':
                node_colors.append('lightgreen')
            elif node[1]['type'] == 'Año':
                node_colors.append('pink')

        # Dibujar el grafo
        plt.figure(figsize=(10, 7))
        pos = nx.spring_layout(self.graph)  # Posiciones de los nodos

        # Dibujar nodos, aristas y etiquetas
        nx.draw_networkx_nodes(self.graph, pos, node_color=node_colors, node_size=800)
        nx.draw_networkx_edges(self.graph, pos, edge_color="gray", width=1.5)
        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_color="black", font_weight="bold")

        plt.title("Relaciones en la Biblioteca", fontsize=15)
        plt.axis("off")
        plt.show()