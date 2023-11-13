class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            dic = {}
            for j in range(i+1, len(nums)):
                if nums[j] in dic:
                    res.append([nums[i], nums[j], dic[nums[j]]])
                dic[target - nums[j]] = nums[j]
        
        unique_combinations = set()
        for sublist in res:
            # Sort and convert to tuple for immutability
            unique_combinations.add(tuple(sorted(sublist)))

        # Convert each tuple back into a list
        unique_list = [list(combination) for combination in unique_combinations]

        return unique_list
            