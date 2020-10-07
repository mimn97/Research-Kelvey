# Advanced version of Research.py
# Written by Minhwa "Mina" Lee
# Here, we define some classes to setup for a cube; that is, 'Vertex', and 'Graph.'
# Utilized a property of OO programming in Python

# neighbor = All Vertices adjacent to a certain vertex
# neighbors = a set of vertices adjacent to a certain Vertex
# self = 'self'

# class Vertex:
#     def __init__(self, vertex):
#         self.name = vertex
#         self.neighbors = []
#
#     def add_neighbor(self, neighbor):
#         if isinstance(neighbor, Vertex):
#             if neighbor.name not in self.neighbors:
#                 self.neighbors.append(neighbor.name)
#                 neighbor.neighbors.append(self.name)
#                 self.neighbors = sorted(self.neighbors)
#                 neighbor.neighbors = sorted(neighbor.neighbors)
#         else:
#             return False
#
#     def add_neighbors(self, neighbors):
#         for neighbor in neighbors:
#             if isinstance(neighbor, Vertex):
#                 if neighbor.name not in self.neighbors:
#                     self.neighbors.append(neighbor.name)
#                     neighbor.neighbors.append(self.name)
#                     self.neighbors = sorted(self.neighbors)
#                     neighbor.neighbors = sorted(neighbor.neighbors)
#             else:
#                 return False
#
#     def __repr__(self):
#         return str(self.neighbors)
#
# class Graph:
#     def __init__(self):
#         self.vertices = {}
#
#     def add_vertex(self, vertex):
#         if isinstance(vertex, Vertex):
#             self.vertices[vertex.name] = vertex.neighbors
#
#
#     def add_vertices(self, vertices):
#         for vertex in vertices:
#             if isinstance(vertex, Vertex):
#                 self.vertices[vertex.name] = vertex.neighbors
#
#     def add_edge(self, vertex_from, vertex_to):
#         if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
#             vertex_from.add_neighbor(vertex_to)
#             if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
#                 self.vertices[vertex_from.name] = vertex_from.neighbors
#                 self.vertices[vertex_to.name] = vertex_to.neighbors
#
#     def add_edges(self, edges):
#         for edge in edges:
#             self.add_edge(edge[0],edge[1])
#
#     def adjacencyList(self):
#         if len(self.vertices) >= 1:
#                 return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
#         else:
#             return dict()
#
#     def adjacencyMatrix(self):
#         if len(self.vertices) >= 1:
#             self.vertex_names = sorted(g.vertices.keys())
#             self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
#             import numpy as np
#             self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
#             for i in range(len(self.vertex_names)):
#                 for j in range(i, len(self.vertices)):
#                     for el in g.vertices[self.vertex_names[i]]:
#                         j = g.vertex_indices[el]
#                         self.adjacency_matrix[i,j] = 1
#             return self.adjacency_matrix
#         else:
#             return dict()
#
# def graph(g):
#     """ Function to print a graph as adjacency list and adjacency matrix. """
#     return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())
#
# ###################################################################################
#
# a = Vertex('A')
# b = Vertex('B')
# c = Vertex('C')
# d = Vertex('D')
# e = Vertex('E')
#
# a.add_neighbors([b,c,e])
# b.add_neighbors([a,c])
# c.add_neighbors([b,d,a,e])
# d.add_neighbor(c)
# e.add_neighbors([a,c])
#
# g = Graph()
# print(graph(g))
# print()
# g.add_vertices([a,b,c,d,e])
# g.add_edge(b,d)
# print(graph(g))

# import numpy as np

class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        # Return True if neighbor is an instance(object) or subclass of the class Vertex
        if isinstance(neighbor, Vertex):
             if neighbor.name not in self.neighbors: # When a vertex was not initialized yet
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors) # returns a list of 'neighbors' in sorted manner
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

    def __repr__(self):
        return str(self.neighbors)


class Graph:
    def __init__(self):
        self.vertices = {} # Use a dictionary - key:value

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, vertex_start, vertex_end):
        if isinstance(vertex_start, Vertex) and isinstance(vertex_end, Vertex):
            vertex_start.add_neighbor(vertex_end)
            if isinstance(vertex_start, Vertex) and isinstance(vertex_end, Vertex):
                self.vertices[vertex_start.name] = vertex_start
                self.vertices[vertes_end.name] = vertex_end

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def adjacencyList(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()

    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indexes = dict(zip(self.vertex_names, range(len(self.vertex_names))))
            import numpy as np
            self.adjacency_matrix = np.zeros(shape = (len(self.vertices,len(self.vertices))))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in g.vertices[self.vertex_names[i]]:
                        j = g.vertex_indexes[el]
                        self.adjacency_matrix[i,j] = 1
            return self.adjacency_matrix
        else:
            return dict()

def graph(g):
    return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())


# Calling out functions
cube = {            # adjacent matrix -> Create a matrix based on the inputs
    "1":[0,0,0],
    "2":[1,0,0],
    "3":[1,1,0],
    "4":[0,1,0],
    "5":[0,0,1],
    "6":[1,0,1],
    "7":[1,1,1],
    "8":[0,1,1]
    }

a = Vertex('1')
b = Vertex('2')
c = Vertex('3')
d = Vertex('4')
e = Vertex('5')
f = Vertex('6')
g = Vertex('7')
h = Vertex('8')

a.add_neighbors([b,d,e])
b.add_neighbors([a,c,f])
c.add_neighbors([b,d,g])
d.add_neighbors([a,c,h])
e.add_neighbors([a,f,h])
f.add_neighbors([b,e,g])
g.add_neighbors([f,c,h])
h.add_neighbors([e,d,g])

g = Graph()
print(graph(g))
g.add_vertices([a,b,c,d,e,f,g,h])
print(graph(g))
