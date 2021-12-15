from queue import PriorityQueue

from numpy.core.numeric import Infinity

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def shortestReach(n, edges, s):
    g = Graph(n)
    for a in range(len(edges)):
        g.add_edge(edges[a][0], edges[a][1], edges[a][2])  
    D = dijkstra(g, s)  
    mylist = []
    for vertex in range(len(D)):
        if vertex != s:
            mylist.append(D[vertex])
    mylist = [-1 if i == Infinity else i for i in mylist] 
    return mylist
print(shortestReach(5, [[0,1,5], [1,2,6], [2,3,2], [0,2,15]], 0))