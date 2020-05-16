# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict


class Graph:
    """This class represents a directed graph using adjacency list
    representation
    """
    def __init__(self):
        self.graph = defaultdict(list)
        """Constructor"""

    def addEdge(self, u, v):
        """function to add an edge to graph"""
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        """A function used by DFS"""
        visited[v] = True
        print(v,)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        """The function to do DFS traversal."""

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2
