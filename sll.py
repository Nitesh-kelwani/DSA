class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    # you can say this as append also
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
        # edge case -4 & 5 (insert at specific position and insert at end if position matches)
        # we are getting previous index position and reference of that node
        # Find the previous node before the insertion point
        # consider you are searching for 5 in ll 1 25 32 5 13. This loop will stop at 32 (2nd condition)
        # consider you are searching for 13 in ll 1 25 32 15 13. This loop will stop at 15 (2nd condition)
        # consider you are searching for 29 in ll 1 25 32 15 13. This loop will stop at 1st condition as its already at the end of list.
        while current and current_position < position - 1:
            current = current.next
            current_position += 1
        
        # If we're at the end of the list or position is out of bounds
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