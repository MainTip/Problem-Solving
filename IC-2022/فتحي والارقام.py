n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,n):
    if(sum(x[0:i])>=sum(x[i:n])):
        c+=1
print(c)
