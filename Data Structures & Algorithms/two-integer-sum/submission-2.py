class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_vals = {}

        for i, num in enumerate(nums):
            diff = target - num
            if(diff in stored_vals):
                if(i<stored_vals.get(diff)):
                   return [i, stored_vals.get(diff)]
                else:
                    return [stored_vals.get(diff), i]
            else:
                stored_vals[num] = i