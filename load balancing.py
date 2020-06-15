n=int(input())
a=list(map(int,input().split()))
sec=0
a.sort()
dif=a[n-1]-a[0]
while True:
	a[0]+=1
	a[n-1]-=1
	a.sort()
	if dif==(a[n-1]-a[0]) or a[n-1]-a[0]==0:
		break
	sec+=1
	dif=a[n-1]-a[0]
	
	
print(sec)	
