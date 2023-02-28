MAX_SIZE=10

class Queue():

    def __init__(self):
        self.queue=[]
        self.size=0
    
    def __str__(self):
        return ' -> '.join(str(i) for i in self.queue)
    
    def is_empty(self):
        return (self.queue==[])
    
    def enqueue(self,item):
        if (self.size==MAX_SIZE):
            raise Exception("Full queue")
        self.queue.append(item)
        self.size+=1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Empty queue")
        self.size-=1
        return self.queue.pop(0)
            
    
    

    
    
        
        



