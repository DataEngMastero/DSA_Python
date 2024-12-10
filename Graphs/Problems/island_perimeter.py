# Leetcode Problem #463

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set() # Keep track of cells visited

        def dfs(i, j):
            # Out of bounds 
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
                return 1

            # Water Side
            if grid[i][j] == 0:
                return 1

            # If cell is already visited
            if (i, j) in visited:
                return 0

            # Mark the land visited and traverse in all four directions
            visited.add((i, j))
            perimeter = dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            
            return perimeter


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        