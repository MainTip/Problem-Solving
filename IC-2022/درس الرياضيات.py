h=10**9+7
for _ in range(int(input())):
    x=int(input())
    x=x*(x+1)*(x+x+1)//6
    print(x%h)
