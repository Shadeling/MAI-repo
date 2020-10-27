N=int(input())
d=dict()
for i in range(N):
    name, s =input().split()
    if name not in d:
        d[name]=int(s)
    else:
        d[name]+=int(s)

for key,val in sorted(d.items()):
    print(key, val)