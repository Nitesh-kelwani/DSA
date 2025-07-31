class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        return
    
    def search(self ,key):
        current=self.head
        pos=0
        if current.value==key:
            print(f"{key} found at {pos}th position")
        elif current.value!=key:
            while current.next:
                current=current.next
                pos+=1
                if current.value==key:
                    print(f"{key} found at {pos}th position")
        else:
            print(f"{key} is not found in linked list")


    def insertAtPosition(self,position, value):
        newnode = Node(value)
        # Edge case -1
        if position < 0:
            return
        # edge case -2
        elif self.head is None and position >0:
            return
        # edge case -3
        if position ==0:
            newnode.next = self.head
            self.head = newnode
            return
        current = self.head
        current_position = 0

        while current and current_position < position - 1:
            current = current.next
            current_position += 1
        

        if not current or current_position != position - 1:
            return
        newnode.next = current.next
        current.next = newnode
        return
        
    def delete(self,value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is not None and current.next.value == value:
            # ignore the current.next node and point to the next node
            current.next = current.next.next
        return
    
    def display(self):
        temp = self.head
        print("displaying elements in a linked list")
        while temp:
            print(temp.value, end= "\t")
            temp = temp.next
        return

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insertAtPosition(1, 15)
ll.insertAtPosition(0, 5)
ll.insertAtPosition(5, 35)
ll.delete(20)
ll.display()
ll.search(36)