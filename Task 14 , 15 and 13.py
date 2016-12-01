import sys


# TestGraph
# Node > 0   1   2   3   4   5   6   7   8   9  10  11
#   v
#   0    0,  0,  0,  0,  0,  0, 10,  0, 12,  0,  0,  0
#   1    0,  0,  0,  0, 20,  0,  0, 26,  0,  5,  0,  6
#   2    0,  0,  0,  0,  0,  0,  0, 15, 14,  0,  0,  9
#   3    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7,  0
#   4    0, 20,  0,  0,  0,  5, 17,  0,  0,  0,  0, 11
#   5    0,  0,  0,  0,  5,  0,  6,  0,  3,  0,  0, 33
#   6    0,  0,  0,  0, 17,  6,  0,  0,  0,  0,  0,  0
#   7    0, 26, 15,  0,  0,  0,  0,  0,  0,  3,  0, 20
#   8    2,  0, 14,  0,  0,  3,  0,  0,  0,  0,  0,  0
#   9    0,  5,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0
#   10   0,  0,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0
#   11   0,  6,  9,  0, 11, 33,  0, 20,  0,  0,  0,  0


class SimpleGraph(object):

    def __init__(self, number_of_nodes=10):
        self._adjacency_list = [[]]
        self._number_of_nodes = number_of_nodes
        self._edge_weights  = [[0 for x in range(number_of_nodes)] for y in range(number_of_nodes)]

    def size(self):
        return self._number_of_nodes

    def add_node(self, node):
        self._adjacency_list.insert(node, [])

    def add_edge(self, node1, node2, weight=1):
        self._adjacency_list[node1].append(node2)
        self._adjacency_list[node2].append(node1)
        self._edge_weights[node1][node2] = weight
        self._edge_weights[node2][node1] = weight

    def get_neighbours(self, node):
        return self._adjacency_list[node]

    def get_weight(self, node1, node2):
        return self._edge_weights[node1][node2]

    def bfs_traversal(self, start_node):
        queue = []
        visited = []
        queue.append(start_node)
        visited.append(start_node)
        while len(queue) > 0:
            curr_node = queue.pop(0)
            for neighbourNode in self.get_neighbours(curr_node):
                if not visited.__contains__(neighbourNode):
                    queue.append(neighbourNode)
                    visited.append(neighbourNode)
        return visited

    def dfs_traversal(self, start_node):
        stack = []
        visited = []
        stack.append(start_node)
        visited.append(start_node)
        while len(stack) > 0:
            curr_node = stack.pop()
            for neighbourNode in self.get_neighbours(curr_node):
                if not visited.__contains__(neighbourNode):
                    stack.append(neighbourNode)
                    visited.append(neighbourNode)
        return visited

    def dijkstra(self, start_node, destination_node):
        distance = []
        visited = []
        prev = []
        UNKNOWN = sys.maxsize >> 1
        for i in range(0, self._number_of_nodes, 1):
            distance.append(UNKNOWN)
            visited.append(False)
            prev.append(-1)

        distance[start_node] = 0
        while True:
            # find the nearest unvisited node from the source (in place of priority queue -> deque)
            min_distance = UNKNOWN
            min_node = 0
            for node in range(0, self._number_of_nodes, 1):
                if visited[node] == 0 and distance[node] < min_distance:
                    min_distance = distance[node]
                    min_node = node

            if min_distance == UNKNOWN:
                # no min_distance node found -> algorithm finished
                break

            visited[min_node] = True
            for i in range(0, self._number_of_nodes, 1):
                # improve the distance[0..n-1] through min_node
                curr_weight = self.get_weight(min_node, i)
                if curr_weight > 0:
                    # no 'i' is connected to min_node
                    new_distance = distance[min_node] + self.get_weight(min_node, i)
                    if new_distance < distance[i]:
                        distance[i] = new_distance
                        prev[i] = min_node

        if distance[destination_node] == UNKNOWN:
            # no path found from source to destination
            return None

        # reconstruct path from source to destination
        path = []
        curr_node = destination_node
        while curr_node != -1:
            path.insert(0, curr_node)
            curr_node = prev[curr_node]

        return path



def fill_graph():
    for i in range(0, graph.size()):
        graph.add_node(i)
    graph.add_edge(0, 6, 10)
    graph.add_edge(0, 8, 12)
    graph.add_edge(1, 4, 20)
    graph.add_edge(1, 7, 26)
    graph.add_edge(1, 9, 5)
    graph.add_edge(1, 11, 6)
    graph.add_edge(2, 7, 15)
    graph.add_edge(2, 8, 14)
    graph.add_edge(2, 11, 9)
    graph.add_edge(3, 10, 7)
    graph.add_edge(4, 5, 5)
    graph.add_edge(4, 6, 17)
    graph.add_edge(4, 11, 11)
    graph.add_edge(5, 6, 6)
    graph.add_edge(5, 8, 3)
    graph.add_edge(5, 11, 33)
    graph.add_edge(7, 9, 3)
    graph.add_edge(7, 11, 20)


def print_path(graph, source_node, destination_node):
    output = "Shortest path [{:d} -> {:d}]: ".format(source_node, destination_node)
    path = graph.dijkstra(source_node, destination_node)
    if path is None:
        output += "no path"
    else:
        path_length = 0
        for i in range(0, len(path) - 1, 1):
            path_length += graph.get_weight(path[i], path[i + 1])
        for p in range(0, len(path), 1):
            output += "{:d}".format(path[p])
            if p != len(path) - 1:
                output += "->"
        output += " (length = {:d})".format(path_length)
    print(output)


graph = SimpleGraph(12)
fill_graph()
print("BFS:")
for node in graph.bfs_traversal(0):
    print(node)
print("DFS:")
for node in graph.dfs_traversal(0):
    print(node)
print("Dijkstra:")
print_path(graph, 0, 9)
print_path(graph, 0, 2)
print_path(graph, 0, 10)
print_path(graph, 0, 11)
print_path(graph, 0, 1)


