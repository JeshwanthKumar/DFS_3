#Time_Complexity: O(mn)
#Space_Complexity: Recursive stack space - O(mn)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)  #m is the length of row
        n = len(image[0])   #n is the lenght of column
        dirs_ = [[0,1],[1,0],[-1,0],[0,-1]] #Initialize direction array
        colorTBC = image[sr][sc]    #Initialized colorTBC as a copy of the initial color to be changed
        if colorTBC == color:   #If the colorTBC is equal to color return image
            return image
        q = deque() #Initialize q using deque
        q.append((sr,sc))   #Append sr and sc tro the q
       
        
        
        
        while q :   #Continue till the q is empty
            size = len(q)   #Size is the length of q
            for _ in range(size):
                curr = q.popleft() #Pop the first element in the q
                image[curr[0]][curr[1]] = color #Initialize color to image[curr[0]][curr[1]]
                for x,y in dirs_:   #For x an y in direction array
                    nr = x+curr[0]  #Add x+curr[0] to nr
                    nc = y+curr[1]  #Add y and curr[1] to nc
                    # print(nr,nc)
                    if nr >=0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == colorTBC:  #Boundary check and if image[nr][nc] is equal to color
                        image[nr][nc] = color   #Change image[nr][nc] as color
                        q.append((nr,nc))   #Append sr and sc to the q
                        # print(q)
                        
        return image    #Return the image
            
        