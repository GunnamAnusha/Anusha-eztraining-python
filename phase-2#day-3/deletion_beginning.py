#while creating linked list we gonna do it in ascending order
#one prg multiple concepts
class Node:
    def __init__(self,data):    #create linked list
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        if not temp:
            print("list is empty")
            return
        else:
            print("start:",end=" ")
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("end")
    def insert(self,data):    #inserts data
        new_node=Node(data)
        #if the linked list is empty
        if self.head is None:
            self.head=new_node
        #if the data is smaller than the head
        elif self.head.data>=new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            #locate the node before insertion point
            current=self.head
            while current.next and new_node.data>current.next.data:
                current=current.next
            #insertion
            new_node.next=current.next
            current.next=new_node
    def delete(self,key):
        #if the list is empty
        if self.head is None:
            print("declartion error:the list is empty")
            return
        #if the key is in head
        if self.head.data==key:
            self.head=self.head.next
            return
        #find position of first occurrence of the
        current=self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
        #if the key was not found
        if current is None:
            print("deletion error:key not found")
        else:
            previous.next=current.next
#__name is python special variable
if __name__=="__main__": #starting point of program
    
    #create an object
    ll=linkedlist()
    print(" ")
    #insert some nodes
    ll.insert(10)
    ll.insert(12)
    ll.insert(8)
    ll.insert(11)
    ll.insert(10)

    ll.printlist()
    ll.delete(12)
    ll.delete(8)
    ll.delete(10)
    ll.printlist()
        
