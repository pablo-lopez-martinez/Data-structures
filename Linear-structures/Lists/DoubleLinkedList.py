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
    
    def insert_item(self, item, position=None):
    
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
        prev=position.prev
        position.prev=item
        item.next=position
        item.prev=prev
        prev.next=position
            

        
list=DoubleLinkedList()

node1=Node(1)
node2=Node(2)
node3=Node(4)
node4=Node(6)
node5=Node(5)
list.insert_item(node1)
list.insert_item(node2)
list.insert_item(node3)
list.insert_item(node4)
list.insert_item(node5,node1)
list.print_list()

        