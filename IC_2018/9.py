from math import *
n=int(input())
x=floor(n/2)
if(n%2==0):
    x=x-1
print(x)
if(x%2):
    print("Win")
else:
    print("Lose")
