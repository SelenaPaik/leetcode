class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval=1
        minval=1
        res = max(nums)
        for num in nums:
            if num==0:
                maxval=1
                minval=1
                continue
            
            tmp = maxval*num   
            maxval = max(num, num*maxval, num*minval)
            minval = min(num, tmp, num*minval)
            res = max(res, maxval)
            print(res)
                
        return res
