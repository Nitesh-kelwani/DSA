# create a level by level traverslor using queue and linked list
class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Q:
    def __init__(self):
        self.front=None
        self.rear=None

    def enQ(self,val):
        if self.rear==None:
            self.front=Node(val)
            self.rear=self.front
            return
        self.rear.next=Node(val)
        self.rear=self.rear.next

    def dQ(self):
        if self.rear==None:
            return
        del_ele=self.front.value
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        return del_ele
    
    def peek(self):
        if self.rear is None:
            print("Queue is empty")
            return
        print(self.front.value)
        return
