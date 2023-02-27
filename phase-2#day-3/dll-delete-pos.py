class Node:                   #create a list
    def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None

class dll:
    def __init__(self):
        self.head=None
        
    def delete_pos(self,pos):   #delete at the pos  
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
    def display(self):         
        if self.head is None:
            print("empty")
        else:
          temp=self.head
          while temp:
             print(temp.data,"<-->",end=" ")
             temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2

l.delete_pos(1)
l.display() 
