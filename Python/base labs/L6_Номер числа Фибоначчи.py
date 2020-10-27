a=int(input())
i1=0 
i2=1
n=0

while(a>i1):
    t=i2
    i2=i1+i2
    i1=t
    n=n+1
if(a==i1):
    print(n)
else:
    print(-1)