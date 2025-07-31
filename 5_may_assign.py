# getting the sum of all the elements in 2 linked lists

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Sll:
    def __init__(self):
        self.head=None

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
        
    def insertat_posi(self,pos,val):
        newnode=Node(val)
        if pos<0:
            return
        elif self.head is None and pos>0:
            return
        if pos==0:
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        cur_pos=0
        while current and cur_pos < pos - 1:
            current = current.next
            cur_pos += 1        
        if not current or cur_pos != pos - 1:
            return
        newnode.next = current.next
        current.next = newnode
        return
    
    def display(self):
        temp = self.head
        print("displaying elements in a linked list")
        sum=0
        while temp:
            print(temp.value, end= "\t")
            sum+=temp.value
            temp = temp.next
        return sum
    
    def sumofall(self):
        temp = self.head
        print("displaying elements in a linked list")
        sum=0
        while temp:
            sum+=temp.value
            temp = temp.next
        return sum
    


l1=Sll()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insertat_posi(1,40)
sum1=l1.sumofall()
l2=Sll()
l2.insert(2)
l2.insert(3)
l2.insert(4)
l2.insertat_posi(1,1)
sum2=l2.sumofall()
print()
print(f" The sum of both Linked list is : {sum1+sum2}")