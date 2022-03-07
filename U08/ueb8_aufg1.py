class ListElement:
    value = None
    nextElement = None
    
    def __init__(self, value):
        self.value = value
        
class Liste:
    def __init__(self, root = None):
        self.root = root

    def _getData(self):
        return self.root.value
    
    def _getNextElement(self):
        return self.root.nextElement
    
    def _deleteByValue(self, value, elementOfList = None):
        if elementOfList == None:
            elementOfList = self.root
        watchedNode = elementOfList
        if watchedNode == None:
            return watchedNode
        elif watchedNode.value == value:
            return watchedNode.nextElement
        else:
            watchedNode.nextElement = self._deleteByValue(value, watchedNode.nextElement)
            return watchedNode
        
    def _delteByIndex(self, index):
        watchedNode = self.root
        itemCounter = 1
        while watchedNode:
            if index-1 == itemCounter:
                changingNode = watchedNode
            if index == itemCounter:
                NodeToDelete = watchedNode
            itemCounter +=1
            watchedNode = watchedNode.nextElement
        changingNode.nextElement = NodeToDelete.nextElement
        del NodeToDelete
        return True

    def _getListOfSameValues(self, value):
        watchedNode = self.root
        returnList = []
        while watchedNode:
            if watchedNode.value == value:
                returnList.append(watchedNode)
            watchedNode = watchedNode.nextElement
        return returnList
    
    def _multiplyValueWithIndex(self):
        watchedNode = self.root
        positionCounter = 1
        while watchedNode:
            watchedNode.value = watchedNode.value * positionCounter
            positionCounter += 1
            watchedNode = watchedNode.nextElement
        return True
    
    def _appendBegin(self, value):
        newNode = ListElement(value)
        newNode.nextElement = self.root
        self.root = newNode
    
    def zaehlen_rek (self, element=None): 
        if element is None:
            k = self.root
        else:
            k = element

        if k.nextElement == None:
            return 1
        else:
            return 1 + self.zaehlen_rek(k.nextElement)

    def _appendEnd(self, value):
        newNode = ListElement(value)
        if self.root == None:
            self.root = newNode
        else:
            self._findLastElement().nextElement = newNode
        
    def _findLastElement(self):
        last = self.root
        while last.nextElement:
            last = last.nextElement
        return last
        
    def _isTheListEmpty(self):
        return self.root is None
    
    def _sizeOfTheList(self):
        watchedNode = self.root
        counter = 0
        while watchedNode is not None:
            counter += 1
            watchedNode = watchedNode.nextElement
        return counter
       
    def _mult_rekursiv(self, elementOfList):
        if elementOfList == None:
            return 1
        else:
            return (elementOfList.value * self._mult_rekursiv(elementOfList.nextElement))
    
    def clear(self):
        element = self.root
        while element.nextElement:
            temp = element.nextElement
            element.nextElement = None
            element = temp
        self.root = None
            
    
    def __str__(self):
        result = "["
        watchedNode = self.root
        while watchedNode: 
            result += ('' if result == '[' else ", ") + str(watchedNode.value)
            watchedNode = watchedNode.nextElement
        result += "]"
        return result

def mult_iterativ(liste):
    watchedNode = liste.root
    product = 1
    while watchedNode != None:
        product *= watchedNode.value
        watchedNode = watchedNode.nextElement
    return product

def mult_rekursiv(liste):
    return liste._mult_rekursiv(liste.root)
    
linkedList = Liste()
print("linked list created\n")

linkedList._appendEnd(6)
linkedList._appendEnd(66)
linkedList._appendEnd(9)
linkedList._appendEnd(77)
linkedList._appendEnd(9)

print("added some elements to the linked list\n")

print("Is the list empty?")
print(linkedList._isTheListEmpty())

print("\nHow many elements are in the list?")
print(linkedList._sizeOfTheList())

print("\nprinting the whole list:")
print(linkedList)

print("\niterativ product of all elements in the list:")
print(mult_iterativ(linkedList))

print("\nrecursiv product of all elements in the list:")
print(mult_rekursiv(linkedList))

print("\ndeleting ListObject with value 77:")
print(linkedList._deleteByValue(77))

print("\nthe new list after deleting an item with the value 77:")
print(linkedList)

print("\nlist with all objects with the value 9:")
print(linkedList._getListOfSameValues(9))

print("\nnow multiply the values with their position in the linked list:")
print(linkedList._multiplyValueWithIndex())

print("\nlist after changing the values:")
print(linkedList)

print("\nnow deleting the item with the index 2:")
print(linkedList._delteByIndex(2))


linkedList.clear()
print("\nlist after deleting the item with the index 2:")
print(linkedList)

print("\nlist after deleting the item with the index 2:")
print(linkedList.zaehlen_rek())

