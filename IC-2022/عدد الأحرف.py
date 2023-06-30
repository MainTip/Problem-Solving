s=input()
l=len(s)
x=0
for i in range(l):
    for j in range(l):
        x=x+len(set(list(s[i:j+1])))
print(x)
