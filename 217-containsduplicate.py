"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        # If we reach here, there are no duplicates.
        return False


a = [1,2,3]
test1 = Solution()
print(test1.containsDuplicate(a)) # Should return False

b = [1,2,3,1]
test2 = Solution()
print(test2.containsDuplicate(b)) # Should return True
