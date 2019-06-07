g=int(input())
v=input().split()
n=[]
r=''
for j in v:
    if v.count(j)>1 and j not in n:
        n.append(j)
if len(n)>0:
    for j in range(len(n)-1):
        r+=n[j]+" "
    print(r+n[-1])
else:
    print("unique")
