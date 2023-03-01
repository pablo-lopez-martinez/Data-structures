MAX_SIZE=10

class Stack():
    def __init__(self):
        self.stack=[]
        self.size=0

    def __str__(self):
        return ' -> '.join(str(i) for i in self.stack)

    def is_empty(self):
        return self.stack==[]
        
    def top(self):
        if (self.is_empty()):
            raise Exception("The stack is empty")
        return self.stack[self.size-1]

    def push(self,data):
        if (self.size==MAX_SIZE):
            raise Exception("The stack is full")
        self.size+=1
        self.stack.append(data)
        

    def pop(self):
        if (self.is_empty()):
            raise Exception("The stack is empty")
        self.size-=1
        self.stack.pop(self.size)
        

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.pop()
print(stack)
