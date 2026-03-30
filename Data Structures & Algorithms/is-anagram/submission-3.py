class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        for num1 in s:
            seen1[num1] = seen1.get(num1, 0) + 1
        seen2 = {}
        for num2 in t:
            seen2[num2] = seen2.get(num2, 0) + 1
        if seen1 == seen2:
            return True
        return False
    
     