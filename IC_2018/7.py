def s(x):
  return x*(x+1)//2
a,b=int(input()),int(input()) 
print(max(s(a),s(b))-min(s(a),s(b))+min(a,b))
