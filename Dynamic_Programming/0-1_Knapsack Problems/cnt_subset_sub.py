def cnt_subsets(arr, sum, n):
    # Base Condition > Initaisation
    for row in range(n + 1):
        for col in range(sum + 1):
            if col == 0:
                td[row][col] = 1
            if row == 0 and col != 0:
                td[row][col] = 0

    # Choice Diagram Iterative
    for row in range(1, n + 1):
        for col in range(1, sum + 1):
            if arr[row-1] <= col:
                td[row][col] = td[row - 1][col - arr[row - 1]] + td[row - 1][col]
            else:
                td[row][col] = td[row - 1][col]
    return td[n][sum]

arr = [2, 3, 5, 6, 8, 10]
sum = 10
n = len(arr)

td = []
for i in range(n + 1):
    td.append([-1] * (sum + 1))

print(cnt_subsets(arr, sum, n))