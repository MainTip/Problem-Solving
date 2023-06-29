#update: There is an efficent and shorter code but this code is for learning , in advanced Solutions You'll See Like This Probelm Inserting
Modulo and Floor for such a thing for a better algorithm 
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))
er=0
c1=[a[0],b[0],c[0],d[0],e[0]]
c2=[a[1],b[1],c[1],d[1],e[1]]
c3=[a[2],b[2],c[2],d[2],e[2]]
c4=[a[3],b[3],c[3],d[3],e[3]]
c5=[a[4],b[4],c[4],d[4],e[4]]
if(len(set(a))==len(set(b))==len(set(c))==len(set(d))==len(set(e))==5):
    if(len(set(c1))==len(set(c2))==len(set(c3))==len(set(c4))==len(set(c5))==5):
        #we're good :)
        er=0
    else:
        er=1
if( not min(f)>=1 and not max(f)<=9):
    er=1
if(er==1):
    print("not sudoku")
else:
    print("sudoku")
