#Linked list implementation with head node

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setNext(self,node):
        self.next=node

class Linked_list():

    def __init__(self):
        self.head=Node(None)
        self.head.next=None

    def print_list(self):
        tmp=self.head.next
        while (tmp.getNext()!=None): 
            print(tmp.getData(),end=" -> ")
            tmp=tmp.getNext()
        print(tmp.getData())

    def is_empty_list(self):
        return self.head.getNext()==None

    def insert_item(self, item, position=None):
    
        #The element is inserted at the begining
        if (position)==self.head.getNext():
            item.next=self.head.getNext()
            self.head.setNext(item)
            return
        
        #The element is inserted at the end 
        if (position)==None:
            i=self.head
            while (i.getNext()!=None): i=i.getNext()
            i.setNext(item)
            return 
        
        #Default: The element is inserted in the middle 
        i=self.head.getNext()
        while (i.getNext()!=position): i=i.getNext()
        i.setNext(item)
        item.setNext(position)

    def delete_item(self,item):
        
        if (self.is_empty_list()): 
            raise Exception("Empty List")

        #If the element to delete is at the begining
        if (self.head.getNext()==item): 
            self.head.next=item.getNext()
            return

        #Any other case
        i=self.head.getNext()
        while (i.getNext()!=None and i.getNext()!=item):
            i=i.getNext()
        if (i.getNext()==None): 
            raise Exception("No such element")
          
        i.setNext(item.next)
        

    def find_item(self,data)-> Node: 
        i=self.head
        while (i!=None and i.getData()!=data):
            i=i.getNext()
        if (i!=None):
            return i.getData()
        print("The element doesn't exist in the list")


list=Linked_list()
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
list.insert_item(node1)
list.insert_item(node2)
list.insert_item(node3)
list.insert_item(node4,node2)
list.delete_item(node2)
list.print_list()




