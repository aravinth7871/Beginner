s,v=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
for i in range(v):
	h,g=map(int,raw_input().split())
	d=l[u-1:g]
	print(sum(d))
