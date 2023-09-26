class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].append(vertex1)

    def get_adjacent_vertices(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return []

    def __str__(self):
        return str(self.adjacency_list)

# Create a graph and add vertices and edges
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")

# Print the adjacency list
print("Adjacency List:")
print(graph)

# Get adjacent vertices of a vertex
print("Adjacent vertices of B:", graph.get_adjacent_vertices("B"))
