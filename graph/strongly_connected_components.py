# Kosaraju algorithm

class Graph:
    def __init__(self, V):
        self.V = V
        self.nodes = [ [] for _ in range(V)]

    def addEdge(self, u, v):
        self.nodes[u].append(Edge(u,v))

    def adj(self, u):
        return self.nodes[u]


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

def dfs(graph):
    visited = [False] * graph.V
    stack = []

    for node in range(graph.V):
        if not visited[node]:
            dfsUtil(graph, node, visited, stack)

    return stack

def dfsUtil(graph, node, visited, stack):
    visited[node] = True

    for edge in graph.adj(node):
        if not visited[edge.v]:
            dfsUtil(graph, edge.v, visited, stack)

    stack.append(node)

# Transpose a graph
def transpose(graph):
    newGraph = Graph(graph.V)

    for node in range(graph.V):
        for edge in graph.adj(node):
            newGraph.addEdge(edge.v, edge.u)
    
    return newGraph

def dfsStack(graph, stack):
    visited = [False] * graph.V

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfsStackUtil(graph, node, visited)
            print()

def dfsStackUtil(graph, node, visited):
    visited[node] = True
    print(node, end = ' ')

    for edge in graph.adj(node):
        if not visited[edge.v]:
            dfsStackUtil(graph, edge.v, visited)


def findStronglyConnectedComponents(graph):
    # Find the recursive stack of all nodes
    stack = dfs(graph)

    # Transpose of graph
    transposeGraph = transpose(graph)

    # Get strongly connected components
    dfsStack(transposeGraph, stack)


def driver():
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    
    findStronglyConnectedComponents(g)

driver()