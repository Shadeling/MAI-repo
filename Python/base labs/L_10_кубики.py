N,M=input().split()
N=int(N)
M=int(M)

ann, bor=set(), set()
for i in range(N):
    ann.add(int(input()))
for i in range(M):
    bor.add(int(input()))


f1=sorted(ann.intersection(bor))
f2=sorted(ann-bor)
f3=sorted(bor-ann)
print(len(f1))
print(*f1, sep =' ')
print(len(f2))
print(*f2, sep =' ')
print(len(f3))
print(*f3, sep =' ')
