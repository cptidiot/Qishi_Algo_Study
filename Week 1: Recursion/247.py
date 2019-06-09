
'''
Total runtime 856 ms
'''
class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        oddNumber = ['0','1','8']
        evenNumber = ['11','69','88','96','00']
        
        # base case 
        if n == 0:
            return ['']
        if n == 1:
            return oddNumber
        if n == 2:
            return evenNumber[:-1]
            
        #general case
        
        if n % 2:
            pre, mid = self.findStrobogrammatic(n-1), oddNumber
        else:
            pre, mid = self.findStrobogrammatic(n-2), evenNumber
            
        cut = (n-1) / 2 
        
        
        return [i[:cut]+j+i[cut:] for j in mid for i in pre]