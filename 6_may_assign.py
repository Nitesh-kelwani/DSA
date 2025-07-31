class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

class BST:
    def __init__(self):
        self.root=None
        self.all_ele=[]

    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self._insert_rec(self.root,key)

    def _insert_rec(self,root,key):
        if key<root.val:
            if root.left is None:
                root.left=Node(key)
            else:
                self._insert_rec(root.left,key)
        else:
            if root.right is None:            
                root.right=Node(key)
            else:
                self._insert_rec(root.right,key)
    
    def inorder_store(self):
        
        temp=self.root
        all=[]
        all=self._inorder_rec(temp)
        return all

    def _inorder_rec(self,root):
        if root:
            self._inorder_rec(root.left)
                  # left-> root->right
            self.all_ele.append(root.val)
            self._inorder_rec(root.right)
            return self.all_ele

    

    def search(self,key):
        return self._search_rec(self.root,key)
    
    def _search_rec(self,root,key):
        if root is None or root.val==key:
            return root
        if key<root.val:
            return self._search_rec(root.left,key)
        else:
            return self._search_rec(root.right,key)

    
    def delete(self, key):
        if self.search(key) is None:
            print(f"Key {key} not found in BST.")
            return
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self._delete_rec(root.left, key)
        elif key > root.val:
            root.right = self._delete_rec(root.right, key)
        else:
            # Here two conditions are possible for deletion:, leaf node or node with single child
            # having only child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left


            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._delete_rec(root.right, temp.val)

        return root

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def is_bst(self):
        ele=self.inorder_store()
        for i in range(1,len(ele)):
            if ele[i]<=ele[i-1]:
                return False
        return True

    def level_travlser(self):
        if self.root is None:
            return
        queue=[]
        queue.append(self.root)
        while queue:
            node=queue.pop(0)
            
            print(node.val,end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

bst = BST()
insert_ele=[50,30,20,40,70,60,80]
for i in insert_ele:
    bst.insert(i)

# insert_ele.sort()
# print(insert_ele)


# all_elements=bst.inorder_store()
# # print(all_elements)
# if all_elements==insert_ele:
#     print("The binary tree is BSt")
# else:
#     print("This binary tree is not BST")

res=bst.is_bst()
print(res)

