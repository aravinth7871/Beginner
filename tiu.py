h = int(input())
k = list(map(int,input().split()))
k.sort(reverse = True)
k = [str(x) for x in k]
print("".join(k))
