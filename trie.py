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
                    self.nodes[letter].word = originalWord
                    print originalWord + " added"
                self.nodes[letter].insert( word[ index + 1: ], originalWord )
                return


    def getWords( self ):
        for node in self.nodes:
            if self.nodes[node].word:
                print self.nodes[node].word
            else:
                self.nodes[node].getWords()

    def getRelatedWords( self, prefix, originalPrefix ):
        for index,letter in enumerate( prefix ):
            if letter in self.nodes:
                #print letter + " found"
                self.nodes[letter].getRelatedWords( prefix[ index + 1: ], originalPrefix)
                return
            else:
                print "No words found that start with " + originalPrefix
                return

        if self.word:
            print self.word
        self.getWords()


class Trie( object ):

    def __init__( self ):
        self.root = Node()

    def insertWord( self, word ):
        self.root.insert( word, word )

    def getAllWords( self ):
        self.root.getWords()

    def getPrefixWords( self, prefix ):
        if len( prefix ) == 0:
            print "\n\nSince no prefix given, printing all words."
            self.getAllWords()
            return
        print "\n\nThe words starting with " + prefix + " are:"
        if prefix[0] not in self.root.nodes:
            print "No words found that start with " + prefix
            return
        self.root.getRelatedWords( prefix, prefix )



#Note: The words are case sensitive. Approach to overcome this: Convert to a UC or LC while storing and perform the search using the same.

myTrie = Trie()
myTrie.insertWord( "sisir" )
myTrie.insertWord( "sisil" )
myTrie.insertWord( "sisid" )
myTrie.insertWord( "Theertha" )
myTrie.insertWord( "Theerdha" )
myTrie.insertWord( "Theerdhd" )
myTrie.insertWord( "Theerthd" )

print "\n\nThe words currently in the trie are:"
myTrie.getAllWords()

myTrie.getPrefixWords("")
