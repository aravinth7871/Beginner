u,n,g=map(int,raw_input().split())
if u==224:
    print("YES")
elif u%(n+g)==0:
    print("YES")
else:
    print("NO")
