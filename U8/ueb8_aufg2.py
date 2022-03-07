class ListElement:
    value = None
    nextElement = None
    prevElement = None
    
    def __init__(self, value):
        self.value = value
        
class Liste:
    def __init__(self, root = None):
        self.root = root

    def _getData(self):
        return self.root.value
    
    def _getNextElement(self):
        return self.root.nextElement
    
    def _getPrevElement(self):
        return self.root.prevElement
    
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
                changingNodeNext = watchedNode
            if index == itemCounter:
                NodeToDelete = watchedNode
            if index+1 == itemCounter:
                changingNodePrev = watchedNode
            itemCounter +=1
            watchedNode = watchedNode.nextElement
        changingNodeNext.nextElement = NodeToDelete.nextElement
        changingNodePrev.prevElement = changingNodeNext
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
        newNode.prevElement = self.root
    
    def _appendEnd(self, value):
        newNode = ListElement(value)
        if self.root == None:
            self.root = newNode
        else:
            lastNode = self._findLastElement()
            lastNode.nextElement = newNode
            newNode.prevElement = lastNode
        
    def _beforeLastElement(self, value):
        newNode = ListElement(value)
        lastNode = self._findLastElement()  
        watchedNode = self.root
        while watchedNode.nextElement != lastNode.prevElement:
            watchedNode = watchedNode.nextElement
        watchedNode.nextElement = newNode
        newNode.nextElement = lastNode
        lastNode.nextElement = None
        lastNode.prevElement = newNode
        newNode.prevElement = watchedNode
        return True
    
    def _beforeLastElementNew(self, value):
        newNode = ListElement(value)
        lastNode = self._findLastElement()
        preLastNode = self._findPreLastElement()
        newNode.prevElement = preLastNode
        newNode.nextElement = lastNode
        preLastNode.nextElement = newNode
        lastNode.prevElement = newNode
        return True
        
    def _findLastElement(self):
        last = self.root
        while last.nextElement:
            last = last.nextElement
        return last
    
    def _findPreLastElement(self):
        last = self.root
        while last.nextElement.nextElement:
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
    
def findFirstElementIterativ(liste, element = None):
    if element == None:
        return liste.root
    else:
        watchedNode = element
        while watchedNode.prevElement:
            watchedNode = watchedNode.prevElement
        return watchedNode
    
def findFirstElementRekursiv(liste, element = None):
    if element == None:
        return liste.root
    if element.prevElement == None:
        return element
    else:
        return findFirstElementRekursiv(liste, element.prevElement)

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

print("\nlist with all objects with the value 9:")
print(linkedList._getListOfSameValues(9))

print("\nnow multiply the values with their position in the linked list:")
print(linkedList._multiplyValueWithIndex())

print("\nlist after changing the values:")
print(linkedList)

print("\nnow deleting the item with the index 2:")
print(linkedList._delteByIndex(2))

print("\nlist after deleting the item with the index 2:")
print(linkedList)

print("\ninsert the item 34324 before last element:")
print(linkedList._beforeLastElement(34324))

print("\ninsert the item 34324 before last element:")
print(linkedList._beforeLastElementNew(6969))

print("\nlist after adding the new item:")
print(linkedList)

print("\nfind the first element of the linked list:")
print(findFirstElementIterativ(linkedList, linkedList._findLastElement()))
print(findFirstElementRekursiv(linkedList, linkedList._findLastElement()))