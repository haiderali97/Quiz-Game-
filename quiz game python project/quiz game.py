print("Welcome to KBC")
name=str(input("Enter your name to start your game : "))
score=0

fi=open("q1.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='d' or op=='D'):
    score+=1

#Q2
fi=open("q2.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='a' or op=='A'):
    score+=1
#Q3
fi=open("q3.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='c' or op=='C'):
    score+=1
#Q4
fi=open("q4.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='d' or op=='D'):
    score+=1
#Q5
fi=open("q5.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='c' or op=='C'):
    score+=1
#Q6
fi=open("q6.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='c' or op=='C'):
    score+=1
#Q7
fi=open("q7.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='a' or op=='A'):
    score+=1    
    
#Q8
fi=open("q8.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='b' or op=='B'):
    score+=1
#Q9
fi=open("q9.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='c' or op=='C'):
    score+=1
#Q10
fi=open("q10.txt",'r')
print(fi.read())
op=str(input("enter correct option : "))
if(op=='c' or op=='C'):
    score+=1

print(name,'your score is : ',score)    
    
    
    
    
    
    
    
    
    
    
    
    
    
