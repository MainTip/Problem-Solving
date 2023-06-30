n=int(input())
x=input().split()
ar=[]
for i in range(n):
    for j in range(n):
        ar.append(x[i]+x[j])
ar=list(map(int,ar))
print(sum(ar))
