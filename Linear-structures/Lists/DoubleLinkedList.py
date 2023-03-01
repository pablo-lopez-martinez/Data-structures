class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList():

    def __init__(self):
        self.head=Node()
        
    def print_list(self):
        tmp=self.head.next
        while (tmp.next!=None): 
            print(tmp.data,end=" -> ")
            tmp=tmp.next
        print(tmp.data)

    def is_empty_list(self):
        return self.head.next==None
    
    def insert_item(self, data, position=None):
        
        item=Node(data)
        #The element is inserted at the end 
        if (position==None):
            i=self.head
            while(i.next!=None): i=i.next
            i.next=item
            item.prev=i
            return

        #The element is inserted at the begining
        if (self.head.next==position):
            self.head.next=item
            item.prev=self.head
            item.next=position
            position.prev=item
            return


        #The element is inserted in the middle
        #Through double linking the list its way easier than with simple linked list
        prev=position.prev
        position.prev=item
        item.next=position
        item.prev=prev
        prev.next=item

    def find_item(self,data):
        i=self.head
        while (i!=None and i.data!=data):
            i=i.next
        if (i!=None):
            return i
        raise Exception("No such element")
    
    def delete_item(self,data):
        if (self.is_empty_list()): 
            raise Exception("Empty List")
        
        i=self.head.next
        #If the element to delete is at the begining
        if (i.data==data): 
            i.next.prev=i
            self.head.next=i.next
            return

        #Any other case
        i=self.find_item(data)
        prev=i.prev
        prev.next=i.next
        i.next.prev=prev
            

        


        