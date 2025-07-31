# Given a singly linked list, the task is to find the middle of the linked list. If the number of nodes are even, 
# then there would be two middle nodes, so return the second middle node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.n=1
        self.count=0
        self.head = None
    # you can say this as append also
    def insert(self, value):
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            self.n+=1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        self.n+=1
        # print(self.n)
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
            self.n+=1
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
        # 10 20 30 40 50 60 70 80
        newnode.next = current.next
        current.next = newnode
        self.n+=1
        return

    def delete(self,value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.n-=1
            return f"{value} is successfully deleted from the list"
            
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is not None and current.next.value == value:
            # ignore the current.next node and point to the next node
            current.next = current.next.next
            self.n-=1
            return f"{value} is successfully deleted from the list"
        else:
            return "Element not found"
         
    
    
    def display(self):
        temp = self.head
        print("displaying elements in a linked list")
        while temp:
            print(temp.value, end= "\t")
            temp = temp.next
        return
    
    def display_mid(self):
        temp = self.head
        print("displaying mid element in a linked list")
        while temp:
            self.count+=1
            # print(self.count)
            if self.count==(self.n+1) // 2:
                print(temp.value, end= "\t")
            # print(temp.value, end= "\t")
            temp = temp.next
        return

# count=0
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
ll.insert(70)
ll.insert(80)
ll.insertAtPosition(4,45)
ll.insertAtPosition(1,15)
print(ll.delete(80))
print(ll.delete(30))
ll.display()
ll.display_mid()
# print(ll.delete(15))
# print((n + 1) // 2)
# check=ll.head.next.next.next.next
# print(check.value)