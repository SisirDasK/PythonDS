class Node( object ):

    def __init__( self ):
        self.word = None
        self.nodes = {}

    def insert( self, word, originalWord ):
        for index,letter in enumerate( word ):
            if letter in self.nodes:
                self.nodes[letter].insert( word[ index + 1: ], originalWord)
                return
            else:
                self.nodes[letter] = Node()
                print letter + " inserted"
                if index == len( word ) - 1:
                    self.word = originalWord
                    print originalWord + " added"
                self.nodes[letter].insert( word[ index + 1: ], originalWord )
                return


    def getWords( self ):
        for node in self.nodes:
            if self.nodes[node].word:
                print self.nodes[node].word
            else:
                self.nodes[node].getWords()

class Trie( object ):

    def __init__( self ):
        self.root = Node()

    def insertWord( self, word ):
        self.root.insert( word, word )

    def getAllWords( self ):
        self.root.getWords()



myTrie = Trie()
myTrie.insertWord( "sisir" )
myTrie.insertWord( "sisil" )
myTrie.insertWord( "sisid" )
myTrie.insertWord( "Theertha" )
myTrie.insertWord( "Theerdha" )

myTrie.getAllWords()
