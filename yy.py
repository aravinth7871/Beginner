v=int(input())
k=list(map(int,input().split()))
g=0
for f in range(0,v):
    for u in range(0,f):
        if k[u]<k[f]:
            g=g+k[u]
print(g) 
