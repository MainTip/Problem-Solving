a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=a+b+c
if(min(d)<1 or max(d) > 100):
    print("Numbers should be between 1 and 100")
else:
    print("The max of the elements of column 1 = "+str(max(a[0],b[0],c[0])))
    print("The max of the elements of column 2 = "+str(max(a[1],b[1],c[1])))
    print("The max of the elements of column 3 = "+str(max(a[2],b[2],c[2])))
