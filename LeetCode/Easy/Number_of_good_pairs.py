import math
class Solution(object):
    def numIdenticalPairs(self, nums):
        dict = {}
        count = 0
        r = 2
        for i in nums:
            if i in dict:
                dict[i] = dict[i] + 1
            else :
                dict[i] = 1
        for i in dict:
            n = dict[i]
            if(n >= 2):
                count+=  n*(n-1)/2
            
        return count
            