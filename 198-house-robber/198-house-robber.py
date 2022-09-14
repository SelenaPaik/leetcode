class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        elif len(nums)==2:
            return max(nums[0], nums[1])
    
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(dp[0]+nums[2],dp[1])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2], nums[i] + dp[i-3])
        return dp[len(nums)-1]
        