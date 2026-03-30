class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = seen.get(num, 0) + 1
        counts = Counter(seen)
        top = counts.most_common(k)
        elements = [element for element, count in top]
        return elements
        
