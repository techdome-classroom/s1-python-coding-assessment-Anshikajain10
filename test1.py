class Solution:
    def getTotalIsles(self, grid):
        if not grid or not grid[0]:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "W":
                return
            
            grid[i][j] = "W"
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        total_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "L":  
                    total_islands += 1
                    dfs(i, j)  
        
        return total_islands
