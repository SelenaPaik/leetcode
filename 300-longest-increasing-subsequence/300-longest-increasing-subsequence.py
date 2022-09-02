class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 내 위치보다 뒤에 있는 원소들 중 나보다 큰 것의 갯수를 dp에 넣는다
        dp = [1] * len(nums)
        res = 0
        for i in range(len(nums)-1,-1,-1):
                for j in range(i+1,len(nums)):
                    if(nums[i] < nums[j]):
                        dp[i] = max(dp[i], 1+dp[j])
        res = max(dp)
      
        return res 