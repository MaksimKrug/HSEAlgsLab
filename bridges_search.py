import numpy as np
import sys

sys.setrecursionlimit(100000)


class ComputeBridgesDeterm:
    def __init__(self, adj_list):
        # init statistics
        self.timer = 0
        self.adj_list = adj_list
        self.history, self.bridges = [], []
        # determ bridges
        self.colors = ["white" for i in self.adj_list]
        self.ret = [np.inf for i in self.adj_list]
        self.entry = [0 for i in self.adj_list]
        # if node's color == white run dfs
        for i in self.adj_list:
            if self.colors[i] == "white":
                self.bridges_determ_dfs(i)

    def bridges_determ_dfs(self, vertex):
        # update color and timers
        self.colors[vertex] = "gray"
        self.history.append(vertex)
        self.timer += 1
        self.entry[vertex] = self.timer
        # for all neighbors: if adj_color == white: run dfs;
        for adjacent in self.adj_list[vertex]:
            if self.colors[adjacent] == "white":
                self.bridges_determ_dfs(adjacent)
                # ret = min(vertex, adjacent)
                self.ret[vertex] = min(self.ret[vertex], self.ret[adjacent])
                if self.ret[adjacent] > self.entry[vertex]:
                    if vertex < adjacent:
                        self.bridges.append((vertex, adjacent))
                    else:
                        self.bridges.append((adjacent, vertex))
            elif len(self.history) < 2 or self.history[-2] != adjacent:
                self.ret[vertex] = min(self.ret[vertex], self.entry[adjacent])
        self.colors[vertex] = "black"
        self.history.pop()


def compute_bridges_determ(adj_list):
    determ = ComputeBridgesDeterm(adj_list)
    return determ.bridges


class RandomBridges:
    def __init__(self):
        self.adj_list, self.samples = [], {}
        self.bridges, self.edges, self.colors, self.history, = [], [], [], []
        self.EDGE_NUM = 0
        self.SAMPLE_NUM = 1

    def sampling_dfs(self, vertex):
        self.colors[vertex] = "gray"
        self.history.append(vertex)
        for adjacent in self.adj_list[vertex]:
            if self.colors[adjacent] == "white":
                self.sampling_dfs(adjacent)
            elif len(self.history) < 2 or self.history[-2] != adjacent:
                rand = np.uint64(
                    np.random.randint(0, np.iinfo(np.uint64).max, dtype=np.uint64)
                )
                self.samples[vertex][adjacent] = rand
                self.samples[adjacent][vertex] = rand
        self.colors[vertex] = "black"
        self.history.pop()

        if len(self.history) > 0:
            parent = self.history[-1]
            parent_edge_weight = np.uint64(0)
            for adjacent in self.adj_list[vertex]:
                if adjacent != parent:
                    parent_edge_weight ^= self.samples[vertex][adjacent]
            self.samples[vertex][parent] = parent_edge_weight
            self.samples[parent][vertex] = parent_edge_weight

    def launch_sampling(self):
        self.colors = ["white" for i in self.adj_list]
        for vertex in self.adj_list:
            if self.colors[vertex] == "white":
                self.sampling_dfs(vertex)

    def find_bridges(self, adj_list):
        self.adj_list = adj_list
        for i in range(len(adj_list)):
            self.samples[i] = {}
        self.launch_sampling()
        for first_key in self.adj_list:
            for second_key in self.adj_list[first_key]:
                if (second_key, first_key) not in self.bridges and self.samples[
                    first_key
                ][second_key] == 0:
                    self.bridges.append((first_key, second_key))
        return self.bridges

    def find_2bridges(self, adj_list, sort_fun):
        self.adj_list = adj_list
        self.track = self.track
        for i in range(len(adj_list)):
            self.samples[i] = {}
        # print(self.samples)
        self.launch_sampling()
        for first_key in self.adj_list:
            for second_key in self.adj_list[first_key]:
                self.edges.append(
                    ((first_key, second_key), self.samples[first_key][second_key])
                )
        self.edges = list(set(self.edges))
        samples_list = [edge[self.SAMPLE_NUM] for edge in self.edges]
        sorted_args = sort_fun(samples_list)
        cluster_size = 0
        current_cluster = 0
        for i in range(len(sorted_args) - 1):
            cluster_size += 1
            if (
                self.edges[sorted_args[i]][self.SAMPLE_NUM]
                != self.edges[sorted_args[i + 1]][self.SAMPLE_NUM]
            ):
                if cluster_size > 1:
                    self.bridges.append([])
                    j = i - cluster_size + 1
                    while j < i:
                        self.bridges[current_cluster].append(
                            (self.edges[sorted_args[j]][self.EDGE_NUM])
                        )
                        j += 1
                    cluster_size = 0
                    current_cluster += 1
        return self.bridges


def compute_bridges_rand(adj_list):
    rand = RandomBridges()
    return rand.find_bridges(adj_list)


def compute_2bridges_rand(adj_list, sort_fun):
    rand = RandomBridges()
    return rand.find_2bridges(adj_list, sort_fun)
