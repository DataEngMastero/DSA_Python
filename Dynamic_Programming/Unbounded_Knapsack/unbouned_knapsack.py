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
                td[row][col] = max(value_arr[row-1] + td[row][col - wt_arr[row-1]], td[row-1][col])
            else:   
                td[row][col] = td[row-1][col]
    return td[n][w]


wt_arr = [1, 3, 4, 5]
value_arr = [1, 4, 5, 7]
weight = 10
n = len(wt_arr)

td = []
for row in range(n + 1):
    td.append([-1] * (weight + 1))

print("Top-Down Approach Solution :")
print(knapsack_top_down(wt_arr, value_arr, weight, len(wt_arr)))
