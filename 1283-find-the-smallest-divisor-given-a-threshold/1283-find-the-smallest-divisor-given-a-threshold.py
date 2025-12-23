class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left<=right:
            sumval = 0
            divisor = (left+right)//2

            for num in nums:
                sumval += math.ceil(num/divisor)


            if sumval<=threshold:
                right = divisor-1
            else:
                left = divisor+1
        return left