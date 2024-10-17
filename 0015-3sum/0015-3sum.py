class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        seen = set()
        ans = []

        for i in range(n):
            l, r = i+1, n-1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0 and (nums[i], nums[l], nums[r]) not in seen:
                    seen.add((nums[i], nums[l], nums[r]))
                    ans.append([nums[i], nums[l], nums[r]])

                if summ > 0:
                    r -= 1
                
                else:
                    l += 1
        
        return ans