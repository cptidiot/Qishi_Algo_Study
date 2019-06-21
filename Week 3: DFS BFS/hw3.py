# Leetcode 200 Number of Islands:
'''
Runtime: 76 ms, faster than 80.74% of Python3 online submissions for Number of Islands.
Memory Usage: 13.8 MB, less than 83.40% of Python3 online submissions for Number of Islands.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 'searched'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

# Leetcode 513 Find Bottom Left Tree Value:
'''
Runtime: 48 ms, faster than 92.75% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 15.7 MB, less than 54.48% of Python3 online submissions for Find Bottom Left Tree Value.
'''
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        queue = [root]
        
        while queue:
            result = queue[0].val
            size = len(queue)
            while size:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
        return result
    
    
    

# Leetcode 542 01 Matrix:
'''
Runtime: 560 ms, faster than 54.67% of Python3 online submissions for 01 Matrix.
Memory Usage: 16.2 MB, less than 35.67% of Python3 online submissions for 01 Matrix.
'''
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        def bfs(queue):
            while queue:
                (r, c) = queue.popleft()
                for (d_r, d_c) in [(1,0), (-1,0), (0,1), (0,-1)]:
                    n_r, n_c = r+d_r, c+d_c
                    if 0 <= n_r < row_len and 0 <= n_c < col_len and res[r][c]+1 < res[n_r][n_c]:
                        res[n_r][n_c] = res[r][c]+1
                        queue.append((n_r, n_c))
                      
                    
        row_len, col_len = len(matrix), len(matrix[0])
        res = [[float('inf') for _ in range(col_len)] for _ in range(row_len)]
        queue = collections.deque()
        
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r,c))
        bfs(queue)
        return res
        

# Leetcode 934 Shortest Bridge:
'''
Runtime: 184 ms, faster than 63.81% of Python3 online submissions for Shortest Bridge.
Memory Usage: 17 MB, less than 19.02% of Python3 online submissions for Shortest Bridge.
'''
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        row_len, col_len = len(A), len(A[0])
        direction = ((1,0),(0,1),(-1,0),(0,-1))
        tmp = [[0 for _ in range(col_len)] for _ in range(row_len)]
        queue = collections.deque()
        
        def dfs(x,y):
            
            tmp[x][y] = 1
            queue.append((0,x,y))
            
            for i in direction:
                nx = x + i[0]
                ny = y + i[1]
                
                if 0 <= nx < row_len and 0 <= ny < col_len and A[nx][ny] == 1 and tmp[nx][ny] == 0:
                    tmp[nx][ny] = 1
                    dfs(nx, ny)
        
        flag = 0
        
        for i in range(row_len):
            for j in range(col_len):
                if A[i][j] == 1:
                    dfs(i,j)
                    flag = 1
                    break
        
            if flag:
                break

        while queue:
            t,x,y = queue.popleft()
            
            for i in direction:
                nx = x + i[0]
                ny = y + i[1]
                
                if 0 <= nx < row_len and 0 <= ny < col_len and tmp[nx][ny] == 0:
                    if A[nx][ny] == 0:
                        queue.append((t + 1, nx, ny))
                        tmp[nx][ny] = 1
                    else:
                        return t
