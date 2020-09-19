s=input().split()
a = ['I' for i in range(int(s[0]))]
k=int(s[1])

for i in range(k):
    ball=input().split()
    l=int(ball[0])
    r=int(ball[1])
    for i1 in range(l-1,r):
        a[i1]='.'
print(''.join(a))