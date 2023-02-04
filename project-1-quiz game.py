q1="""who is the first law ministerof independent INDIA?
a.Nehru
b.pallavi desai
c.B.R.Ambedkar
d.APJ.Abdul Kalam"""

q2="""who is known as missile woman of Indai?
a.Tessy Thomas
b.pali
c.Ranjani Rao
d.Janaki Ammal"""

q3="""in which country is the global seed vault located?
a.norway
b.japan
c.America
d.Korea"""

q4="""which are easily available sources of vitamin B12?
a.sunlight
b.milk
c.sprouts
d.rice"""

q5="""which element is a diamond made of?
a.nickel
b.platinum
c.carbon
d.phosphorus"""

questions={q1:"c",q2:"a",q3:"a",q4:"b",q5:"c"}
name=input("Hi whats ur name")
print("Hello",name,"welcome to the quiz")
score=0
for i in questions:
                                               
    print(i)
    flag1=input("Do you want to skip these questions(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is:",score)
    flag2=input("do you want to skip?type(yes/no)")
    if flag2=="yes":
        break
    print("your total score is:",score)
