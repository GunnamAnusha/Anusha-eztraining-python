#creating node-declaration & definition
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head  #temp=first node
            while temp:
                print(temp.data," ",end=" ")
                #temp.data means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
#node creation and initialization
n=node("w")   #so n.data in node class will be
obj.head=n  #assigning first node as head
n1=node("i")
obj.head.next=n1    #next node value
n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5
obj.display()

