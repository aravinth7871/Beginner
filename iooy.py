m,u=map(int,input().split())
w=list(map(int,input().split()))[:m]
w.sort()
print(w[-u])
