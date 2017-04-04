class Graph( object ):

    def __init__( self, verticesCount ):
        if type( verticesCount ) is not int:
            print "Please enter a valid integer value."
            return

        self.verticesCount = int( verticesCount )
        self.graph = dict()

        i = 1
        while i <= self.verticesCount:
            self.graph[i] = []
            i = i + 1

        print "Graph created with " + str( self.verticesCount ) + " vertices"

    def _validVertex( self, vertex ):
        if vertex in self.graph.keys():
            return True
        else:
            return False

    def addVertex( self, vertex ):
        if self._validVertex( vertex ):
            print "Vertex " + str( vertex ) + " already exists in graph"
            return

        if type( vertex ) is not int:
            print "In this graph vertices can only be integers. Failed to add '" + str( vertex ) + "' to the graph"
            return

        self.graph[vertex] = []
        print "Vertex " + str( vertex ) + " added to graph"
        self.verticesCount = self.verticesCount + 1

    def addConnection( self, vertex, connections ):
        #Eliminating duplicates
        connections = list( set( connections ) )

        if not self._validVertex( vertex ):
            print "Vertex " + str( vertex ) + " doesn't exist in the graph"
            return

        if type( connections ) is not list:
            print "The connections must be represented as a list. Eg: [1,2,3,4]"
            return

        for connection in connections:
            if not self._validVertex( connection ):
                print "The vertex " + str( connection ) + " doesn't exist in the graph for vertex " + str( vertex ) + " to connect to."
                return

        self.graph[vertex] = connections
        print "Connections added to vertex " + str( vertex )

    def displayVertexConnections( self, vertex ):
        if not self._validVertex( vertex ):
            print "Vertex " + str( vertex ) + " doesn't exist in the graph"
            return

        print "Vertex " + str( vertex ) + " is connected to",
        for index,neighbor in enumerate( self.graph[vertex] ):
            if index == len( self.graph[ vertex ] ) - 1:
                print "and " + str( neighbor )
            else:
                print str( neighbor ),


    def displayAllConnections( self ):
        for vertex in self.graph:
            if not self.graph[vertex]:
                print "Vertex " + str( vertex ) + " is not connected to any other vertices"
            else:
                print "Vertex " + str( vertex ) + " is connected to",
                if len( self.graph[vertex] ) == 1:
                    print str( *self.graph[vertex] )
                else:
                    for index,neighbor in enumerate( self.graph[vertex] ):
                        if index == len( self.graph[ vertex ] ) - 1:
                            print "and " + str( neighbor )
                        else:
                            print str( neighbor ),


    def shortestPath( self, source, destination ):
        if not self._validVertex( source ):
            print "Please enter a valid source vertex"
            return
        if not self._validVertex( destination ):
            print "Please enter a valid destination vertex"
            return

        shortestPath = self._shortestPathAlgo( source, destination )

        if not shortestPath:
            print "No path exists from " + str( source ) + " to " + str( destination )
            return

        print "The shortest path from " + str( source ) + " to " + str( destination ) + " is"
        for index,vertex in enumerate( shortestPath ):
            if index == len( shortestPath ) - 1:
                print str( vertex )
            else:
                print str( vertex ) + " --> ",

    #Algorithm source: https://www.python.org/doc/essays/graphs/
    def _shortestPathAlgo( self, source, destination, path=[] ):
        path = path + [source]
        if source == destination:
            return path
        shortestPath = None
        for vertex in self.graph[source]:
            if vertex not in path:
                currentPath = self._shortestPathAlgo( vertex, destination, path )
                if currentPath:
                    if not shortestPath or len( currentPath ) < len( shortestPath ):
                        shortestPath = currentPath
        return shortestPath




g1 = Graph(5)
g1.addVertex(6)
g1.addConnection( 1, [2,3] )
g1.addConnection( 2, [5,6] )
g1.addConnection( 3, [2] )
g1.addConnection( 5, [3,6] )
g1.addConnection( 6, [4] )
g1.displayAllConnections()
g1.shortestPath( 1, 4 )
