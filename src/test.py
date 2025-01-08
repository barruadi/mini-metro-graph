import pygame
import networkx as nx
import random
import math

# Inisialisasi Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Struktur data posisi node
node_positions = {
    'circle': {},
    'square': {},
    'triangle': {},
    'unique': {}
}

# Struktur data untuk menyimpan edges
edges = []

# Graf menggunakan NetworkX
graph = nx.Graph()

# ID unik untuk setiap node
global_node_id = 1

# Fungsi menggambar node
def draw_nodes():
    screen.fill((0, 0, 0))  # Bersihkan layar setiap kali menggambar ulang
    for shape, nodes in node_positions.items():
        for _, pos in nodes.items():
            if shape == 'circle':
                pygame.draw.circle(screen, BLUE, pos, 20)
            elif shape == 'square':
                pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] - 20, pos[1] - 20, 40, 40))
            elif shape == 'triangle':
                pygame.draw.polygon(screen, RED, [
                    (pos[0], pos[1] - 20),
                    (pos[0] - 20, pos[1] + 20),
                    (pos[0] + 20, pos[1] + 20)
                ])
            elif shape == 'unique':
                pygame.draw.polygon(screen, (255, 255, 0), [
                    (pos[0] + 20 * math.cos(math.radians(angle)), pos[1] + 20 * math.sin(math.radians(angle)))
                    for angle in range(0, 360, 72)
                ])

# Fungsi menggambar sisi (edges)
def draw_edges():
    for edge in edges:
        node1, node2 = edge
        x1, y1 = graph.nodes[node1]['pos']
        x2, y2 = graph.nodes[node2]['pos']
        pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

# Fungsi menggambar sisi (edges) dengan algoritma Dijkstra
def draw_edges_dijkstra(start_node):
    # Hitung jalur terpendek dari start_node ke semua node lainnya
    lengths, paths = nx.single_source_dijkstra(graph, start_node)
    
    for target_node, path in paths.items():
        if start_node != target_node:
            for i in range(len(path) - 1):
                node1 = path[i]
                node2 = path[i + 1]
                x1, y1 = graph.nodes[node1]['pos']
                x2, y2 = graph.nodes[node2]['pos']
                pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

# Fungsi menambahkan node baru ke node_positions
def add_node_to_positions(pos):
    global global_node_id
    shapes = ['circle', 'square', 'triangle', 'circle', 'square', 'triangle', 'unique']
    shape = random.choice(shapes)  # Pilih bentuk secara acak
    
    # Tambahkan ke node_positions
    node_positions[shape][global_node_id] = pos
    
    # Tambahkan ke graf
    graph.add_node(global_node_id, pos=pos, shape=shape)
    
    # Hubungkan ke semua node lainnya
    for existing_node in graph.nodes:
        if existing_node != global_node_id:
            x1, y1 = graph.nodes[existing_node]['pos']
            x2, y2 = pos
            weight = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            graph.add_edge(existing_node, global_node_id, weight=weight)
            edges.append((existing_node, global_node_id))  # Tambahkan edge ke daftar edges
            draw_edges_dijkstra(existing_node)  # Gambar ulang edges dengan algoritma Dijkstra
            pass
    
    global_node_id += 1

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Klik kiri untuk menambahkan simpul
                add_node_to_positions(event.pos)
                print(node_positions)
                print(edges)
    
    # Gambar graf
    screen.fill((0, 0, 0))  # Bersihkan layar
    # draw_edges_dijkstra(node_positions)
    draw_nodes()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
