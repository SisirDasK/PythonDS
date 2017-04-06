myList = ["Sisir", "Theertha", "Pavan", 12345]

print "Original list: " + str( myList )

print "Retreiving an element from the list"
print "First element: " + myList[0]
print "Last element: " + str( myList[-1] )
print "Second element to last element: " + str( myList[1:] )

print "\n\nInsertion and deletion of elements"
myList.append("Last item")
myList.insert(1, "Second item")
print "After insertion of new elements"
print myList
print "After deletion of new elements"
myList.remove("Last item")
myList.remove("Second item")
print myList

print "\n\nThe pop and the index function"
myList.append("Last item")
myList.insert(1, "Second item")
print myList
print "'" + myList.pop() + "' popped"
print "'" + myList.pop(1) + "' popped"
print "Index of 'Sisir' is " + str ( myList.index("Sisir") )

list2 = ["This", "is", "another", "list"]
#appending another list to existing list
myList.extend( list2 )
print myList

myList.sort()
print "Sorted list: " + str( myList )

myList.reverse()
print "Reversed list: " + str( myList )

#list comprehension

#Constructing another list of only strings fromt the first list

strList = [ ele for ele in myList if type( ele ) == str ]

print "Old list: " + str( myList )

print "New list: " + str( strList )
