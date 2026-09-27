class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_set = set(nums)
        return len(result_set) != len(nums)

        
        