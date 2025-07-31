class ImplementStack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, value):
        self.stack.append(value)
        self.top += 1
        return
    
    def pop(self):
        if self.is_empty():
            return "Stack is underflow"
        removed_element = self.stack[self.top]
        self.stack.pop(self.top)
        self.top -=1
        
        return removed_element
        
    def peek(self):
        return self.stack[self.top]
        
    def display(self):
        print("\n Printing the elements inside stack: ")
        for i in self.stack:
            print(i, end= "\t")
        return 


def validparenth(str):
    st=ImplementStack()
    for char in str:
        if char in "({[":
            print(char)
            st.push(char)
        elif char in ")}]":
            if st.is_empty():
                return
            elif st.peek()==char:
                print(char)
                st.pop()
            else:
                return
    return "valid parnthesis" 

print(validparenth("abc({}[fjk])"))