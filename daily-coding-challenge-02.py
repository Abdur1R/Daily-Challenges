l0=input().split()
l1=[]
l=len(l0)
for i in range(0,l):
    l0[i]=int(l0[i])
for i in l0:
    s=1
    for j in l0:
        if i!=j:
            s*=j
    l1.append(s)
print(l1)
    