def rod_cutting(lengths, prices, w, n): 
    # Base Case => Intialisation
    for row in range(n + 1):
        for col in range(w + 1):
            if row == 0 or col == 0:
                td[row][col] = 0

    # Choice Diagram => Iterative Solution
    for row in range(1, n + 1):
        for col in range(1, w + 1):
            if(lengths[row - 1] <= col):
                td[row][col] = max(prices[row-1] + td[row][col - lengths[row-1]], td[row-1][col])
            else:   
                td[row][col] = td[row-1][col]
    return td[n][w]


lengths = [1, 2, 3, 4]
prices = [1, 4, 5, 7]
N = 4
n = len(lengths)

td = []
for row in range(n + 1):
    td.append([-1] * (N + 1))

print("Top-Down Approach Solution :")
print(rod_cutting(lengths, prices, N, n))
