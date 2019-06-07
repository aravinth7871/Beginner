d,h=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(h):
    v,d=map(int,input().split())
    t=functools.reduce(math.gcd,l[v-1:d])
    print(t)
