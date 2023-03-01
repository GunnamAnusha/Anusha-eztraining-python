s=input() #takes the parenthesis as input
st=[ ] #stores in the stack
balanced=True  #consider it is balanced
for char in s:
    if (char=="{" or char=="[" or char=="("):
        st.append(char)
    elif(char=="}"):
        if (len(st) and st.pop()!="{"):
            balanced=False
            break
    elif (char=="]"):
        if(len(st) and st.pop()!="["):
            balanced=False
            break
    elif(char==")"):
        if(len(st) and st.pop()!="("):
            balanced=False
            break
    else:
        balanced==False
        break
if(balanced==False or len(st)):
    print("not balanced")
else:
    print("balanced")
