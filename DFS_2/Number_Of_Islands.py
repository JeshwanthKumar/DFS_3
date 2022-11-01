#Time_Complexity: O(mn)
#Space_Complexity: Recursive stack space - O(mn)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)  #m is the lenght of row
        self.n = len(grid[0])   #n is the length of column
        self.count = 0  #Initialize count as 0
        self.dirs_= [[0,1],[1,0],[0,-1],[-1,0]] #Initialize direction array
        
        for i in range(self.m): 
            for j in range(self.n):
                if grid[i][j] == "1":   #if grid[i][j] is equal to "1" 
                    self.dfs(i,j)   #Recursive function call dfs(i,j)
                    self.count += 1 #Increment the count by 1
        return self.count   #Return count
                    
    def dfs(self,i,j):  #Recursive function
        #base condition
        if self.grid[i][j] == "0":  #If the grid[i][j] is equal to 0
            return  #Return this unfolds the recursion
        
        self.grid[i][j] = "0"   #Set grid[i][j] as "0"
        for x, y in self.dirs_: #For x an y in direction array
            nr = x+i    #Add x and i to nr
            nc = y+j    #Add y and j to nc
            
            if nr >= 0 and nr < self.m and nc >= 0 and nc < self.n: #Boundary check
                self.dfs(nr,nc) #Recursive call by passing nr and nc
        