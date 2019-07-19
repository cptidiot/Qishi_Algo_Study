class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        graph = [ [] for _ in range(numCourses) ]
        ans = []
        
        for y,x in prerequisites:
            indegree[y] += 1
            graph[x] += y,
            
        q = collections.deque([i for i in range(numCourses) if indegree[i]==0])
        
        while q:
            x = q.pop()
            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y]==0:
                    q.append(y)
            ans += x,
            
        if len(ans)==numCourses:
            return ans
        else:
            return []


