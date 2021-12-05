from collections import deque

# def dfs_recursive(graph, v, colors, black_order):
#     # color current element
#     colors[v] = "gray"
#     # for each white neighbour run dfs
#     for adjacent in graph[v]:
#         if (colors[adjacent] == "white"):
#             dfs_recursive(graph, adjacent, colors, black_order)
            
#     colors[v] = "black"
#     black_order.append(v)
    
    
# def dfs_shell(graph):
#     # init colors and black_order
#     colors = ["white" for i in range(len(graph))]
#     black_order = []
#     # run dfs_recursive
#     dfs_recursive(graph, next(iter(graph)), colors, black_order)
#     return black_order
    
    
# def convert_to_edge_graph(graph):
#     # node2edges => edge2nodes
#     edges_list = []
#     for vertex in graph:
#         for adjacent in graph[vertex]:
#             edges_list.append((vertex, adjacent))
#     # create edge graph
#     edge_graph = {}
#     for edge in range(len(edges_list)):
#         edge_graph[edge] = []
#         for potential_adjacent in range(len(edges_list)):
#             if edges_list[edge][1] == edges_list[potential_adjacent][0]:
#                 edge_graph[edge].append(potential_adjacent)
                
#     return edges_list, edge_graph


# def compute_Euler_circuit_digraph(graph):
#     # create edge_graph
#     edges_list, edge_graph = convert_to_edge_graph(graph)
#     cycles = []
#     # iterate over black order get all eiler's cycles
#     for edge_index in dfs_shell(edge_graph):
#         cycles.insert(0, edges_list[edge_index])
#     return cycles

def dfs_iterative(graph, v):
    path = []
    stack = deque()
    stack.append(v)

    while stack:
        s = stack.pop()
        if s not in path:
            path.append(s)
        elif s in path:
            #leaf node
            continue
        for neighbour in graph[s]:
            stack.append(neighbour)
    
    return path[::-1]

    
def dfs_shell(graph):
    # init colors and black_order
    colors = [i for i in graph]
    black_order = []
    # run dfs_recursive
    while len(colors) != 0:
        black_order_temp = dfs_iterative(graph, colors[0])
        black_order.extend(black_order_temp)
        colors = [i for i in colors if i not in black_order_temp]
    return black_order
    
    
def node_grap2edge_graph(graph):
    # node2edges => edge2nodes
    edges_list = []
    for vertex in graph:
        for adjacent in graph[vertex]:
            edges_list.append((vertex, adjacent))
    # create edge graph
    edge_graph = {}
    for edge in range(len(edges_list)):
        edge_graph[edge] = []
        for potential_adjacent in range(len(edges_list)):
            if edges_list[edge][1] == edges_list[potential_adjacent][0]:
                edge_graph[edge].append(potential_adjacent)
                
    return edges_list, edge_graph


def compute_Euler_circuit_digraph(graph): 
    # create edge_graph
    edges_list, edge_graph = node_grap2edge_graph(graph)
    cycles = []
    # iterate over black order get all eiler's cycles
    for edge_index in dfs_shell(edge_graph):
        cycles.insert(0, edges_list[edge_index])
    return cycles 
