# Leetcode 190. Reverse Bits
'''
Runtime: 16 ms, faster than 85.70% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 22.52% of Python online submissions for Reverse Bits.
'''
def reverseBits(self, n):
    ans = 0
    for i in xrange(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans


# Leetcode 338. Counting Bits
'''
Runtime: 68 ms, faster than 78.28% of Python online submissions for Counting Bits.
Memory Usage: 15.8 MB, less than 47.47% of Python online submissions for Counting Bits.
'''


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num+1):
            result.append(result[i>>1] + int(i&1))
        return result
    
    
# Leetcode 693. Binary Number with Alternating Bits
'''
Runtime: 16 ms, faster than 76.66% of Python online submissions for Binary Number with Alternating Bits.
Memory Usage: 11.8 MB, less than 30.38% of Python online submissions for Binary Number with Alternating Bits.
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)
        
        if '00' in s or '11' in s:
            return False
        else:
            return True
        
# Leetcode 401. Binary Watch
'''
Runtime: 20 ms, faster than 69.85% of Python online submissions for Binary Watch.
Memory Usage: 11.8 MB, less than 51.39% of Python online submissions for Binary Watch.
'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+ bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans        
