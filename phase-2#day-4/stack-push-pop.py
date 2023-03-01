#implementation of stack-LIFO
stack=[ ]
def push():
    element=int(input("enter the element:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
while True:
    print("select the operations which you want to do 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("please select only the shown numbers")
        
