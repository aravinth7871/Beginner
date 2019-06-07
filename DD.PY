v=int(input())
n=1000
for i in range(0,20):
    if pow(2,i)<=v:
        s = abs(pow(2, i) - v)
        if s < n: n = s
print(n)
