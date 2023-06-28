s=input()
if(s[0:11]=='http://www.'and len(s.split('.'))==3):
    print('http')
    print('www')
    print(s.split('.')[1])
    print(s.split('.')[2])
else:
    print('invalid')
