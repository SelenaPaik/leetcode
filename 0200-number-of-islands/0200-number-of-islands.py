class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]    
        
        res=0
        def dfs(i,j,grid,res):
                grid[i][j]="2"
                for (x,y) in dirs:
                    new_i, new_j = i+x, j+y
                    if 0<= new_i <len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]=="1":
                        dfs(new_i, new_j, grid,res)
     
        num=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j,grid,res)
                    num+=1
                
        return num
    