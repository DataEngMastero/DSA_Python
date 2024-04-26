


def minimum_subset_sum(arr, sum, n):
    td = []
    for row in range(n + 1):
        td.append([-1] * (sum + 1))
    
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
    
    subset_top_down(arr, sum, n)

    # Only require final array
    result = td[n]

    valid_subset_sums = []
    for num in range(len(result)//2):
        if result[num]:
            valid_subset_sums.append(num)

    # Minimum Subset Difference
    min_diff = sum 
    for num in valid_subset_sums:
        min_diff = min(min_diff, sum - (2 * num))

    return min_diff

    


arr = [1, 6, 11, 5]
n = len(arr)
sum = sum(arr)


print(minimum_subset_sum(arr, sum, n))
