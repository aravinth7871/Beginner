from itertools import combinations
a,b=map(int,input().split())
z=len(str(a))
k=list(combinations(str(a),z-b))
k=(sorted(k))
g="".join(k[0])
print(g)
