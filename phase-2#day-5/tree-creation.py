class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)

node1.leftchild=node2
node1.rightchild=node3
node2.leftchild=node4
node2.rightchild=node5
node3.leftchild=node6
node3.rightchild=node7

print("Root Node is:",node1.data)
print("rootnode.left is:",node1.leftchild.data)
print("rootnode.right is:",node1.rightchild.data)
print("node1.leftchild.left is:",node2.data)
print("node1.leftchild.right is:",node2.leftchild.data)
print("node1.rightchild.right is:",node2.rightchild.data)
print("node1.rightchild is:",node3.data)
print("node3.leftchildis:",node3.leftchild.data)
print("node3.rightchild is:",node3.rightchild.data)



