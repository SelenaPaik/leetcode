class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0;
        if len(nums)==1: return nums[0];
        
        left =0;
        right=len(nums)-1
          
        while left<right:
            mid=(left+right)//2 
            if nums[right]<nums[mid]:
                left=mid +1
            else: 
                right = mid
            
        return nums[right]
                
            
        
        