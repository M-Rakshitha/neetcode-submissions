class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = 1 + seen.get(num, 0)
            if seen[num] >= 2:
                return True
        return False