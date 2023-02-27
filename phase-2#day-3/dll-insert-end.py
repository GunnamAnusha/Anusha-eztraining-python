class Node:                   #create a list
    def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None

class dll:
    def __init__(self):
        self.head=None
        
    def insert_end(self):   #insert at the end  
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
        
    def display(self):         
        if self.head is None:
            print("empty")
        else:
          temp=self.head
          while temp:
             print(temp.data,"<-->",end=" ")
             temp=temp.next

l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display() 
