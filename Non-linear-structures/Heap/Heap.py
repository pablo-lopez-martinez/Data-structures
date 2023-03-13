class Heap():
    def __init__(self):
        self.array=[]
        self.last_pos: int=-1

    def percolate_up(self,i: int):
        while i>0 and self.array[int(i/2)]<self.array[int(i)]:
            item=self.array[int(i)]
            self.array[int(i)]=self.array[int(i/2)]
            self.array[int(i/2)]=item
            i/=2

    def insert(self,x):
        self.array.append(x)
        self.last_pos+=1
        self.percolate_up(self.last_pos)

    def percolate_down(self,i):
        while True:
            left_child=2*i+1
            right_child=2*i+2
            j=i
            if right_child<=self.last_pos and self.array[right_child]>self.array[i]:
                i=right_child
            if left_child<=self.last_pos and self.array[left_child]>self.array[i]:
                i=left_child
            item=self.array[j]
            self.array[j]=self.array[i]
            self.array[i]=item
            if (j == i):
                break

    def delete_max(self):
        if (self.last_pos<0):
            raise Exception("Empty heap")
        x=self.array[0]
        self.array[0]=self.array[self.last_pos]
        self.last_pos-=1
        if (self.last_pos>-1):
            self.percolate_down(0)
        return x


heap=Heap()
heap.insert(1)
heap.insert(8)
heap.insert(4)
heap.insert(43)
heap.insert(67)
heap.insert(2)
print(heap.array)
print(heap.delete_max())
print(heap.delete_max())
print(heap.delete_max())
print(heap.delete_max())



