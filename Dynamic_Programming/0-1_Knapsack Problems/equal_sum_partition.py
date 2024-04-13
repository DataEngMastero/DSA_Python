def equal_partition_sum(arr, sum, n):
    if sum % 2 != 0:
        return False
    else:
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
        
        
        print("Top-Down Approach Solution :")
        return subset_top_down(arr, sum, n)

arr = [1, 5, 11, 5]
n = len(arr)
sum = sum(arr)

print(equal_partition_sum(arr, sum, n))
