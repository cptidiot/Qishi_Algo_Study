# 4. Median of Two Sorted Arrays
'''
Runtime: 56 ms, faster than 82.80% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.4 MB, less than 28.85% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            return (
                self.find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2)) +
                self.find_kth((total_len // 2) - 1, nums1, 0, len(nums1), nums2, 0, len(nums2))
            ) / 2
        return self.find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2))

    def find_kth(self,k, nums1, start1, end1, nums2, start2, end2):
        if end1 <= start1:
            return nums2[start2 + k]
        if end2 <= start2:
            return nums1[start1 + k]

        mid1 = start1 + (end1 - start1) // 2
        mid2 = start2 + (end2 - start2) // 2
        if k > (mid1 - start1) + (mid2 - start2):
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth(k - (mid2 - start2) - 1, nums1, start1, end1, nums2, mid2 + 1, end2)
            else:
                return self.find_kth(k - (mid1 - start1) - 1, nums1, mid1 + 1, end1, nums2, start2, end2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth(k, nums1, start1, mid1, nums2, start2, end2)
            else:
                return self.find_kth(k, nums1, start1, end1, nums2, start2, mid2)

# 53. Maximum Subarray
'''
Runtime: 36 ms, faster than 97.24% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.8 MB, less than 33.63% of Python3 online submissions for Maximum Subarray.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    
    
    
# 215. Kth Largest Element in an Array
'''
Runtime: 36 ms, faster than 94.54% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.9 MB, less than 21.13% of Python3 online submissions for Kth Largest Element in an Array.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k-1] 
    
    
    
    
# 973. K Closest Points to Origin

'''
Runtime: 340 ms, faster than 93.96% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 16.9 MB, less than 91.93% of Python3 online submissions for K Closest Points to Origin.
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
