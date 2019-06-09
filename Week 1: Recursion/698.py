'''
Runtime: 44 ms, faster than 92.55% of Python3 online submissions for Partition to K Equal Sum Subsets.
Memory Usage: 13.3 MB, less than 20.24% of Python3 online submissions for Partition to K Equal Sum Subsets.
'''


class Solution:
    
    def canPartitionKSubsets(self, nums, k):
        
            nums.sort(reverse=True) 
            buck, kSum = [0] * k, sum(nums) // k
            
            def DFS(idx):
                
                if idx == len(nums): 
                    return len(set(buck)) == 1
                
                for i in range(k):
                    buck[i] += nums[idx]
                    
                    if buck[i] <= kSum and DFS(idx + 1): 
                        return True
                    
                    buck[i] -= nums[idx]
                    
                    if buck[i] == 0: 
                        break 
                return False
            
            return DFS(0)