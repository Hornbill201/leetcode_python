# Leetcode Problem 389 Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        
        return (dict_t - dict_s).keys().pop()
