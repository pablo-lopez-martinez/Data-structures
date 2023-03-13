class BSTree():

    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if self.value==None:
            self.value=value
        elif (value <self.value):
            if self.left is None:
                self.left=BSTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=BSTree(value)
            else:
                self.right.insert(value)

    def find(self,value):
        if value<self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
            
        

    def inorder(self):
        if (self.left): 
            self.left.inorder()
        print(self.value, end=" ")
        if (self.right):
            self.right.inorder()

    def postorder(self):
        pass

    def preorder(self):
        print(self.value, end=" ")
        if (self.left): 
            self.left.preorder()
        if (self.right):
            self.right.preorder()



