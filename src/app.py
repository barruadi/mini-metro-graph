import pygame
from lines import draw_lines
# from station import add_station
import networkx as nx
import random
import math
import typing

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
graph = nx.Graph()

# init
station_type = ['square', 'circle', 'triangle', 'square', 'circle', 'triangle', 'unique']

node_positions = {
    'circle': {},
    'square': {},
    'triangle': {},
    'unique': {}
}

edge_position_format = [
    [], # node position
    {
        'circle': 0,
        'square': 0,
        'triangle': 0,
        'unique': 0
    }
]

edge_position = []

global_node_id = 1



# fn
def get_position_from_id(id: int):
    for shape, nodes in node_positions.items():
        if id in nodes:
            return nodes[id]
    return None

def get_shape_from_id(id: int):
    for shape, nodes in node_positions.items():
        if id in nodes:
            return shape
    return None

def add_station(station):
    global global_node_id
    # Tambahkan ke node_positions
    shape = random.choice(station_type)
    node_positions[shape][global_node_id] = station
    
    # Tambahkan ke graf
    graph.add_node(global_node_id, pos=station, shape=shape)
    global_node_id += 1


# untuk gambar 
def draw_graph():
    screen.fill((0, 0, 0)) 
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                print("Klik kiri")
                add_station(event.pos)
                print(node_positions)
    # add_station(event.pos)
    pygame.display.flip()