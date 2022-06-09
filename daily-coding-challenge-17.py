# A builder is looking to build a row of n houses that can be of k different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color. 
# Given an n by k matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

def minimizeColorCost(given_array):
    results = []
    helper(given_array, results, 0, -1, 0, "")
    return min(results)
    
def helper(given_array, results, curr_house, prev_color, curr_cost, curr_sequence):
    if curr_house == len(given_array):
        results.append((curr_cost, curr_sequence))
        return
    for i in range(0, len(given_array[0])):
        if i != prev_color:
            helper(given_array, results, curr_house + 1, i, given_array[curr_house][i] + curr_cost, curr_sequence + str(i))
    
arr = [[1,2,3,4], [1,2,1,0], [6,1,1,5], [2,3,5,5]]
print(minimizeColorCost(arr))
