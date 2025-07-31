import re
# 1. Find the second highest element in an array
# listt=[10,15,62,52,14,36,52]
# sortedd=sorted(listt)
# # print(sortedd)
# index=len(listt)-2
# print(sortedd[index])

result=[]
# # # 2. Remove duplicate lines from a text file (by creating a new file)
# with open("test1.txt",'r') as f:
    
#     with open("result.txt",'w') as fp:
#         line=f.readlines()
#         for i in range(len(line)):
#             if line[i].strip() in result:
#                 pass
#             else:
#                 # str=result.append(line[i])
#                 result.append(line[i].strip())
#                 fp.write(line[i].strip())
#                 fp.write("\n")

# print(result)

# 3. write Insert method for Circular LInked list

# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.prev=None
#         self.next=None

# class Cll:
#     def __init__(self):
#         self.head=None

#     def insert(self,val):
#         newnode=Node(val)
#         if not self.head:
#             self.head=newnode
#             newnode.next=self.head
#             return
#         current=self.head
#         while current.next!=self.head:
#             current=current.next
#         current.next=newnode
#         newnode.prev=current
#         newnode.next=self.head
#         return
    
#     def display(self):
#         current=self.head
#         while current.next!=self.head:
#             print(current.val,end="\t")
#             current=current.next
#         print(current.val)
#         return
    
# demo=Cll()
# demo.insert(20)
# demo.insert(45)
# demo.insert(62)
# demo.insert(85)
# demo.display()
         

# ➕
# Remove All Adjacent Duplicates: Remove adjacent duplicates in a string using stack logic.
# Example: "abbaca" → "ca"

class stack:
    def __init__(self):
        self.stack=[]
        self.top=-1

    def isempty(self):
        return self.top==-1
    
    def push(self,val):
        self.top+=1
        self.stack.append(val)
        return
    
    def pop(self,a=None):
        if self.isempty():
            return "Stack underflow"
        if a is None:
            self.stack.pop(self.top)
            self.top-=1
        else:
            self.stack.pop(a)
        return
    
    def delet_middle(self):
        if self.isempty():
            return "Stack underflow"
        middle=len(self.stack)//2
        self.pop(middle)
        return
    
    def adjus_dupli(self):
        l=len(self.stack)
        print(l)
        n=l
        for i in range(l-1):
            if self.stack[n-1]==self.stack[n-2]:
                print(self.stack[n-1])
                print(self.stack[n-2])
                self.pop(n-1)
                self.pop(n-2)
                n-=2
            else:
                n-=1
        return
    
    def display(self):
        for val in self.stack:
            print(f"{val} ", end=" ")
        print("")
        return
    
    def peek(self):
        # print(self.stack[self.top])
        return self.stack[self.top]



s=stack()
s.push("h")
s.push("h")
s.push("d")
s.push("k")
s.push("d")
s.push("l")
s.push("o")
s.push("l")
s.push("p")
s.push("s")
s.push("p")
s.push("s")

# s.adjus_dupli()
# s.display()

# # Delete the middle element from the stack
# s.delet_middle()
# s.display()


# Remove All Adjacent Duplicates: Remove adjacent duplicates in a string using stack logic.
s1=stack()
def adj_ele(val):
    chars=list(val)
    for char in chars:
        if s1.isempty():
            s1.push(char)
        else:
            if s1.peek()==char:
                s1.pop()
            else:
                s1.push(char)
    result=''.join(chars)
    return result

# adj_ele("hhdkdlolpsps")
# s1.display()

#   3. Take some long string 
#      Like "Hi bro, how are you are "

#      You just need to find the 'are'
#     How many times

str1="apple apple banana apple orange banana apple grape orange banana"
matches=re.findall(r"apple",str1)
print(len(matches))