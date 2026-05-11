class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def split_num(num):
            num = str(num)
            num = list(num)
            for i in range(len(num)):
                num[i] = int(num[i])
            return num
        temp = []
        for i in nums:
            arr = split_num(i)
            temp+=arr
        
        return temp
