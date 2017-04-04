from collections import OrderedDict

class Tree( object ):

    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode( self, to, data):
        if to == self.data:
            self.children.append( Tree( data ) )
            result = str( data ) + " added to " + str( self.data )
            return result
        else:
            result = None
            for child in self.children:
                if not result:
                    result = child.addNode( to, data)
            return result

    def displayTree( self ):
        print str( self.data ) + "-->",
        if not self.children:
            print "No child nodes",
        for child in self.children:
            print child.data,
        print

        for child in self.children:
            child.displayTree()



root = Tree( 10 )

treeDict = OrderedDict()

treeDict[10] = [50, 60, 70]
treeDict[50]= [510]
treeDict[60]= [600]
treeDict[70]= [700, 710]
treeDict[510]= [5100]
treeDict[5]= [5100]

for parent in treeDict.keys():
    for child in treeDict[parent]:
        result = root.addNode( parent, child )
        if not result:
            print str( parent ) + " not found"
        else:
            print result

root.displayTree()
