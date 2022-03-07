import random

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
     
def insertRandomly(tree, iterations):
    for i in range(0, iterations):
        tree._insert(random.randint(0,10))
    print("True")

firstBinaryTree = BinaryTree()
iteration = 10

print("add " + str(iteration) + " randomly numbers to the tree:")
insertRandomly(firstBinaryTree, iteration)

print("\nsearchning node with value 10:")
print(firstBinaryTree._searchingNode(10))

print("\nprinting tree elements in sorted order:")
firstBinaryTree._printInSortedOrder()
