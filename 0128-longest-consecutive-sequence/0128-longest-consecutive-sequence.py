class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                temp = num
                count = 1
                while temp+1 in num_set:
                    count += 1
                    temp+=1
            maximum = max(maximum,count)
        return maximum
