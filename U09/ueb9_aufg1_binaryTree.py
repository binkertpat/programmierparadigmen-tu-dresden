class binTree:
    root = None

    def __init__(self, valueList):
        for i in valueList:
            self.insertNode(i)
            
    def __str__(self):
        return str(self.__class__) + ": " + str(self.root.__dict__)
    
    def insertNode(self, value):
        newNode = node(value)
        if self.root == None:
            self.root = newNode
        else:
            nextNeighbour = self._findNextNeighbour(newNode, self.root)
            if newNode.value >= nextNeighbour.value:
                nextNeighbour.rightChild = newNode
            else:
                nextNeighbour.leftChild = newNode

    def _findNextNeighbour(self, newNode, currentNode):
        if newNode.value >= currentNode.value:
            if currentNode.rightChild == None:
                return currentNode
            else:
                return self._findNextNeighbour(newNode, currentNode.rightChild)
        else:
            if currentNode.leftChild == None:
                return currentNode
            else:
                return self._findNextNeighbour(newNode, currentNode.leftChild)
    
    def searchForNodeRek(self, value):
        return self._searchRek(self.root, value)
    
    def searchForNodeIterativ(self, value):
        return self._searchIterativ(self.root, value)
        
    def _searchRek(self, node, value):
        if node == None or node.value == value:
            return node
        elif node.value > value:
            return self._searchRek(node.leftChild, value)
        elif node.value < value:
            return self._searchRek(node.rightChild, value)
        
    def _searchIterativ(self, node, value):
        watchedNode = node
        while watchedNode:
            if watchedNode.value == value:
                return watchedNode
            if value < watchedNode.value:
                watchedNode = watchedNode.leftChild
            if value > watchedNode.value:
                watchedNode = watchedNode.rightChild
        return watchedNode
    
    def addAllNodesRek(self):
        return self._addAllRek(self.root)
    
    def addAllNodesIterativ(self):
        return self._addAllIterativ(self.root)
    
    def _addAllRek(self, node):
        if node == None:
            return 0
        return self._addAllRek(node.leftChild) + self._addAllRek(node.rightChild) + node.value
    
    def _addAllIterativ(self, node):
        NodesToCheck = []
        summe = 0
        NodesToCheck.append(node)
        while len(NodesToCheck) > 0:
            watchedNode = NodesToCheck[0]
            NodesToCheck.pop(0)
            if watchedNode != None:
                summe += watchedNode.value
                NodesToCheck.append(watchedNode.leftChild)
                NodesToCheck.append(watchedNode.rightChild)
        return summe
        
class node:
    value = None
    leftChild = None
    rightChild = None
    
    def __init__(self, value=0):
        self.value = value
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
        
b1 = binTree([2,4,3,5,66,22,13,16,1])
print("searchning the node with the value 13 recursiv:")
print(b1.searchForNodeRek(13))

print("\nsearchning the node with the value 13 iterativ:")
print(b1.searchForNodeIterativ(13))

print("\nsumming all nodes recursiv:")
print(b1.addAllNodesRek())

print("\nsumming all nodes iterativ:")
print(b1.addAllNodesIterativ())
