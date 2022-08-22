class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N=len(nums)
        l,r = 0,N-1
        
        if N==1:
            if target==nums[0]: return 0
            else: return -1
            
        # find pivot value
        while l<r:
            mid = (l+r) //2  
            if nums[mid]> nums[r]:
                l = mid+1
            else:
                r = mid
            
        pivot = r 
        
        # find target with binary search
        l,r = 0,N-1
        if pivot!=0:
            if nums[l] < target:
                r = pivot-1
            elif nums[l] > target:
                l = pivot
            else:
                return l
                
        while l<r:
            mid = (l+r)//2
            if nums[mid]< target:
                l=mid+1
            else:
                r=mid
                
        if nums[r]==target:
            return r
        else:
            return -1
        
            
        
        
                