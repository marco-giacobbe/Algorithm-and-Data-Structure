class graph:

    def __init__(self, graph=dict()):
        
        """
        a graph object have one only attribute graph (dict) in the format:
        {vertex1: [adj list of vertex1], ..., vertex2: [adj list of vertex2]}
        """
        
        self.graph = graph

    def __repr__(self):
        
        """
        a graph is represented in the format:
        vertex1 -> adjnode1 adjnode2; vertex2 -> adjnode1 adjnode2
        
        """
        g_repr = ''
        for key, value in self.graph.items():
            g_repr = g_repr + '{} ->'.format(key)
            for el in value:
                g_repr = g_repr + ' {}'.format(el)
            g_repr = g_repr + ';    '
        return g_repr

    def read_graph(self, filename):
        
        """
        Read graph from text file in the format:
        a b c
        b a d
        c a
        d b
        where first element of the line is the vertex and the other element are the adjacent vertex 
        """
        
        try:
            f = open(filename, 'r')

        except:
            raise NameError('{} non è stato trovato. Directory errata o File mancante'.format(filename))

        while True:
            l = f.readline()
            if l == '':
                f.close()
                return
            l = l.rstrip('\n').split(' ')
            v = l.pop(0)
            self.graph[v] = set(l)

    def new_vertex(self, vertex):
        
        """
        Add a new vertex in the current self.graph Graph
        Time complexity: O(1)
        """
        
        self.graph[vertex] = []

    def new_edge(self, v1, v2):
        
        """
        Add a new edge in the current self.graph Graph between vertices v1 and v2
        Time complexity: O(1)
        """

        if v1 not in self.graph:
            raise ValueError("Non esiste il nodo {}".format(v1))
        if v2 not in self.graph:
            raise ValueError("Non esiste il nodo {}".format(v2))
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def remove_vertex(self, vertex):

        """
        Remove a vertex in the current self.graph Graph
        Time complexity: O(n) where n is the number of vertices
        """

        if vertex not in self.graph:
            raise ValueError("Non esiste il nodo {}".format(vertex))
        
        for v in self.graph:
            #pass al vertex to search vertex in adjacents list
            if vertex in self.graph[v]: 
                self.graph[v].remove(vertex)

        return self.graph.pop(vertex)

    def remove_edge(self, v1, v2):

        """
        Remove a edge in the current self.graph Graph
        Time complexity: O(1)
        """

        if v1 not in self.graph:
            raise ValueError("Non esiste il nodo {}".format(v1))
        if v2 not in self.graph:
            raise ValueError("Non esiste il nodo {}".format(v2))
        self.graph[v1].remove(v2)
        self.graph[v2].remove(v1)


    def vertex_count(self):
        
        """
        Return number of all vertices
        Time complexity: O(1)
        """

        return len(self.graph)


    def edge_count(self):

        """
        Return number of all edges
        Time complexity: O(n) where n is the number of vertices
        """

        edges = 0
        for v, e in self.graph.items():
            edges += len(e)
        return edges//2 

    def vertices(self):

        """
        Returns a list of vertices
        Time complexity: O(n) where n is the number of vertices
        O(n) because conversion between dict_keys to list
        otherwise would have been O(1)
        """
        
        return list(self.graph.keys())

    def edges(self):

        """
        Returns a list of edges
        Time complexity: O(m) where m is the number of edges
        """

        edges = []
        for vertex, edge in self.graph.items():
            for node in edge:
                if (vertex, node) not in edges and (node, vertex) not in edges:
                    edges.append((vertex,node))
        return edges

    def incident_edges(self, vertex):
        
        """
        Returns a set of incident edges to a vertex
        Time complexity: O(1)
        """
        
        return self.graph[vertex]
    
    
    
    def edge_existence(self, target_edge):

        """
        Return True if target_edge exist in the graph, False otherwise
        Time complexity: O(m) where m is the number of edges (search miss)
        """
        for vertex, edge in self.graph.items():
            for node in edge:
                if (vertex, node) == target_edge or (node, vertex) == target_edge:
                    return True
        return False

    def dfs(self, recursion=False):

        """
        Graph's Deep First Search 

        Time complexity: O(n+m) where n and m are the number of vertices and edges
        """

        if recursion:
            return self.recursive_dfs()
        return self.iterative_dfs()

    def recursive_dfs(self):
        
        """
        Return a list of visited node
        It called dfs_visit to visit all nodes
        
        Legend:
            0: white
            1: grey
            2: black
        """

        exploration = dict()
        visited = []
        for key in self.graph:
            exploration[key] = 0
        for node in exploration:
            if exploration[node] == 0:
                self.dfs_visit(node, exploration, visited) 
        return visited
            
    def dfs_visit(self, vertex, exploration, visited):

        """
        Called by recursive_dfs()
        """

        exploration[vertex] = 1
        visited.append(vertex)
        for node in self.graph[vertex]:
            if exploration[node] == 0:
                self.dfs_visit(node, exploration, visited)
            exploration[node] = 2

    def iterative_dfs(self):

        """
        an iterative Deep First Search version
        """
        
        visited, stack = [], []
        stack.append(list(self.graph.keys())[0])
        while stack:
            print(stack)
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for adj_node in self.graph[node]:
                    if adj_node not in visited:
                        stack.append(adj_node)
        return visited
    
    def bfs(self):

        """

        """
        
        visited, queue, exploration = [], [], {}

        for node in self.graph:
            self.exploration[node] = 0 
        start = list(self.graph.keys())[0]
        queue.append(start)
        explored[start] = 1

        while queue:
            node = queue.pop(0)
            for adj_node in self.queue[node]:
                if not exploration[adj_node]:
                    exploration[adj_node] = 1
                for adj_node in self.graph[node]:
                    queue.append(adj_node)
        return visited

a = graph()
a.read_graph('graph.txt')
print(a)
print(a.dfs())
