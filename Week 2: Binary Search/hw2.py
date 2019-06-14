# Leetcode 33
'''
Runtime: 32 ms, faster than 95.21% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.2 MB, less than 67.58% of Python3 online submissions for Search in Rotated Sorted Array.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            
            mid = (start+end)//2
            
            if nums[mid]== target:
                return mid
            
            if nums[start] <= target < nums[mid] or (nums[start] > nums[mid] and (target >= nums[start] or target < nums[mid])):
                end = mid - 1
            else: # otherwise
    
                start = mid + 1
        return -1


# Leetcode 69
'''
Runtime: 32 ms, faster than 98.56% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.3 MB, less than 37.02% of Python3 online submissions for Sqrt(x).
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        start = 0
        end = x
        while start < end -1:
            mid = (start+end)//2
            if mid*mid > x:
                end = mid
            elif mid*mid < x:
                start = mid
            elif mid*mid == x:
                return mid
        return start
        
# Leetcode 74        
'''
Runtime: 32 ms, faster than 97.68% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.2 MB, less than 7.42% of Python3 online submissions for Search a 2D Matrix.
'''  
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m,n = len(matrix),len(matrix[0])
        start = 0
        end = m-1
        
        while start < end-1:
            mid = (start+end)//2

            if matrix[start][0] <= target <= matrix[mid][n-1]:
                end = mid
            elif matrix[mid][0] <= target <= matrix[end][n-1]:
                start = mid
            else:
                return False
            
        return target in matrix[start] or target in matrix[end]

# Leetcode 278
'''
Runtime: 24 ms, faster than 99.91% of Python3 online submissions for First Bad Version.
Memory Usage: 13 MB, less than 91.95% of Python3 online submissions for First Bad Version.
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end-1:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        else:
            return end
