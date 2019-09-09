from itertools import combinations
count = 0
wt = int(input("enter weight:"))
for i in range (1,250):
	a = combinations([1,5,7,9,11],i)
	for j in list(a):
		if int(sum(j))==int(wt):
			count=i
print(count)
