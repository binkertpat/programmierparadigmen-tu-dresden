import random
import time

class Node:
    value = None
    leftChild = None
    rightChild = None
    
    def __init__(self, value):
        self.value = value
        
class BinaryTree:
    root = None
    
    def __init__(self):
        self.root = None
           
    def _insert(self,value):
        if(self.root == None):
            self.root = Node(value)
        else:
            self.__helpInsertFunction(value, self.root)
    
    def __helpInsertFunction(self, value, node):
        if(node.value > value):
            if(node.leftChild == None):
                node.leftChild = Node(value)
            else:
                self.__helpInsertFunction(value, node.leftChild)
        else:
            if(node.rightChild == None):
                node.rightChild = Node(value)
            else:
                self.__helpInsertFunction(value, node.rightChild)
                
    def _searchingNode(self, value):
        return self.__searchRekursiv(self.root, value)
    
    def __searchRekursiv(self, node, value):
        if node == None or node.value == value:
            return node
        elif node.value > value:
            return self.__searchRekursiv(node.leftChild, value)
        elif node.value < value:
            return self.__searchRekursiv(node.rightChild, value)
    
    def _printInSortedOrder(self, node = None):
        watchedNode = self.root
        if node:
            watchedNode = node
        if watchedNode.leftChild:
            self._printInSortedOrder(watchedNode.leftChild)
        print(watchedNode.value)
        if watchedNode.rightChild:
            self._printInSortedOrder(watchedNode.rightChild)
            
class NodeForTenery(Node):
    middleChild = None
    
    def __init__(self, value):
        super(NodeForTenery, self).__init__(value)
            
class TeneryTree(BinaryTree):
    
    def _insert(self, value):
        return self._helpInsertFunction(value)
    
    def _helpInsertFunction(self, value):     
        newNode = NodeForTenery(value)
        if (self.root == None):
            self.root = newNode
            return
        getFirstInteger = int(str(abs(value))[0])
        
        watchedNode = self.root
        while watchedNode.value != None:
            if 0 <= getFirstInteger <= 3:
                if watchedNode.leftChild == None:
                    watchedNode.leftChild = newNode
                    return True
                watchedNode = watchedNode.leftChild
                continue
                
            if 4 <= getFirstInteger <= 6:
                if watchedNode.middleChild == None:
                    watchedNode.middleChild = newNode
                    return True
                watchedNode = watchedNode.middleChild
                continue
            
            if 7 <= getFirstInteger <= 9:
                if watchedNode.rightChild == None:
                    watchedNode.rightChild = newNode
                    return True
                watchedNode = watchedNode.rightChild
                continue
        return False
    
    def _searchingNodeOLD(self, value):
        watchedNode = self.root
        getFirstInteger = int(str(abs(value))[0])
        while watchedNode.value != value:
            if 0 <= getFirstInteger <= 3:
                watchedNode = watchedNode.leftChild
                continue
            elif 4 <= getFirstInteger <= 6:
                watchedNode = watchedNode.middleChild
                continue
            elif 7 <= getFirstInteger <= 9:
                watchedNode = watchedNode.rightChild
                continue
        return watchedNode
    
    def _searchingNode(self, value):
        #return self.__searchIterativ(value)
        return self.__searchRekursiv(self.root, value)
    
    def __searchIterativ(self, value):
        watchedNode = self.root
        getFirstInteger = int(str(abs(value))[0])
        while watchedNode.value != value:
            if 0 <= getFirstInteger <= 3:
                watchedNode = watchedNode.leftChild
                continue
            elif 4 <= getFirstInteger <= 6:
                watchedNode = watchedNode.middleChild
                continue
            elif 7 <= getFirstInteger <= 9:
                watchedNode = watchedNode.rightChild
                continue
        return watchedNode
        
    def __searchRekursiv(self, node, value):
        getFirstInteger = int(str(abs(value))[0])
        if node == None or node.value == value:
            return node
        elif 0 <= getFirstInteger <= 3:
            return self.__searchRekursiv(node.leftChild, value)
        elif 4 <= getFirstInteger <= 6:
            return self.__searchRekursiv(node.middleChild, value)
        elif 7 <= getFirstInteger <= 9:
            return self.__searchRekursiv(node.rightChild, value)

def insertRandomly(tree1, tree2, iterations):
    for i in range(0, iterations):
        toInsertValue = random.randint(1,100)
        tree1._insert(toInsertValue)
        tree2._insert(toInsertValue)
    print("True")

firstBinaryTree = BinaryTree()
firstTeneryTree = TeneryTree()
iteration = 10

print("add " + str(iteration) + " randomly numbers to the trees:\n")
insertRandomly(firstBinaryTree, firstTeneryTree, iteration)

beginBinaryTreeSearch = 0
beginTeneryTreeSearch = 0
endBinaryTreeSearch = 0
endTeneryTreeSearch = 0

for i in range(500):
    beginBinaryTreeSearch += time.perf_counter()
    firstBinaryTree._searchingNode(50)
    endBinaryTreeSearch += time.perf_counter()

    beginTeneryTreeSearch += time.perf_counter()
    firstTeneryTree._searchingNode(50)
    endTeneryTreeSearch += time.perf_counter()

timeBinaryTreeSearch = endBinaryTreeSearch-beginBinaryTreeSearch
timeTeneryTreeSearch = endTeneryTreeSearch-beginTeneryTreeSearch
timeBinaryTreeSearch = timeBinaryTreeSearch / 500
timeTeneryTreeSearch = timeTeneryTreeSearch / 500

print("\nZeitmessung:")
print("%.50f" % timeBinaryTreeSearch)
print("%.50f" % timeTeneryTreeSearch)

print("\npercentage:")
print("%.2f" % ((timeBinaryTreeSearch/timeTeneryTreeSearch) * 100) + " %")

