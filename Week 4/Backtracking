# Leetcode 90
'''
Runtime: 48 ms, faster than 71.97% of Python3 online submissions for Subsets II.
Memory Usage: 13.2 MB, less than 56.61% of Python3 online submissions for Subsets II.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()         
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, combination, results):
        
        results.append(list(combination))    
        for i in range(index, len(nums)):  
            if i > index and nums[i] == nums[i - 1]: 
                continue               
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, results)
            combination.pop()

# Leetcode 40
'''
Runtime: 48 ms, faster than 92.78% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.2 MB, less than 68.56% of Python3 online submissions for Combination Sum II.
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      
        candidates.sort()  
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
    
    def dfs(self, candidates, target, start, combination, results):
        
        if target == 0:
            return results.append(list(combination))
        
        for i in range(start, len(candidates)): 
            
            if i > start and candidates[i] == candidates[i - 1]: 
                continue 
            if target < candidates[i]:   
                return
            
            combination.append(candidates[i])
            
            self.dfs(candidates, target - candidates[i], i + 1, combination, results)   
            
            combination.pop()  
            
# Leetcode 47:
'''
Runtime: 72 ms, faster than 80.78% of Python3 online submissions for Permutations II.
Memory Usage: 13.1 MB, less than 94.85% of Python3 online submissions for Permutations II.
'''            
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        results = []
        visited = [False] * len(nums) 
        nums.sort()  
        self.dfs(nums, [], results, visited)  
        return results 

    def dfs(self, nums, subset, results, visited):
        
        if len(nums) == len(subset):
            results.append(list(subset))
        
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue  

            visited[i] = True
            subset.append(nums[i]) 
            self.dfs(nums, subset, results, visited) 
            subset.pop()  
            visited[i] = False 
            
# Leetcode 216:
'''
Runtime: 36 ms, faster than 83.79% of Python3 online submissions for Combination Sum III.
Memory Usage: 13.2 MB, less than 49.24% of Python3 online submissions for Combination Sum III.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if n > sum([i for i in range(1, 11)]):
            return []

        results = []
        self.dfs(k, n, 1, [], results)
        return results


    def dfs(self, k, n, curr, combi, results):
        if len(combi) == k:
            if sum(combi) == n:
                results.append(list(combi))
            return

        if len(combi) > k or curr > 9:
            return
        
        for i in range(curr, 10):
            combi.append(i)
            self.dfs(k, n, i + 1, combi, results)
            combi.pop()

# Leetcode 77:
'''
Runtime: 120 ms, faster than 95.61% of Python3 online submissions for Combinations.
Memory Usage: 15 MB, less than 64.46% of Python3 online submissions for Combinations.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
   
        results=[]
        self.helper(n,1,k,results,[])
        return results
    
    def helper(self,n,start,k,results,combi):
        if k==0:
            results.append(combi[::])
            return
        for i in range(start,n-k+2):
            combi.append(i)
            self.helper(n,i+1,k-1,results,combi)
            combi.pop()

