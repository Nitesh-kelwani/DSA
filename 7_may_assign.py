# 1. write code to count no of nodes in a binary tree
class Node:
    def __init__(self,val):
        
        self.left=None
        self.right=None
        self.val=val

class BST:
    def __init__(self):
        self.root=None
        self.count=0
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
    
    def inorder(self):
        print("Inorder traversal :")
        temp=self.root
        self._inorder_rec(temp)

    def _inorder_rec(self,root):
        if root:
            self._inorder_rec(root.left)
            print(root.val ,end=" ")        # left-> root->right
            self.all_ele.append(root.val)
            self._inorder_rec(root.right)

    def No_node(self):
        print("Inorder traversal :")
        temp=self.root
        self.no_ofNode(temp)
        return self.count

    def no_ofNode(self,root):
        if root:
            self.count+=1
            self.no_ofNode(root.left)
            # print(root.val ,end=" ")        # left-> root->right
            self.no_ofNode(root.right)
        # return self.count
        

    def preorder(self):
        print("preorder traversal :")
        temp=self.root
        self._preorder(temp)

    def search(self,key):
        return self._search_rec(self.root,key)
    
    def _search_rec(self,root,key):
        if root is None or root.val==key:
            return root
        if key<root.val:
            return self._search_rec(root.left,key)
        else:
            return self._search_rec(root.right,key)

    def _preorder(self,root):
        if root:
            print(root.val, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)
    
    def delete(self,key):
        if self.search(key) is None:
            print(f"{key} is not found in the BST")
            return
        self.root=self._delet_rec(self.root,key)
            

    def _delet_rec(self,root,key):
        if not root:
            return root
        if key<root.val:
            root.left=self._delet_rec(root.left,key)
        elif key>root.val:
            root.right=self._delet_rec(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp=self._minvalue(root.right)
            root.val=temp.val
            root.right=self._delet_rec(root.right,temp.val)

        return root



    def _minvalue(self,node):
        current=node
        while current.left:
            current=current.left
        return current





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
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)



bst.delete(50)
bst.inorder()

no_ofnodes=bst.No_node()
if no_ofnodes!=0:
    print(f"\nThe number of nodes present in tree are : {no_ofnodes}")
else:
    print("The tree is empty")
