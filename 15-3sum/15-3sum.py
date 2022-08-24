class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array
        nums.sort()
        
        for i in range(len(nums)):
            #skip the loop if there is same number
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            
            # two sum
            while (l<r):
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # not to have same sum
                    while (l<r and nums[l] == nums[l+1]):
                        l+=1
                    while (l<r and nums[r] == nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
        return res
            