import networkx as nx
graph = nx.Graph()
node_positions = {}

station_type = ['square', 'circle', 'triangle']


def add_station(terminal):
    new_id = len(graph.nodes) + 1
    graph.add_node(new_id, terminal=terminal)
    node_positions[new_id] = terminal

