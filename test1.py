class Solution:
    def getTotalIsles(self, grid):
        if not grid or not grid[0]:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "W":
                return
            # Mark the current land as visited by turning it into water
            grid[i][j] = "W"
            # Explore the neighboring lands in all 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        total_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "L":  # Start a DFS for every unvisited land
                    total_islands += 1
                    dfs(i, j)  # Perform DFS to mark all connected land as visited
        
        return total_islands
