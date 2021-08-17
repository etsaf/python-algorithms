class BinTree():
    def _init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def printInorder(self):
        if self:
            printInOrder(self.left)
            print(self.data)
            printInOrder(self.right)

    def printPostorder(self):
        if self:
            printPostorder(self.left)
            printPostorder(self.right)
            print(self.data)
        
    def printPreorder(self):
        if self:
            print(self.data)
            printPreorder(self.left)
            printPreorder(self.right)
    
#Binary Heaps (min-heap) 
class Node():
    def __init__(self, data):
        self.data = data
        self.children = []