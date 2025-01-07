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
station_type = [
    'square', 'circle', 'triangle', 
    'square', 'circle', 'triangle', 
    'square', 'circle', 'triangle', 
    'square', 'circle', 'triangle',
    'unique'
]

node_positions = {
    'circle': {},
    'square': {},
    'triangle': {},
    'unique': {}
}

edge_position_format = [
    [], # node position (x, y)
    {
        'circle': 0,
        'square': 0,
        'triangle': 0,
        'unique': 0
    }
]

edge_position = []

global_node_id = 1
global_circle_count = 0
global_square_count = 0
global_triangle_count = 0
global_unique_count = 0

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

# untuk masukin station ke node_position
def add_station(station):
    global global_node_id
    # Tambahkan ke node_positions
    shape = random.choice(station_type)
    node_positions[shape][global_node_id] = station
    
    # Tambahkan ke graf
    graph.add_node(global_node_id, pos=station, shape=shape)

    match (shape):
        case 'circle':
            global global_circle_count
            global_circle_count += 1
        case 'square':
            global global_square_count
            global_square_count += 1
        case 'triangle':
            global global_triangle_count
            global_triangle_count += 1
        case 'unique':
            global global_unique_count
            global_unique_count += 1

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
    for edge in graph.edges:
        pos1 = graph.nodes[edge[0]]['pos']
        pos2 = graph.nodes[edge[1]]['pos']
        pygame.draw.line(screen, WHITE, pos1, pos2, 2)

def calculate_algorithm():
    lengths = {}
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            if node1 != node2:
                pos1 = graph.nodes[node1]['pos']
                pos2 = graph.nodes[node2]['pos']
                length = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
                lengths[(node1, node2)] = length

    circuits = []
    used_nodes = set()
    while True:
        circuit = []
        for shape in ['circle', 'square', 'triangle', 'unique']:
            nodes = [node for node in node_positions[shape].keys() if node not in used_nodes]
            if nodes:
                node = nodes[0]
                circuit.append(node)
                used_nodes.add(node)
        if len(circuit) >= 3:
            circuits.append(circuit)
        else:
            break

    # Ensure at least one of each shape in the circuit
    for shape in ['circle', 'square', 'triangle']:
        nodes = [node for node in node_positions[shape].keys() if node not in used_nodes]
        if nodes:
            node = nodes[0]
            circuit.append(node)
            used_nodes.add(node)
    if len(circuit) >= 3:
        circuits.append(circuit)

    all_nodes = list(graph.nodes)
    for i in range(len(all_nodes)):
        node1 = all_nodes[i]
        node2 = all_nodes[(i + 1) % len(all_nodes)]
        pos1 = graph.nodes[node1]['pos']
        pos2 = graph.nodes[node2]['pos']
        if node1 not in used_nodes or node2 not in used_nodes or graph.nodes[node1]['shape'] == 'unique' or graph.nodes[node2]['shape'] == 'unique':
            pygame.draw.line(screen, WHITE, pos1, pos2, 2)
            graph.add_edge(node1, node2)

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    color_index = 0

    for circuit in circuits:
        color = colors[color_index % len(colors)]
        color_index += 1
        for i in range(len(circuit)):
            node1 = circuit[i]
            node2 = circuit[(i + 1) % len(circuit)]
            pos1 = graph.nodes[node1]['pos']
            pos2 = graph.nodes[node2]['pos']
            pygame.draw.line(screen, color, pos1, pos2, 2)
            graph.add_edge(node1, node2)

    # Ensure all shapes are connected
    for shape1 in ['circle', 'square', 'triangle', 'unique']:
        for shape2 in ['circle', 'square', 'triangle', 'unique']:
            if shape1 != shape2:
                nodes1 = list(node_positions[shape1].keys())
                nodes2 = list(node_positions[shape2].keys())
                if nodes1 and nodes2:
                    min_length = float('inf')
                    closest_pair = (None, None)
                    for n1 in nodes1:
                        for n2 in nodes2:
                            length = lengths[(n1, n2)]
                            if length < min_length:
                                min_length = length
                                closest_pair = (n1, n2)
                    node1, node2 = closest_pair
                    pos1 = graph.nodes[node1]['pos']
                    pos2 = graph.nodes[node2]['pos']
                    pygame.draw.line(screen, WHITE, pos1, pos2, 2)
                    graph.add_edge(node1, node2)

    # Adjust circuits to be more dynamic
    for circuit in circuits:
        for i in range(len(circuit)):
            node1 = circuit[i]
            closest_node = None
            min_length = float('inf')
            for node2 in all_nodes:
                if node1 != node2 and node2 not in circuit:
                    length = lengths[(node1, node2)]
                    if length < min_length:
                        min_length = length
                        closest_node = node2
            if closest_node:
                pos1 = graph.nodes[node1]['pos']
                pos2 = graph.nodes[closest_node]['pos']
                pygame.draw.line(screen, WHITE, pos1, pos2, 2)
                graph.add_edge(node1, closest_node)

    for circuit in circuits:
        print("Circuit:", circuit)

    return

def is_point_on_line(point, line_start, line_end, tolerance=5):
    """Check if a point is on a line segment within a given tolerance."""
    x0, y0 = point
    x1, y1 = line_start
    x2, y2 = line_end
    distance = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return distance <= tolerance

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                print("Klik kiri")
                add_station(event.pos)
                draw_graph()
                calculate_algorithm()
                print(node_positions)
            elif event.button == 3:
                print("Klik kanan")
                pos = event.pos
                edges_to_remove = []
                for edge in graph.edges:
                    pos1 = graph.nodes[edge[0]]['pos']
                    pos2 = graph.nodes[edge[1]]['pos']
                    if is_point_on_line(pos, pos1, pos2):
                        edges_to_remove.append(edge)
                for edge in edges_to_remove:
                    graph.remove_edge(*edge)
                draw_graph()
    pygame.display.flip()