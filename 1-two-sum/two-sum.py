from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value: index
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement already exists in our dictionary
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = index

        