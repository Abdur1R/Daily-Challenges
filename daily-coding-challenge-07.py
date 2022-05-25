# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

def result(a,n):
    count = [0]*(n+1)
    count[0] = 1
    count[1] = 1
    if a[0] == 0 :
        print(0)
        return 
    for i in range(2,n+1):
        # print (i,a[i-1])
        if a[i-1]>0:
            count[i] = count[i-1]
        if a[i-1] == 0 and (a[i-2]>2 or a[i-2] == 0) :
            print(0)
            return
        if a[i-2]==1 or a[i-2]==2 and a[i-1]<7:
            count[i] += count[i-2]
    # print(count)
    print(count[n])
 

s = ‘111’
a = [int(i) for i in list(s)]
n = len(a)
result(a,n)