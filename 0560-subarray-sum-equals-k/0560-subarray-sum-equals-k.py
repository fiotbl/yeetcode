class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cum_sum = 0, 0
        sum_dict = {0:1}
        
        for num in nums:
            cum_sum += num
            
            if (cum_sum - k) in sum_dict:
                count += sum_dict[cum_sum-k]
                
            if cum_sum in sum_dict:
                sum_dict[cum_sum] += 1
            else:
                sum_dict[cum_sum] = 1
                
        return count