""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""

 
class AdjNode:
    """A class to represent the adjacency list of the node"""
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
   
class Graph:
    """A class to represent a graph. A graph is the list of the adjacency
    lists. Size of the array will be the no. of the vertices "V"
    """

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    def add_edge(self, src, dest): 
        """Function to add an edge in an undirected graph""" 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
   
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    def print_graph(self): 
        """Function to print the graph""" 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
  
   
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph()
