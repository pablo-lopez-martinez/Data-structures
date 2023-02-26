#Linked list implementation with head node

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():

    def __init__(self):
        self.head=Node(None)
        self.head.next=None

    def print_list(self):
        tmp=self.head.next
        while (tmp.next!=None): 
            print(tmp.data,end=" -> ")
            tmp=tmp.next
        print(tmp.data)

    def is_empty_list(self):
        return self.head.next==None

    def insert_item(self, item, position):
    
        #The element is inserted at the begining
        if (position)==self.head.next:
            item.next=self.head.next
            self.head.next=item
            return
        
        #The element is inserted at the end 
        if (position)==None:
            i=self.head
            while (i.next!=None): i=i.next
            i.next=item
            return 
        
        #Default: The element is inserted in the middle 
        i=self.head.next
        while (i.next!=position): i=i.next
        i.next=item
        item.next=position

    def delete_item(self,item):
        
        if (self.is_empty_list()): 
            raise Exception("Empty List")

        #If the element to delete is at the begining
        if (self.head.next==item): 
            self.head.next=item.next
            return

        #Any other case
        i=self.head.next
        while (i.next!=None and i.next!=item):
            i=i.next
        if (i.next==None): 
            raise Exception("No such element")
          
        i.next=item.next
        

    def find_item(self,data)-> Node: 
        i=self.head
        while (i!=None and i.data!=data):
            i=i.next
        if (i!=None):
            return i.data
        print("The element doesn't exist in the list")




