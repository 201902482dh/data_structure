class Queue:
    MAX_QSIZE = 100
    def __init__(self):
        self.items = [None]*Queue.MAX_QSIZE
        self.front = -1     #첫번째 요소 앞의 인덱스
        self.rear = -1      #마지막 요소 인덱스
        self.size = 0
    def isEmpty(self):
        return self.size==0
    def enqueue(self,e):
        if self.size==len(self.items):
            print("Queue is full")
            self.resize(2*len(self.items))  #가득차면 2배확장
        else:
            self.rear = (self.rear+1)%(len(self.items))
            self.items[self.rear] = e
            self.size+=1
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front = (self.front+1)%(len(self.items))
            e = self.items[self.front]
            self.size-=1
            return e
    def resize(self,cap):
        olditems = self.items
        self.items = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = olditems[walk]
            walk = (walk+1)%len(olditems)
        self.front = -1
        self.rear = self.size-1

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def clear(self):
        self.items = []
    def push(self,e):
        self.items.append(e)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items[-1]
