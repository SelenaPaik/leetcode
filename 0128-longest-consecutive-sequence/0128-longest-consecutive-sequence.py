class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        if(len(nums)==1): return 1
        nums.sort()
        fin=[]
        res=1
        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):
                res+=1
            elif(nums[i-1]+1<nums[i]):
                res=1
            fin.append(res)
 
        return max(fin)
        