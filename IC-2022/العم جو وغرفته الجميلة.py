from math import *
def area(a,b,c):
    s=(a+b+c)/2
    i=s*(s-a)*(s-b)*(s-c)
    return sqrt(i)
a,b,c,d=list(map(int,input().split()))
x=area(a,b,c)*d
print(f'{x:.3f}')
