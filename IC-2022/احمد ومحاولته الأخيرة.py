def sim(a,b):
    a=str(a)
    b=str(b)
    ar=[]
    for i in range(len(a)):
        if(a[i]==b[i]):
            ar.append(i)
    return ar
s=input()
h=10**9+7
p=[]
x=0
for i in range(len(s)):
    if(s[i]!="*"):
        p.append(int(i))
for i in range(0,int(s.replace('*','9'))+1):
    if(sim(str(i),str(s))==p and i%17==6):
        x=x+1
    elif(len(str(i)) != len(str(s))):
         z=len(str(s))-len(str(i))
         if(sim('0'*z+str(i),str(s))==p and i%17==6):
             x=x+1
print(x%h)
