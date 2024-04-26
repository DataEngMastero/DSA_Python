
def knapsack_recursion(wt_arr, value_arr, weight, n):
    # Base Condition is either weight is zero or no items are remaining to add in knapsack
    if n == 0 or weight == 0:
        return 0

    # Code Choice Diagram Code
    if(wt_arr[n -1] <= weight):
        return max(
            value_arr[n-1] + knapsack_recursion(wt_arr, value_arr, weight-wt_arr[n-1], n-1),
            knapsack_recursion(wt_arr, value_arr, weight, n-1)
        )
    else:
        return knapsack_recursion(wt_arr, value_arr, weight, n-1)
    

def knapsack_memoization(wt_arr, value_arr, w, n):
    if n == 0 or w == 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    
    if(wt_arr[n -1] <= weight):
        dp[n][w] = max(
            value_arr[n-1] + knapsack_recursion(wt_arr, value_arr, weight-wt_arr[n-1], n-1),
            knapsack_recursion(wt_arr, value_arr, weight, n-1)
        )
    else:
        dp[n][w] = knapsack_recursion(wt_arr, value_arr, weight, n-1)
    return dp[n][w]


def knapsack_top_down(wt_arr, value_arr, w, n): 
    # Base Case => Intialisation
    for row in range(n + 1):
        for col in range(w + 1):
            if row == 0 or col == 0:
                td[row][col] = 0

    # Choice Diagram => Iterative Solution
    for row in range(1, n + 1):
        for col in range(1, w + 1):
            if(wt_arr[row - 1] <= col):
                td[row][col] = max(value_arr[row-1] + td[row-1][col - wt_arr[row-1]], td[row-1][col])
            else:   
                td[row][col] = td[row-1][col]
    return td[n][w]


wt_arr = [1, 3, 4, 5]
value_arr = [1, 4, 5, 7]
weight = 10
n = len(wt_arr)

print("Recursion Solution : ")
print(knapsack_recursion(wt_arr, value_arr, weight, len(wt_arr)))

dp = []
for row in range(n + 1):
    dp.append([-1] * (weight + 1))
print("Memoization Solution : ")
print(knapsack_memoization(wt_arr, value_arr, weight, len(wt_arr)))

def print_td(td):
    for row in range(len(td)):
        print(td[row])

td = []
for row in range(n + 1):
    td.append([-1] * (weight + 1))

print("Top-Down Approach Solution :")
print(knapsack_top_down(wt_arr, value_arr, weight, len(wt_arr)))