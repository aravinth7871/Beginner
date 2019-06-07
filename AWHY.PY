V,N=map(str,input().split())
l1=0
if len(V)>len(N):
  V,N=N,V
i=0
while i<len(s):
  l1+=(ord(N[i])-ord(V[i]))
  i+=1
for i in range(i,len(N)):
  l1+=ord(N[i])-ord('a')+1
print(l1)
