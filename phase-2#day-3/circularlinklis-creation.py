class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class createlist:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
#adding node at end of ll
    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            #it is cll so,tail will point to head
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("list is empty")
            return
        else:
            print("nodes of the circular linked list:")
            print(current.data,"-->")
            while(current.next!=self.head):
                current=current.next
                print(current.data,"-->")
class circularlinkedlist:
    c1=createlist()
    c1.add("c")
    c1.add("o")
    c1.add("d")
    c1.add("e")
    c1.add("s")
    c1.display()
