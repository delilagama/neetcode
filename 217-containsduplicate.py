"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution:
    def containsDuplicateBrute(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        # If we reach here, there are no duplicates.
        return False

    def containsDuplicateOptimized(self, nums: list[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False
            
a = [1,2,3]
test1 = Solution()
print(test1.containsDuplicateOptimized(a)) # Should return False

b = [1,2,3,1]
test2 = Solution()
print(test2.containsDuplicateOptimized(b)) # Should return True
