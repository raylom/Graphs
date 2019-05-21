"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue
        q = Queue()
        # create empty visited set
        visited = set()
        # add starting vertex to queue
        q.enqueue(starting_vertex)
        # while the queue is not empty
        while q.size() > 0:
            # dequque the first vertex
            v = q.dequeue()
            # if it has not been visited
            if v not in visited:
                # mark as visited
                visited.add(v)
                # then enqueue each if its neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack
        s = Stack()
        # create an empty visited set
        visited = set()
        # push the starting vertex to the stack
        s.push(starting_vertex)
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if it has not been visited...
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            print(starting_vertex)
            visited.add(starting_vertex)
            # call DFT_recursive on each unvisited neighbors
            for neighbor in self.vertices[starting_vertex]:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue
        q = Queue()
        visited = set()
        # add a path of the starting vertex to que
        q.enqueue([starting_vertex])
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # get the last vertex of the path
            v = path[-1]
            # check if its our destination
            if v == destination_vertex:
                return path
            if v not in visited:
                visited.add(v)
        # enqueue path to each of its neighbors in the queue
        for neighbor in self.vertices[v]:
            new_path = path.copy()
            new_path.append(neighbor)
            q.enqueue(new_path)
            if neighbor == destination_vertex:
                return new_path
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                print(v)
                visited.add(v)
                if v == destination_vertex:
                    return path
                for neighbor in self.vertices[v]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    s.push(new_path)
            return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
