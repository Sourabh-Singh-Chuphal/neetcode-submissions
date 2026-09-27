class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = []
        l = len(nums)
        for i in range(0,l):
            difference = target - nums[i]
            if difference in nums[i + 1:]:
                res_dict.append(i)
                j = nums.index(difference, i +1)
                res_dict.append(j)
        return res_dict
            

        