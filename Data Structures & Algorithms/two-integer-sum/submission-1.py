class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_vals = {}

        for i, num in enumerate(nums):
            if(target - num in stored_vals):
                if(i<stored_vals.get(target - num)):
                   return [i, stored_vals.get(target - num)]
                else:
                    return [stored_vals.get(target - num), i]
            else:
                stored_vals[num] = i