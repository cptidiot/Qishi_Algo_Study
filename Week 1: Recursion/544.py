'''
Total runtime 101 ms
'''

class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """
    def findContestMatch(self, n):
        res = [str(i+1) for i in range(n)]
        return self.helper(res)
        
    def helper(self,res):
        if len(res) == 1:
            return res[0]
            
        tmp = []
        i = 0
        j = len(res) - 1 
        while i < j:
            tmp.append('(' + res[i] + ',' + res[j] +')')
            i += 1 
            j -= 1 
        return self.helper(tmp)
        

   