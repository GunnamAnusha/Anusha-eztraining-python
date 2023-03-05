#BST-DELETE
class Node:
    def _init_(self,key):
        self.key=key
        self.left=None
        self.right=None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

#a new node with given key
def insert(node,key):
    #if tree is empty,return new node
    if node is None:
        return node(key)
    #otherwise recur down the tree
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvaluenode(node):
    current=node
    #loop down to find the leftmost leaf
    while(current.left is not None):
        current=current.left
    return current

def deletenode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deletenode(root.left,key)
    elif (key>root.key):
        root.right=deldetenode(root.right.key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvaluenode(root.right)
        root.key=temp.key
        root.right=deletenode(root.right,temp.key)
    return root
"""               50
                 /  \
               30   70  
              /  \ /  \
            20  40 60 80"""

root=None
root=insert(root, 50)
root=insert(root, 30)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root, 70)
root=insert(root, 60)
root=insert(root, 80)
print("inorder traversal of given tree")
inorder(root)
print("\ndelete 20")
root=deletenode(root,20)
print("inorder traversal of given tree")
inorder(root)
print("\ndelete 30")
root=deletenode(root,30)
print("inorder traversal of given tree")
inorder(root)
print("\ndelete 50")
root=deletenode(root,50)
print("inorder traversal of modified tree")
inorder(root)
