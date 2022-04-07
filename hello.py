l=input().split()
k=int(input())
x=0
for I in l:
    i=int(I)
    for J in l:
        j=int(J)
        if (i!=j) and ((i+j)==k):
            print("true")
            x=1
            break
    if x==1:
        break        
