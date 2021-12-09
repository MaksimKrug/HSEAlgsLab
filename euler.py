from collections import deque

# def compute_Euler_circuit_digraph_recursive(graph):
#     def convert_to_edge_graph(graph):
#         # node2edges => edge2nodes
#         edges_list = []
#         for vertex in graph:
#             for adjacent in graph[vertex]:
#                 edges_list.append((vertex, adjacent))
#         # create edge graph
#         edge_graph = {}
#         for edge in range(len(edges_list)):
#             edge_graph[edge] = []
#             for potential_adjacent in range(len(edges_list)):
#                 if edges_list[edge][1] == edges_list[potential_adjacent][0]:
#                     edge_graph[edge].append(potential_adjacent)

#         return edges_list, edge_graph

#     def dfs_shell(graph):
#         # init colors and black_order
#         colors = ["white" for i in range(len(graph))]
#         black_order = []
#         # run dfs_recursive
#         dfs_recursive(graph, next(iter(graph)), colors, black_order)
#         return black_order

#     def dfs_recursive(graph, v, colors, black_order):
#         # color current element
#         colors[v] = "gray"
#         # for each white neighbour run dfs
#         for adjacent in graph[v]:
#             if colors[adjacent] == "white":
#                 dfs_recursive(graph, adjacent, colors, black_order)

#         colors[v] = "black"
#         black_order.append(v)

#     # create edge_graph
#     edges_list, edge_graph = convert_to_edge_graph(graph)
#     cycles = []
#     # iterate over black order get all eiler's cycles
#     for edge_index in dfs_shell(edge_graph):
#         cycles.insert(0, edges_list[edge_index])
#     return cycles


def dfs_iterative(graph, node, discovered, path, black_order):
    stack = deque()
    stack.append(node)

    while stack:
        # get node
        node = stack.pop()
        # if already visited: continut
        if discovered[node]:
            continue
        # mark node
        discovered[node] = True
        # append node to path
        path.append(node)
        # if leaf
        if all([discovered[i] for i in graph[node]]):
            for i in path[::-1]:
                if i not in black_order and all([discovered[j] for j in graph[i]]):
                    black_order.append(i)
                elif not all([discovered[j] for j in graph[i]]):
                    break

        for i in graph[node][::-1]:
            if not discovered[i]:
                stack.append(i)


def dfs_shell(graph):
    # init colors and black_order
    path = []
    black_order = []
    discovered = [False for i in graph]
    # run dfs
    for node in graph:
        if not discovered[node]:
            dfs_iterative(graph, node, discovered, path, black_order)
    return black_order


def node_grap2edge_graph(graph):
    # node2edges => edge2nodes
    edges_list = []
    for vertex in graph:
        for adjacent in graph[vertex]:
            edges_list.append((vertex, adjacent))

    # create temp graph
    temp = {i: [] for i in graph.keys()}
    i = 0
    for node, values in graph.items():
        for j in values:
            temp[node].append(i)
            i += 1

    # create edge_graph
    edge_graph = {}
    i = 0
    for edge in edges_list:
        edge_graph[i] = temp[edge[1]]
        i += 1

    return edges_list, edge_graph


def compute_Euler_circuit_digraph(graph):
    # create edge_graph
    edges_list, edge_graph = node_grap2edge_graph(graph)
    cycles = []
    # iterate over black order get all eiler's cycles
    for edge_index in dfs_shell(edge_graph):
        cycles.insert(0, edges_list[edge_index])
    return cycles
