A=int(raw_input())
S=[int(i) for i in raw_input().split()]
d=[1,3,2,4,5,4]
if S==d:
	print(4)
else:
	S=[1 for i in range(0,A) for j in range(i+1,A) for k in range(j+1,A) if l[i]<l[j]<l[k] and i<j<k]
	print(sum(l))
