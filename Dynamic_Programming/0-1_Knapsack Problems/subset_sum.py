
def subset_sum_recursion(arr, sum, n):
    # Base Case
    if sum == 0:
        return True
    if sum != 0 and n == 0:
        return False


    # Choice Diagram
    if arr[n - 1] <= sum:
        return subset_sum_recursion(arr, sum - arr[n-1], n - 1) or subset_sum_recursion(arr, sum, n - 1)
    else:
        return subset_sum_recursion(arr, sum, n - 1) 


def subset_set_memoization(arr, sum, n):
    # Base Case 
    if sum == 0:
        return True
    if sum != 0 and n == 0:
        return False

    if dp[n][sum] != -1:
        return dp[n][sum]

    # Choice Diagram
    if arr[n - 1] <= sum:
        dp[n][sum] = (subset_set_memoization(arr, sum - arr[n-1], n - 1) or subset_set_memoization(arr, sum, n - 1))
    else:
        dp[n][sum] = subset_set_memoization(arr, sum, n - 1)

    return dp[n][sum]


def subset_top_down(arr, sum, n):
    # Base Condition > Initaisation
    for row in range(n + 1):
        for col in range(sum + 1):
            if col == 0:
                td[row][col] = True 
            if row == 0 and col != 0:
                td[row][col] = False

    # Choice Diagram Iterative
    for row in range(1, n + 1):
        for col in range(1, sum + 1):
            if arr[row-1] <= col:
                td[row][col] = td[row - 1][col - arr[row - 1]] or td[row - 1][col]
            else:
                td[row][col] = td[row - 1][col]
    return td[n][sum]

arr = [2, 3, 4, 8, 10]
sum = 11 
n = len(arr)
print("Recursion Solution : ")
print(subset_sum_recursion(arr, sum, n))

dp = []
for row in range(n + 1):
    dp.append([-1] * (sum + 1))
print("Memoization Solution : ")
print(subset_set_memoization(arr, sum, n))

td = []
for row in range(n + 1):
    td.append([-1] * (sum + 1))
print("Top-Down Approach Solution :")
print(subset_top_down(arr, sum, n))