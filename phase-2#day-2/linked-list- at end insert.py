class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insertend(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head  #temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp.data means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
#node creation and initialization
n=Node(10)   #so n.data in node class will be
obj.head=n  #assigning first node as head
n1=Node(20)
n.next=n1    #next node value
n2=Node(30)
n1.next=n2
print("before inserting")
obj.display()
print(" ")
print("after inserting")
obj.insertend(100)
obj.display()
