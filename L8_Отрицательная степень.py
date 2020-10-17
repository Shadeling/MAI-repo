def power(a,n):
        b=1
        for i in range(abs(int(n))):
            b*=float(a)
            
        if int(n)>0:
            return b
        else:
            return 1/b
            
            
a=input()
n=input()
print(power(a,n))