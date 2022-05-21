def firstmissingpositive(arr, n):
    arr = sorted(arr)
    # missing least positive value
    res = 0
    # removing negative and duplicate values
    arr = {ele for ele in arr if ele > 0}
    arr = list(arr)
    for i in range(len(arr)):
        # if element not equal to i+1 value updating result with the i+1 and break
        if arr[i] != i+1:
            res = i+1
            break
    if res == 0:
        return len(arr)+1
    else:
        return res


A = [0, 10, 1, 2, -10, -20]

N = len(A)

print(firstmissingpositive(A, N))